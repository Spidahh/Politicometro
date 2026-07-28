# Modello dati

## Entità principali

### Persona

- nome e identificativi;
- incarichi;
- organizzazioni;
- dichiarazioni;
- casi;
- diritto di replica;
- eventuali omonimie.

### Organizzazione

- partito;
- ente pubblico;
- società;
- fondazione;
- associazione;
- comitato;
- testata;
- struttura territoriale.

### Caso

Contenitore editoriale principale.

- titolo;
- sintesi;
- perché conta;
- stato;
- impatto;
- responsabilità;
- cronologia;
- soggetti;
- prove;
- affermazioni;
- repliche;
- domande aperte;
- revisioni.

### Affermazione

- testo esatto o parafrasi;
- autore;
- data;
- contesto;
- tipo: fattuale, previsione, opinione, promessa, accusa;
- verificabilità;
- verdetto;
- prove a favore e contro.

### Evento

- data;
- tipo;
- luogo;
- soggetti;
- descrizione;
- relazione con uno o più casi.

### Prova

- documento;
- articolo originale;
- video;
- audio;
- dataset;
- testimonianza;
- sentenza;
- comunicato;
- screenshot archiviato.

La prova ha origine, attendibilità contestuale, accessibilità, licenza e limiti.

### Relazione

Una relazione deve avere un tipo esplicito:

- incarico;
- partecipazione societaria;
- parentela rilevante;
- donazione dichiarata;
- collaborazione professionale;
- nomina;
- contratto;
- citazione;
- accusa;
- semplice co-presenza.

Non usare una linea generica “collegato a”.

## Indicatori

Politicometro non calcola un voto morale unico. Per ogni caso mostra indicatori separati:

- **forza delle prove**;
- **impatto pubblico**;
- **responsabilità decisionale**;
- **attualità**;
- **completezza della ricostruzione**.

Gli indicatori devono essere accompagnati da spiegazioni. Un numero non sostituisce il ragionamento.

## Grafi

Il grafo serve a trovare percorsi e ricorrenze, non a suggerire colpe per prossimità. Ogni arco deve essere cliccabile e spiegare fonte, data e natura della relazione.

## Schemi iniziali

Nel repository:

- [`../data/schema/case.schema.json`](../data/schema/case.schema.json);
- [`../data/examples/case.example.json`](../data/examples/case.example.json);
- [`../data/source-registry.example.yaml`](../data/source-registry.example.yaml).
