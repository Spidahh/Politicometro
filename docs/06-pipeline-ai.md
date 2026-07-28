# Pipeline AI

## Principio

L'AI è un assistente di ricerca e organizzazione. Non è il direttore responsabile, il giudice o la fonte.

Il sistema lavora in batch dal computer del gestore. Il sito pubblico riceve soltanto contenuti già elaborati e approvati.

## Pipeline proposta

### 1. Raccolta

- RSS e API;
- download di pagine e documenti consentiti;
- import manuale;
- inbox delle segnalazioni;
- elenco di account e canali monitorati;
- registrazione di timestamp e hash.

### 2. Conservazione

Conservare:

- contenuto originale;
- URL;
- autore;
- data di pubblicazione e acquisizione;
- eventuale licenza;
- hash;
- formato;
- testo estratto;
- metadati.

### 3. Normalizzazione

- estrazione testo;
- trascrizione audio e video;
- riconoscimento della lingua;
- pulizia;
- separazione articolo/commenti;
- rilevamento di aggiornamenti della pagina.

### 4. Deduplicazione e genealogia

Il sistema deve riconoscere:

- copie quasi identiche;
- articoli derivati da un'agenzia;
- aggiornamenti dello stesso articolo;
- citazioni reciproche;
- fonte originale probabile.

### 5. Estrazione strutturata

L'AI propone:

- persone, enti, società e luoghi;
- incarichi;
- affermazioni verificabili;
- date e importi;
- azioni e decisioni;
- relazioni dichiarate;
- stato giudiziario esplicitamente menzionato;
- fonti citate nell'articolo;
- domande ancora aperte.

### 6. Raggruppamento in eventi e casi

Articoli e documenti vengono collegati a:

- evento;
- caso;
- promessa;
- affermazione;
- flusso finanziario;
- persona o organizzazione.

### 7. Ricerca dei riscontri

Per ogni affermazione importante:

- cercare la fonte primaria;
- cercare conferme indipendenti;
- cercare smentite e spiegazioni alternative;
- cercare la replica dell'interessato;
- verificare date e importi;
- distinguere fatto, interpretazione e previsione.

### 8. Generazione della bozza

L'AI produce una bozza conforme a uno schema, con campi obbligatori e citazioni puntuali. Non deve produrre testo libero senza collegamento alle prove.

### 9. Controlli automatici

- nomi e ruoli coerenti;
- date non impossibili;
- importi con unità;
- fonti raggiungibili o archiviate;
- frasi sensibili supportate;
- stato giudiziario completo;
- presenza della replica;
- rischio di confondere omonimi;
- differenza fra società e persone.

### 10. Revisione umana

La profondità dipende dal rischio. Nessun contenuto delicato viene pubblicato soltanto perché il modello assegna alta confidenza.

### 11. Pubblicazione statica

Il sistema genera:

- JSON validati;
- pagine;
- feed;
- sitemap;
- schede social;
- registro delle versioni.

## Cosa l'AI non deve inferire

- intenzioni criminali;
- colpevolezza;
- appartenenza mafiosa;
- corruzione da semplici relazioni;
- identità di fonti anonime;
- orientamento politico dell'utente;
- equivalenza morale fra casi diversi.

## Tracciabilità

Ogni campo generato deve poter rispondere a:

> da quale passaggio e da quale fonte deriva?

Il sistema dovrebbe conservare il prompt, il modello, la versione, l'output grezzo e le modifiche umane per audit interno, rispettando privacy e licenze.
