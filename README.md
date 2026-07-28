# Politicometro

**La politica senza la curva. Prima il fatto, poi il partito.**

Politicometro è un progetto civico-editoriale pensato per rendere la politica italiana più facile da capire, ricordare e verificare. Non vuole dire alle persone per chi votare, non vuole costruire una classifica morale dei politici e non vuole sostituire giornalisti, magistrati o cittadini.

Vuole fare una cosa più concreta:

> collegare ciò che politici e partiti dicono con ciò che accade dopo, mostrando prove, conseguenze, interessi, soldi pubblici, smentite, risposte e aggiornamenti in un formato comprensibile in pochi secondi.

## Il problema

La politica online viene consumata soprattutto come rissa, meme, spezzone video, slogan o appartenenza. I contenuti più aggressivi ricevono attenzione, mentre atti complessi, inchieste locali, sviluppi giudiziari, contraddizioni e risultati concreti scompaiono rapidamente.

Politicometro nasce per affrontare cinque problemi:

1. **rumore:** le polemiche sovrastano i fatti con conseguenze reali;
2. **memoria corta:** una promessa o uno scandalo viene dimenticato dopo pochi giorni;
3. **doppio standard:** lo stesso comportamento viene giudicato diversamente in base al partito;
4. **frammentazione:** documenti, articoli, dichiarazioni e aggiornamenti sono sparsi;
5. **complessità:** chi non segue la politica ogni giorno fatica a ricostruire cosa sia davvero successo.

## Il prodotto

Il cuore non è un voto di onestà assegnato dall'intelligenza artificiale. Il cuore è una raccolta di **schede verificabili**, leggibili a tre livelli:

- **20 secondi:** cosa è successo, perché conta, cosa sappiamo davvero;
- **2 minuti:** cronologia, protagonisti, denaro, responsabilità e punti irrisolti;
- **tutte le prove:** documenti, articoli, video, dichiarazioni, repliche e cronologia delle correzioni.

I format iniziali sono:

- **La storia che gira:** controllo di una frase o narrazione virale;
- **Detto contro fatto:** confronto fra dichiarazioni, decisioni e risultati;
- **Stesso metro:** casi comparabili relativi a partiti diversi;
- **Dove sono finiti i soldi:** flussi di denaro, appalti, incarichi e beneficiari;
- **Che fine ha fatto:** aggiornamento di casi dimenticati;
- **Nebbia:** annunci importanti non ancora verificabili per mancanza di dati;
- **Una cosa fatta bene:** risultati positivi documentati.

## Principi non negoziabili

- Una fonte ufficiale non è automaticamente completa o affidabile; resta però utile come prova documentale.
- Una fonte investigativa non è automaticamente vera; può far emergere un caso da verificare.
- Un post social dimostra che qualcuno ha pubblicato una frase, non che quella frase sia vera.
- Un'indagine non equivale a una condanna.
- Un collegamento personale o societario non equivale a un illecito.
- Accuse, prove, interpretazioni e fatti accertati devono restare distinti.
- Lo stesso metodo deve valere per governo, opposizione, amministrazioni locali e soggetti non eletti.
- Gli errori devono essere corretti pubblicamente e rapidamente.
- L'AI propone, collega e riassume; non pubblica autonomamente accuse delicate.

## Architettura prevista

```text
Fonti ufficiali, investigative, locali e social
                    ↓
       raccolta batch dal computer
                    ↓
      archivio dei materiali originali
                    ↓
 normalizzazione, deduplicazione, trascrizione
                    ↓
 AI: entità, affermazioni, eventi, collegamenti
                    ↓
     motore delle prove e delle contraddizioni
                    ↓
        revisione editoriale proporzionata
                    ↓
       JSON/versioni statiche del contenuto
                    ↓
              sito pubblico
```

L'AI non deve essere live sul sito. Il processo può essere avviato dal computer del gestore e pubblicare una nuova versione statica. Il sito resta disponibile anche quando quel computer è spento.

## Sostenibilità economica

La proposta iniziale è un modello misto:

1. **membership volontaria** per mantenere gratuito il contenuto essenziale;
2. **strumenti professionali e licenze dati** per giornalisti, ricercatori, università e organizzazioni civiche;
3. **formazione, eventi e progetti finanziati** su verifica, dati pubblici e alfabetizzazione mediatica;
4. sponsorizzazioni limitate e dichiarate, soltanto dopo aver definito una carta di indipendenza.

Sono vietati:

- pubblicità di partiti, candidati e comitati elettorali;
- contenuti editoriali acquistabili;
- pagamento per rimuovere o migliorare una scheda;
- vendita dei dati personali degli utenti;
- classifiche sponsorizzate;
- accesso privilegiato alle conclusioni fattuali.

Il piano completo si trova in [`docs/08-monetizzazione.md`](docs/08-monetizzazione.md).

## Struttura della documentazione

- [`docs/00-manifesto.md`](docs/00-manifesto.md) — identità e scopo;
- [`docs/01-strategia-prodotto.md`](docs/01-strategia-prodotto.md) — proposta di valore e perimetro;
- [`docs/02-pubblico-posizionamento.md`](docs/02-pubblico-posizionamento.md) — pubblico italiano e tono;
- [`docs/03-esperienza-formati.md`](docs/03-esperienza-formati.md) — home, schede e formati social;
- [`docs/04-metodo-editoriale.md`](docs/04-metodo-editoriale.md) — verifica e pubblicazione;
- [`docs/05-strategia-fonti.md`](docs/05-strategia-fonti.md) — fonti ufficiali e supplementari;
- [`docs/06-pipeline-ai.md`](docs/06-pipeline-ai.md) — automazione batch e controlli;
- [`docs/07-modello-dati.md`](docs/07-modello-dati.md) — entità e relazioni;
- [`docs/08-monetizzazione.md`](docs/08-monetizzazione.md) — ricavi e scenari economici;
- [`docs/09-lancio-distribuzione.md`](docs/09-lancio-distribuzione.md) — crescita e social;
- [`docs/10-roadmap.md`](docs/10-roadmap.md) — percorso MVP;
- [`docs/11-rischi-legali-etici.md`](docs/11-rischi-legali-etici.md) — rischi principali;
- [`docs/12-governance-trasparenza.md`](docs/12-governance-trasparenza.md) — indipendenza e controlli;
- [`docs/13-metriche-esperimenti.md`](docs/13-metriche-esperimenti.md) — misurazione dell'impatto;
- [`docs/14-fonti-ricerca.md`](docs/14-fonti-ricerca.md) — fonti usate per questa impostazione.

## Stato

Il repository contiene per ora la visione, i requisiti e alcuni schemi iniziali. Non contiene ancora un'applicazione funzionante.

Il primo obiettivo tecnico è realizzare un prototipo con casi dimostrativi non diffamatori, dati fittizi o casi storici accuratamente documentati, così da testare comprensione, utilità e tono prima di automatizzare la raccolta.
