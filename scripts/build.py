#!/usr/bin/env python3
"""Interroga i dati aperti della Camera e rigenera index.html.

Fonte: https://dati.camera.it/sparql (endpoint ufficiale della Camera
dei deputati). Nessuna dipendenza esterna: solo libreria standard.
"""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EP = "https://dati.camera.it/sparql"
OCD = "http://dati.camera.it/ocd"
DC = "http://purl.org/dc/elements/1.1"

# Legislature repubblicane: numero -> (inizio, fine o None se in corso)
LEGISLATURE = {
    19: (date(2022, 10, 13), None),
    18: (date(2018, 3, 23), date(2022, 10, 12)),
    17: (date(2013, 3, 15), date(2018, 3, 22)),
    16: (date(2008, 4, 29), date(2013, 3, 14)),
    15: (date(2006, 4, 28), date(2008, 4, 28)),
    14: (date(2001, 5, 30), date(2006, 4, 27)),
}


def chiedi(query, tentativi=3):
    url = EP + "?" + urllib.parse.urlencode({"query": query})
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/sparql-results+json",
            "User-Agent": "Politicometro/1.0 (+https://github.com/Spidahh/Politicometro)",
        },
    )
    for n in range(tentativi):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.load(r)["results"]["bindings"]
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
            if n == tentativi - 1:
                raise
            print(f"    ritento ({e})", file=sys.stderr)
    return []


def per_legislatura(filtro=""):
    """Conta le votazioni d'assemblea per legislatura, senza doppioni.

    COUNT(DISTINCT) e' obbligatorio: alcune votazioni hanno piu' valori
    per la stessa proprieta' e un COUNT(*) raddoppierebbe i totali.
    """
    q = f"""SELECT ?leg (COUNT(DISTINCT ?s) AS ?n) WHERE {{
      ?s a <{OCD}/votazione> ; <{OCD}/rif_leg> ?leg . {filtro}
    }} GROUP BY ?leg ORDER BY DESC(?leg) LIMIT 8"""
    fuori = {}
    for b in chiedi(q):
        try:
            fuori[int(b["leg"]["value"].rsplit("_", 1)[-1])] = int(b["n"]["value"])
        except ValueError:
            continue
    return fuori


def ultima_seduta():
    q = f"""SELECT (MAX(?d) AS ?d) WHERE {{
      ?s a <{OCD}/votazione> ; <{DC}/date> ?d
    }}"""
    r = chiedi(q)
    grezzo = r[0]["d"]["value"] if r and "d" in r[0] else ""
    if len(grezzo) >= 8 and grezzo[:8].isdigit():
        return date(int(grezzo[:4]), int(grezzo[4:6]), int(grezzo[6:8]))
    return None


def anni(n, fine_dati):
    inizio, fine = LEGISLATURE[n]
    fine = fine or fine_dati or date.today()
    return max((fine - inizio).days / 365.25, 0.1)


# ------------------------------------------------------------------ html

MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
        "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]


def data_it(d):
    return f"{d.day} {MESI[d.month - 1]} {d.year}"


def num(n):
    return f"{n:,}".replace(",", ".")


def barre(righe, corrente, suffisso=""):
    """righe: [(etichetta, valore_mostrato, valore_barra, nota)]"""
    massimo = max((r[2] for r in righe), default=1) or 1
    out = []
    for etichetta, mostrato, valore, nota in righe:
        largo = max(valore / massimo * 100, 1.2)
        cls = " ora" if etichetta == corrente else ""
        out.append(
            f'      <div class="riga{cls}">\n'
            f'        <span class="et">{etichetta}<b>{nota}</b></span>\n'
            f'        <span class="pista"><i style="width:{largo:.1f}%"></i></span>\n'
            f'        <span class="vl">{mostrato}{suffisso}</span>\n'
            f"      </div>"
        )
    return "\n".join(out)


def main():
    print("Interrogo dati.camera.it")

    fine_dati = ultima_seduta()
    print(f"  ultima votazione in archivio: {fine_dati}")

    tot = per_legislatura()
    print("  totali ok")
    fid = per_legislatura(f'?s <{OCD}/richiestaFiducia> ?f . FILTER(str(?f)="1")')
    print("  fiducie ok")
    seg = per_legislatura(f'?s <{OCD}/votazioneSegreta> ?g . FILTER(str(?g)="1")')
    print("  segrete ok")
    app = per_legislatura(f'?s <{OCD}/approvato> ?a . FILTER(str(?a)="1")')
    print("  approvate ok")

    legs = [n for n in sorted(LEGISLATURE, reverse=True) if tot.get(n)]
    if not legs:
        print("Nessun dato: index.html lasciato com'e'.", file=sys.stderr)
        return 1

    ora = legs[0]

    def et(n):
        i, f = LEGISLATURE[n]
        f = f or fine_dati or date.today()
        return f"{i.year}-{f.year}"

    corrente = et(ora)

    # 1. fiducie all'anno
    r_fid = []
    for n in legs:
        a = anni(n, fine_dati)
        v = fid.get(n, 0)
        r_fid.append((et(n), f"{v / a:.1f}", v / a, f"{v} in {a:.1f} anni"))

    # 2. voti segreti all'anno
    r_seg = []
    for n in legs:
        a = anni(n, fine_dati)
        v = seg.get(n, 0)
        r_seg.append((et(n), f"{v / a:.1f}", v / a, f"{v} in tutto"))

    # 3. quota di votazioni approvate
    r_app = []
    for n in legs:
        t, v = tot[n], app.get(n, 0)
        q = 100 * v / t if t else 0
        r_app.append((et(n), f"{q:.0f}%", q, f"{num(v)} su {num(t)}"))

    fid_ora = fid.get(ora, 0)
    anni_ora = anni(ora, fine_dati)
    ritmo_ora = fid_ora / anni_ora
    ritmo_prima = sum(fid.get(n, 0) for n in legs[1:]) / sum(anni(n, fine_dati) for n in legs[1:])

    template = (ROOT / "scripts" / "template.html").read_text(encoding="utf-8")
    pagina = (
        template
        .replace("{{FIDUCIE}}", barre(r_fid, corrente))
        .replace("{{SEGRETE}}", barre(r_seg, corrente))
        .replace("{{APPROVATE}}", barre(r_app, corrente))
        .replace("{{N_FIDUCIE}}", str(fid_ora))
        .replace("{{RITMO_ORA}}", f"{ritmo_ora:.1f}")
        .replace("{{RITMO_PRIMA}}", f"{ritmo_prima:.1f}")
        .replace("{{N_VOTAZIONI}}", num(tot[ora]))
        .replace("{{N_SEGRETE}}", str(seg.get(ora, 0)))
        .replace("{{LEG}}", str(ora))
        .replace("{{DAL}}", data_it(LEGISLATURE[ora][0]))
        .replace("{{ULTIMA}}", data_it(fine_dati) if fine_dati else "-")
        .replace("{{AGGIORNATO}}", datetime.now(timezone.utc).strftime("%d.%m.%Y"))
    )

    (ROOT / "index.html").write_text(pagina, encoding="utf-8")
    (ROOT / "dati.json").write_text(
        json.dumps(
            {
                "fonte": EP,
                "ultima_votazione": str(fine_dati),
                "legislature": {
                    str(n): {
                        "dal": str(LEGISLATURE[n][0]),
                        "al": str(LEGISLATURE[n][1] or fine_dati),
                        "votazioni": tot[n],
                        "fiducie": fid.get(n, 0),
                        "segrete": seg.get(n, 0),
                        "approvate": app.get(n, 0),
                    }
                    for n in legs
                },
            },
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )
    print("Scritti index.html e dati.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
