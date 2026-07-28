#!/usr/bin/env python3
"""Raccoglie i feed di politica italiana e rigenera index.html.

Nessuna dipendenza esterna: solo libreria standard, cosi' gira ovunque
(GitHub Actions incluso) senza installare niente.
"""

import html
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent.parent
USER_AGENT = "Mozilla/5.0 (compatible; Politicometro/1.0; +https://github.com/Spidahh/Politicometro)"
GIORNI = 5
GENERALISTI = {"Open"}  # feed non solo politici: vanno filtrati per parole chiave

FONTI = [
    ("ANSA",      "https://www.ansa.it/sito/notizie/politica/politica_rss.xml"),
    ("Il Post",   "https://www.ilpost.it/politica/feed/"),
    ("Adnkronos", "https://www.adnkronos.com/RSS_Politica.xml"),
    ("Il Sole",   "https://www.ilsole24ore.com/rss/italia--politica.xml"),
    ("Repubblica", "https://www.repubblica.it/rss/politica/rss2.0.xml"),
    ("Rainews",   "https://www.rainews.it/rss/politica"),
    ("Open",      "https://www.open.online/feed/"),
]

TEMI = [
    ("Giustizia", [
        "magistrat\\w*", "procur\\w*", "tribunal\\w*", "process\\w*", "indagat\\w*",
        "condann\\w*", "assolt\\w*", "intercettazion\\w*", "chat", "csm", "consulta",
        "corte costituzionale", "cassazione", "giudic\\w*", "inchiest\\w*", "reato",
        "carcer\\w*", "giustizia", "toghe", "separazione delle carriere", "nordio",
    ]),
    ("Soldi pubblici", [
        "manovra", "bilancio", "tass\\w*", "irpef", "fisco", "pnrr", "appalt\\w*",
        "miliard\\w*", "milion\\w*", "deficit", "debito", "pension\\w*", "salari\\w*",
        "stipend\\w*", "bonus", "cuneo", "spending review", "conti pubblici",
    ]),
    ("Parlamento", [
        "camera", "senato", "aula", "fiducia", "emendament\\w*", "ddl", "decreto",
        "giunta", "commissione", "legge elettorale", "parlament\\w*", "deputat\\w*",
        "senator\\w*", "maggioranza", "opposizion\\w*", "voto",
    ]),
    ("Immigrazione", [
        "migrant\\w*", "sbarch\\w*", "hotspot", "albania", "rimpatri\\w*", "cpr",
        "profugh\\w*", "richiedenti asilo", "flussi", "immigrazion\\w*",
    ]),
    ("Territori", [
        "region\\w*", "comune", "sindac\\w*", "governator\\w*", "consiglio regionale",
        "autonomia differenziata", "elezioni regionali",
    ]),
    ("Estero e difesa", [
        "ucraina", "gaza", "israele", "nato", "unione europea", "bruxelles",
        "dazi", "trump", "iran", "difesa", "riarmo", "guerra", "putin", "zelensky",
    ]),
]

POLITICO = [
    "governo", "meloni", "schlein", "conte", "salvini", "tajani", "renzi",
    "calenda", "parlament\\w*", "camera", "senato", "ministr\\w*", "partito",
    "m5s", "lega", "forza italia", "fratelli d'italia", "avs", "opposizion\\w*",
    "maggioranza", "premier", "quirinale", "consiglio dei ministri", "mattarella",
    "pd", "onorevole", "coalizione", "elezioni",
]


def _regex(parole):
    return re.compile(r"\b(?:" + "|".join(parole) + r")\b", re.IGNORECASE)


TEMI_RE = [(nome, _regex(parole)) for nome, parole in TEMI]
POLITICO_RE = _regex(POLITICO)


def scarica(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def testo(nodo, *nomi):
    for n in nomi:
        el = nodo.find(n)
        if el is not None and el.text:
            return el.text.strip()
    return ""


def quando(grezzo):
    if not grezzo:
        return None
    try:
        d = parsedate_to_datetime(grezzo)
    except (TypeError, ValueError):
        try:
            d = datetime.fromisoformat(grezzo.replace("Z", "+00:00"))
        except ValueError:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(timezone.utc)


def pulisci(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def chiave(titolo):
    return re.sub(r"[^a-z0-9]+", "", titolo.lower())[:70]


def tema(titolo):
    for nome, rx in TEMI_RE:
        if rx.search(titolo):
            return nome
    return "Altro"


def e_politica(titolo):
    return bool(POLITICO_RE.search(titolo)) or tema(titolo) != "Altro"


def locale(tag):
    return tag.rsplit("}", 1)[-1]


def figlio(nodo, *nomi):
    """Testo del primo figlio con quel nome, ignorando i namespace."""
    for el in nodo:
        if locale(el.tag) in nomi:
            if el.text and el.text.strip():
                return el.text.strip()
            href = el.get("href")
            if href:
                return href.strip()
    return ""


def leggi_feed(nome, url):
    try:
        raw = scarica(url)
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        print(f"  ! {nome}: {e}", file=sys.stderr)
        return []

    # alcuni feed hanno BOM o righe vuote prima della dichiarazione xml
    raw = raw.lstrip(b"\xef\xbb\xbf").lstrip()

    try:
        radice = ElementTree.fromstring(raw)
    except ElementTree.ParseError as e:
        print(f"  ! {nome}: xml illeggibile ({e})", file=sys.stderr)
        return []

    voci = []
    for item in radice.iter():
        if locale(item.tag) not in ("item", "entry"):
            continue
        titolo = pulisci(figlio(item, "title"))
        link = figlio(item, "link", "guid", "id")
        data = quando(figlio(item, "pubDate", "published", "updated", "date"))
        if not titolo or not link.startswith("http") or not data:
            continue
        voci.append({"titolo": titolo, "link": link, "data": data, "fonte": nome})

    print(f"  {nome}: {len(voci)}")
    return voci


def raccogli():
    limite = datetime.now(timezone.utc) - timedelta(days=GIORNI)
    viste, fuori = set(), []

    for nome, url in FONTI:
        for v in leggi_feed(nome, url):
            if v["data"] < limite:
                continue
            if nome in GENERALISTI and not e_politica(v["titolo"]):
                continue
            k = chiave(v["titolo"])
            if not k or k in viste:
                continue
            viste.add(k)
            v["tema"] = tema(v["titolo"])
            fuori.append(v)

    fuori.sort(key=lambda v: v["data"], reverse=True)
    return fuori


# ---------------------------------------------------------------- html

GIORNI_IT = ["lunedì", "martedì", "mercoledì", "giovedì",
             "venerdì", "sabato", "domenica"]
MESI_IT = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
           "agosto", "settembre", "ottobre", "novembre", "dicembre"]


def data_lunga(d):
    return f"{GIORNI_IT[d.weekday()]} {d.day} {MESI_IT[d.month - 1]}"


def esc(s):
    return html.escape(s, quote=True)


def rendi(voci, template):
    adesso = datetime.now(timezone.utc)

    conteggi = {}
    for v in voci:
        conteggi[v["tema"]] = conteggi.get(v["tema"], 0) + 1
    ordinati = sorted(conteggi.items(), key=lambda kv: kv[1], reverse=True)

    chips = "\n".join(
        f'        <button class="chip" type="button" data-tema="{esc(t)}">'
        f'{esc(t)}<b>{n}</b></button>'
        for t, n in ordinati
    )

    blocchi, giorno_corrente = [], None
    for v in voci:
        locale = v["data"] + timedelta(hours=2)  # ora italiana, estate
        g = locale.date()
        if g != giorno_corrente:
            if giorno_corrente is not None:
                blocchi.append("      </div>")
            etichetta = "oggi" if g == (adesso + timedelta(hours=2)).date() else data_lunga(locale)
            blocchi.append(f'      <h3 class="giorno">{esc(etichetta)}</h3>')
            blocchi.append('      <div class="lista">')
            giorno_corrente = g

        blocchi.append(
            f'        <a class="voce" data-tema="{esc(v["tema"])}" href="{esc(v["link"])}"'
            f' target="_blank" rel="noopener noreferrer">\n'
            f'          <span class="ora">{locale.strftime("%H:%M")}</span>\n'
            f'          <span class="tit">{esc(v["titolo"])}</span>\n'
            f'          <span class="meta"><b class="tema">{esc(v["tema"])}</b>'
            f'<b class="fonte">{esc(v["fonte"])}</b></span>\n'
            f"        </a>"
        )
    if giorno_corrente is not None:
        blocchi.append("      </div>")

    aggiornato = (adesso + timedelta(hours=2)).strftime("%d.%m.%Y ore %H:%M")

    return (template
            .replace("{{CHIPS}}", chips)
            .replace("{{VOCI}}", "\n".join(blocchi))
            .replace("{{TOTALE}}", str(len(voci)))
            .replace("{{FONTI}}", str(len(FONTI)))
            .replace("{{GIORNI}}", str(GIORNI))
            .replace("{{AGGIORNATO}}", aggiornato))


def main():
    print("Raccolta feed:")
    voci = raccogli()
    print(f"Totale utilizzabili: {len(voci)}")

    if not voci:
        print("Nessuna voce: index.html lasciato com'e'.", file=sys.stderr)
        return 1

    template = (ROOT / "scripts" / "template.html").read_text(encoding="utf-8")
    (ROOT / "index.html").write_text(rendi(voci, template), encoding="utf-8")
    (ROOT / "dati.json").write_text(
        json.dumps(
            [{**v, "data": v["data"].isoformat()} for v in voci],
            ensure_ascii=False, indent=1,
        ),
        encoding="utf-8",
    )
    print("Scritti index.html e dati.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
