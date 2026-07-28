# Strategia delle fonti

## Nessuna fonte basta da sola

Le fonti ufficiali possono essere incomplete, tardive, difficili da consultare o costruite per rappresentare l'azione dell'istituzione. Le fonti giornalistiche possono avere errori, interessi, limiti o dipendere da una stessa origine. I social possono far emergere documenti e testimonianze, ma anche manipolazioni.

Politicometro usa un sistema a strati.

## Strato A — Segnali

Serve a scoprire storie:

- giornalismo investigativo;
- stampa locale;
- associazioni antimafia e anticorruzione;
- osservatori ambientali, sanitari e sul lavoro;
- sindacati e categorie professionali;
- interrogazioni e denunce politiche;
- whistleblower;
- comitati territoriali;
- social di giornalisti, amministratori e cittadini;
- podcast e video investigativi;
- pagine rimosse o modificate.

Un segnale entra nella coda privata e non è automaticamente pubblicabile.

## Strato B — Inchieste e competenza

Fonti capaci di produrre ricostruzioni originali:

- redazioni investigative italiane e internazionali;
- giornalisti specializzati in appalti, giustizia, sanità, ambiente e criminalità organizzata;
- analisti di dati pubblici;
- esperti accademici;
- organizzazioni civiche con metodologia dichiarata.

L'affidabilità viene valutata per singolo contenuto:

- documenti mostrati;
- fonti nominative o anonime;
- metodologia;
- contraddittorio;
- correzioni;
- conferme indipendenti;
- distinzione fra ipotesi e fatti.

## Strato C — Riscontri documentali

Serve a verificare e precisare:

- atti amministrativi;
- contratti e bandi;
- bilanci;
- registri societari e titolarità effettiva, nei limiti di legge;
- sentenze e provvedimenti disponibili;
- Gazzetta Ufficiale e Normattiva;
- Camera e Senato quando pertinenti;
- ANAC, OpenBDAP, OpenCoesione;
- albi, organigrammi e amministrazione trasparente;
- richieste di accesso civico;
- comunicati e repliche ufficiali.

La fonte ufficiale non determina l'agenda, ma può rafforzare o smentire una ricostruzione.

## Strato D — Dichiarazioni originali

- video completi;
- trascrizioni;
- interviste;
- comunicati;
- account verificati;
- conferenze stampa;
- interventi pubblici.

Occorre conservare copia, data, contesto e URL. Uno spezzone non deve essere analizzato senza cercare la versione completa.

## Strato E — Social e messaggistica

I social servono per:

- identificare narrazioni virali;
- trovare fonti originali;
- rilevare post cancellati;
- osservare campagne coordinate;
- raccogliere segnalazioni.

Non devono essere usati per trasformare popolarità, sentiment o numero di condivisioni in prova.

## Registro delle fonti

Per ogni fonte:

```yaml
name: Testata o ente
kind: official | investigative | local | expert | social | civil_society
ownership: gruppo o soggetto noto
territory: nazionale o locale
access: rss | api | web | manual | licensed
original_reporting: true
corrections_policy: present
known_dependencies:
  - agenzia o fonte frequentemente ripresa
notes: limiti e punti di forza
```

## Priorità territoriale

Il sistema deve includere progressivamente:

- regioni;
- comuni capoluogo;
- aziende sanitarie;
- società partecipate;
- consorzi;
- autorità portuali;
- università;
- aziende di trasporto e rifiuti.

Molte storie nazionali iniziano come notizie locali apparentemente isolate.
