# Studio di base — Politicometro

**Data:** 28 luglio 2026
**Stato:** studio, non decisioni. Niente di quanto segue è approvato.

---

## Premessa: il vincolo che decide tutto

Il progetto ha un vincolo che viene prima di ogni altra cosa:

> Il sito non dice mai una conclusione. Mostra i fatti con lo stesso identico metro per tutti, e la conclusione se la fa il lettore da solo. Uno di destra, uno di sinistra e uno che non vota devono poterci stare dentro tutti e tre senza sentirsi attaccati.

Non è un vincolo morale, è un vincolo tecnico. Se il sito emette un giudizio — anche uno solo, anche implicito, anche giusto — metà del pubblico se ne va e non torna più. Tutto lo studio qui sotto serve a capire **come si costruisce un oggetto del genere e se può funzionare davvero.**

Il secondo vincolo: deve essere **quasi divertente**. Non un archivio, non un convegno. Roba che uno apre per curiosità e resta lì dieci minuti.

---

## 1. Il problema, misurato

Non è un'impressione. I numeri sono grossi e vanno tutti nella stessa direzione.

**La gente ha smesso di votare.**
- Regionali 2025: nelle sei regioni al voto l'affluenza è stata del **44,7%**, contro il 57,2% delle precedenti. Meno 12,5 punti, **2.291.000 elettori in meno** in valore assoluto.
- Europee 2024: sotto il 50% per la prima volta nella storia (48,3%).
- Nelle regionali degli ultimi anni si è arrivati al 37% nel Lazio.

**Il motivo non è la pigrizia.**
- Il **73%** degli italiani non si sente rappresentato dalla classe politica attuale.
- Il **63%** non crede di poter influire con il proprio voto.
- Il **35%** indica la sfiducia nella classe politica come motivo principale dell'astensione — è la prima causa dichiarata.

**I partiti sono ultimi in ogni classifica di fiducia.** ISTAT, rilevazione 2024: flessione generalizzata della fiducia istituzionale, con i partiti politici in fondo alla classifica — oltre il 50% dei cittadini gli assegna un voto tra 1 e 5. Sopra la sufficienza restano solo vigili del fuoco, forze dell'ordine e Presidente della Repubblica.

**E ha anche smesso di informarsi.**
- Solo il **39%** degli italiani si dichiara "molto" o "estremamente" interessato alle notizie: uno dei livelli più bassi d'Europa.
- La fiducia nelle notizie è al **36%**, e — dato decisivo per noi — premia le testate **percepite come meno schierate** e quelle locali.
- Solo il **9%** paga per informazione online. Il **69%** dice che *nessuna offerta* lo convincerebbe ad abbonarsi.
- Social, aggregatori e video hanno **superato** TV, carta e siti di news come fonte principale.

### Cosa ci dice questo

C'è un pubblico enorme, molto più grande di quello dei lettori di politica: **la gente che ha mollato.** Non è un pubblico difficile perché è stupido. È difficile perché è **stufo**, e ha una soglia di sopportazione bassissima per qualunque cosa somigli a un predicozzo.

Questo pubblico non lo raggiungi con la qualità. Lo raggiungi togliendo i motivi per cui se n'è andato.

E il dato sul 69% che non pagherebbe mai chiude una porta in partenza: **qualunque piano basato sugli abbonamenti dei lettori italiani parte perdente.** Va tenuto presente quando si parlerà di soldi.

---

## 2. Il problema più difficile: l'effetto "media ostile"

Qui c'è la cosa che va capita meglio di tutte, perché è quella che può uccidere il progetto.

La ricerca la chiama **hostile media effect**: chi ha una posizione politica tende a percepire un contenuto neutro come *sbilanciato contro di sé*. Non contro gli altri: contro di sé. Due persone di parti opposte guardano lo stesso identico articolo neutrale e **tutte e due** escono convinte che favorisse l'altra parte.

Aggravante documentata: il pubblico di destra ha in media un livello di diffidenza più alto verso le fonti di informazione e consuma una gamma più stretta di fonti; quello di sinistra tende a fidarsi e consumare più fonti diverse. Vuol dire che **la soglia di sospetto non è simmetrica**, e un sito che vuole essere letto da tutti deve superare la barra più alta delle due, non la media.

Conseguenza operativa, ed è la conclusione più importante di questo studio:

> **L'apoliticità non è un'intenzione, è un'architettura.** Non basta essere onesti: il lettore diffidente deve poter *verificare da solo, in tre secondi e senza fidarsi di noi*, che il metro è lo stesso per tutti. Se glielo dobbiamo spiegare, abbiamo già perso.

Da qui derivano quasi tutte le regole di design della sezione 6.

---

## 3. Cosa funziona davvero (e cosa no)

### I fatti, presentati bene, funzionano

Il più grande studio sperimentale sul tema (esperimenti simultanei in quattro paesi, pubblicato su PNAS) trova che le correzioni fattuali aumentano l'accuratezza delle convinzioni di **0,59 punti su una scala a 5**, mentre l'esposizione alla disinformazione le peggiora solo di 0,07. In pratica: **il fatto pesa circa otto volte più della balla.**

Due limiti seri, però, e vanno progettati attorno:
1. **L'effetto svanisce col tempo** se passa troppo tra la balla e la correzione. → il sito non può essere un archivio consultato una volta: deve essere qualcosa che si *riattraversa*.
2. **L'effetto dipende da ideologia e convinzioni pregresse.** → torna il punto 2: conta chi lo dice e come, non solo cosa.

E un dato che ridimensiona l'entusiasmo: uno studio del 2024 sulle Community Notes di X ha trovato più fact-check pubblicati, ma **nessuna prova** che riducessero l'ingaggio con i post fuorvianti. Segnalare non basta. **Il formato conta più del contenuto.**

### Il gioco funziona sul serio

- Ricerca del Center for Media Engagement: chi fa un **quiz politico** dichiara poi **più interesse per le notizie politiche** rispetto a chi ha fatto un quiz su celebrità. Il quiz non è una furbata: è un vettore misurato.
- Gli editori usano giochi e puzzle come motore principale di **formazione dell'abitudine** e fidelizzazione — è ormai una colonna portante dei modelli editoriali digitali.
- Quiz, sondaggi e infografiche interattive risultano efficaci nel presentare materiale elettorale in modo che la gente lo attraversi invece di scorrerlo.

### Il caso che assomiglia di più a quello che vuoi tu: il Wahl-O-Mat

Germania, dal 2002, gestito dall'agenzia federale per l'educazione civica. Funziona così: politologi preparano ~38 domande su temi concreti; **i partiti rispondono**; il cittadino risponde alle stesse domande; dopo circa tre minuti vede quanto è vicino a ciascun partito.

I numeri: **6,7 milioni di consultazioni nel 2009, circa il 12% dell'elettorato.**

Perché è il modello più interessante per noi:
- **Non giudica nessuno.** Non dice "questo partito è buono". Mette solo il cittadino e le posizioni sullo stesso piano.
- **Il verdetto lo produce l'utente**, con le sue risposte. È letteralmente il meccanismo che chiedi tu: la gente ci arriva da sola.
- È **divertente**: dura tre minuti, il risultato è personale, è condivisibile.
- È **inattaccabile politicamente**, perché le posizioni le hanno scritte i partiti stessi.
- Effetto collaterale documentato: costringe la discussione sui *contenuti* invece che su personaggi, immagini ed eventi di campagna.

Limite: è tarato sulle elezioni e sulle *posizioni dichiarate*, non su cosa è successo dopo. È metà del problema, non tutto.

### I promise tracker

Il **Polimeter** (Canada, dal 2013, gestito da politologi universitari, dichiaratamente non-partisan) traccia le promesse elettorali e ne pubblica lo stato. Metodo: solo impegni **formali e verificabili** presi in campagna (programma ufficiale, comunicato, documento depositato); le promesse vaghe o irrilevanti **vengono scartate**; la classificazione è fatta da più codificatori indipendenti.

Risultati che vale la pena guardare, perché sono controintuitivi: governo Trudeau 2015-2019, **353 promesse, 92,2% mantenute in tutto o in parte**. Nel mandato di minoranza 2019-2021, invece, 52%.

Due lezioni per noi:
1. **La metodologia pubblica e la selezione severa sono ciò che rende il tracker credibile a entrambe le parti.** Se il criterio è pubblico e applicato meccanicamente, chi contesta deve contestare il metodo, non il risultato — e il metodo è verificabile.
2. **Il risultato può essere lusinghiero per il politico.** E va bene così, anzi: è la prova migliore che lo strumento non è una macchina da fango. Un tracker che dà sempre torto a tutti è un tracker che nessuno crede.

---

## 4. Chi c'è già in Italia, e cosa lascia scoperto

**openpolis / openparlamento** (fondazione indipendente, dal 2008): dati ufficiali di Camera e Senato riorganizzati in aperto. Presenze e assenze nei voti elettronici, cambi di gruppo, voti espressi, coesione interna dei gruppi, peso politico dei singoli parlamentari, iter dei ddl, composizione delle commissioni, "voti chiave".

È materiale eccellente. Ma è costruito **per chi già sa cosa cerca**: è uno strumento da addetti ai lavori, con indicatori da capire prima di poterli usare.

**Pagella Politica**: fact-checking delle dichiarazioni, formato classico "dichiarazione → verdetto". Il verdetto è esplicito e viene dalla redazione — cioè esattamente il modello che tu non vuoi.

### Lo spazio vuoto

Nessuno dei due copre il posto dove sta la gente che ha mollato:

| | Dati grezzi | Fact-check | **Spazio vuoto** |
|---|---|---|---|
| Chi lo usa | ricercatori, giornalisti | chi già segue la politica | **chi ha mollato** |
| Cosa chiede | precisione | verdetto | *"ma quindi com'è messa davvero?"* |
| Verdetto | assente ma illeggibile | esplicito, della redazione | **lo produce il lettore** |
| Tempo richiesto | ore | minuti | **secondi** |

Questo spazio è vuoto in Italia. È lì che va il progetto.

---

## 5. Le materie prime: cosa esiste già, gratis

Buona notizia: **i dati ci sono, sono pubblici e sono enormi.** Il progetto non deve fare inchieste — deve rendere leggibile roba che è già lì e che nessuno guarda.

- **Camera e Senato — open data ufficiali.** Voti in assemblea, atti, iter. È la fonte da cui attinge anche openparlamento.
- **ANAC — portale open data (`dati.anticorruzione.it`).** Appalti pubblici in formato **OCDS** (standard internazionale): oltre **70 milioni di contratti dal 2007 al 2024**, **38.000 stazioni appaltanti**, **238.000 imprese**. Dashboard e dataset scaricabili liberamente.
- **OpenCoesione** (`opencoesione.gov.it`): tutti i progetti finanziati con fondi europei e nazionali di coesione, dal Sistema nazionale di monitoraggio, **aggiornati ogni due mesi**, scaricabili. Include la localizzazione: si può arrivare al singolo progetto **nel comune del lettore**.
- **OpenCUP**: anagrafe nazionale dei progetti di investimento pubblico.
- **Soldipubblici**: spesa delle amministrazioni.
- **dati.gov.it**: catalogo nazionale.
- **ISTAT**: dati socio-economici, per mettere le promesse a confronto con la realtà misurata.

Il pezzo più promettente è **OpenCoesione incrociato con ANAC**, perché permette una cosa che nessuno fa: partire dal **CAP del lettore**. Non "la politica italiana", ma "i soldi pubblici arrivati nel tuo comune, e che fine hanno fatto". La localizzazione batte l'astrazione, e i dati locali sono anche quelli su cui la fiducia è più alta (vedi §1).

---

## 6. Le regole di design che derivano da questo studio

Queste non sono opinioni: sono le conseguenze operative di §2 e §3.

**1. Il sito non usa mai una parola di verdetto.** Mai "corrotto", "mente", "fallito", "scandalo", "promessa tradita". Nemmeno "purtroppo". I fatti stanno lì, in ordine, e basta. La parola di giudizio è il punto esatto in cui perdi metà del pubblico.

**2. Simmetria obbligatoria e visibile.** Ogni cosa mostrata per una parte deve essere mostrata, nello stesso identico formato, per tutte le altre. Non "per equilibrio": perché il lettore diffidente deve poterlo **verificare con l'occhio in tre secondi**, senza leggere niente. La simmetria è la prova, e la prova deve essere grafica.

**3. Il criterio è pubblico e meccanico.** Come il Polimeter: cosa entra, cosa esce, chi decide. Chi contesta deve contestare il metodo, non il risultato. E il metodo dev'essere così noioso e rigido che contestarlo non conviene.

**4. Il lettore fa il lavoro finale.** Il sito accosta. Non conclude. La frase-tipo del sito è *"ha detto X — poi è successo Y"*, punto. Il "quindi" è del lettore, ed è per questo che ci crede: se l'è dedotto lui.

**5. Le cose fatte bene si mostrano, con lo stesso rilievo.** Non per buonismo: è **il test di credibilità più importante che abbiamo.** Un sito dove ogni tanto la tua parte ne esce bene è un sito che non stai leggendo per farti dare ragione — ed è l'unica cosa che disinnesca l'effetto media ostile. Nessuna quota, nessun bilancino: se il fatto c'è, si pubblica.

**6. Nessun punteggio complessivo, nessuna classifica.** Un numero unico "onestà: 4/10" è un giudizio travestito da dato: è la cosa più condivisibile e insieme la più letale. Il momento in cui esiste una classifica, il sito diventa un'arma di una parte e ha finito di essere apolitico.

**7. Venti secondi, poi il resto se lo vuoi.** L'unità base si legge nel tempo di uno scroll. Tutta la profondità sta sotto, per chi la cerca.

**8. Il tono è piatto e un po' ironico, mai indignato.** L'indignazione è la firma di una parte. Il distacco è l'unica voce che possono ascoltare tutti.

**9. Il sito non spiega mai sé stesso.** Niente manifesto, niente "il problema", niente "perché questo sito esiste", niente "in Italia la politica è diventata rissa". Il lettore lo sa già — glielo si dice da vent'anni. Sentirselo spiegare significa essere trattato da ignorante, ed è il modo più veloce per farlo uscire.

Corollario, ed è una regola di lavoro più che di design: **le frasi con cui si descrive il progetto a chi lo costruisce non sono testo del sito.** Servono a stabilire l'intenzione, e poi vanno buttate. Quando finiscono in pagina diventano due cose insieme: una spiegazione inutile e una presa di posizione. È l'errore che c'è già dentro `README.md` e `docs/00-manifesto.md` — la lista "rumore, memoria corta, doppio standard, frammentazione, complessità" è una descrizione interna del problema, finita per sbaglio davanti al lettore.

Il sito mostra e basta. Il perché lo capisce chi guarda.

---

## 7. Formati candidati (in ordine di quanto sono sostenuti da evidenza)

Non sono proposte da approvare: sono le opzioni che lo studio fa emergere come le più solide.

**A. Il confronto secco — "detto / poi successo"**
Dichiarazione datata, con fonte, accanto a cosa risulta essere successo dopo, con fonte. Nessun commento. Il formato dove la regola 4 è più pura, e il più facile da rendere simmetrico.
*Evidenza:* PNAS (i fatti pesano 8x), Polimeter (metodo meccanico = credibilità).

**B. Il quiz "riconosci chi l'ha detto"**
Una frase vera, presa da un atto o una dichiarazione. Chi l'ha detta? Quattro opzioni, tutte plausibili. Il lettore sbaglia — e sbagliare è **l'unico modo in cui una persona cambia idea senza che nessuno gliela cambi.** Il sito non ha detto niente: ha solo fatto una domanda.
*Evidenza:* è il meccanismo del Wahl-O-Mat (la conclusione la produce l'utente) unito a quello dei quiz (aumento misurato dell'interesse politico).
Questo è il formato che regge meglio contemporaneamente i due vincoli tuoi: **apolitico** e **quasi divertente**.

**C. "Nel tuo comune"**
Il lettore mette il CAP. Vede i soldi pubblici arrivati lì, i progetti, lo stato, chi ha preso l'appalto. Nessun giudizio: solo i suoi soldi e la sua strada.
*Evidenza:* fiducia più alta sul locale (§1), disponibilità dei dati (§5), e la localizzazione come antidoto all'astrazione.

**D. "Che fine ha fatto"**
Casi grossi di qualche anno fa, e cosa risulta oggi. Attacca direttamente il decadimento dell'effetto nel tempo documentato dalla ricerca sul fact-checking.

**E. Il vicino politico**
Alla Wahl-O-Mat, ma sui voti reali espressi in parlamento invece che sulle dichiarazioni: rispondi su dieci questioni concrete, scopri con chi hai votato uguale senza saperlo. Il più potente e il più delicato: va costruito solo su voti nominali documentati.

---

## 8. Le trappole (cosa fa scappare la gente)

Ricavate per contrasto da tutto quanto sopra:

- **Un punteggio unico.** Vedi regola 6.
- **Qualunque aggettivo.** "Grave", "clamoroso", "vergognoso": ogni aggettivo è una bandiera.
- **La simmetria che si vede solo se leggi tutto.** Se per accorgersi che il metro è lo stesso bisogna leggere venti schede, non funziona. Deve vedersi in una schermata.
- **Il tono da professore.** Il pubblico che ci interessa ha mollato *anche* per quello.
- **Spiegare al lettore il problema che ha già.** Vedi regola 9. Ogni riga che comincia con "oggi la politica è..." va cancellata.
- **Le fonti nascoste dietro un link "approfondisci".** La fonte è la garanzia: deve stare attaccata al fatto, sempre.
- **Il pubblico "giornalisti e ricercatori".** È il pubblico che ha già tutto e non serve. È anche l'errore che c'è dentro i documenti attuali in `docs/`, che vanno rifatti.
- **Basare i soldi sugli abbonamenti dei lettori.** Il 69% dice che nessuna offerta lo convincerebbe. Il piano economico in `docs/08-monetizzazione.md` è costruito su un'ipotesi che i dati non reggono.

---

## 9. Conclusione

Lo studio dice tre cose:

1. **Il pubblico c'è, ed è enorme.** Milioni di persone che hanno smesso di votare e di informarsi, e che nessuno sta servendo — perché tutti gli parlano come se stessero ancora seguendo.
2. **Il tuo vincolo — non dire mai la conclusione — non è un limite: è la soluzione.** È l'unica configurazione che sopravvive all'effetto media ostile, ed è esattamente ciò che ha reso il Wahl-O-Mat un fenomeno di massa. Chi emette verdetti si sceglie una metà del paese. Chi fa dedurre se le tiene tutte e due.
3. **La materia prima è già pubblica, gratis e gigantesca.** Il lavoro non è trovare i fatti. È renderli attraversabili in venti secondi da uno che non ne vuole sapere niente.

Il punto in cui il progetto vive o muore non è la raccolta dati. È il **formato**.

---

## 10. Cosa serve decidere (da te, non da me)

Nessuna di queste è decisa. Le lascio come sono.

1. **Il formato da cui partire.** La mia lettura dello studio dice B (il quiz "chi l'ha detto"): è l'unico che soddisfa insieme apolitico e divertente, ed è il più rapido da mettere in piedi.
2. **Che fine fanno i 15 documenti in `docs/`.** Sono tarati sul pubblico sbagliato. O si buttano, o si tiene solo il metodo e si riscrive il resto.
3. **Se lo studio è quello che intendevi.** Se "studio su tutto" per te voleva dire un'altra cosa, dimmelo e lo rifaccio nella direzione giusta.

---

## Fonti

**Astensione e sfiducia**
- Affluenza regionali 2025 e confronto con le precedenti — https://www.deputatipd.it/news/astensionismo-fornaro-crollo-affluenza-125-nelle-sei-regioni-2025
- Cause dichiarate dell'astensione, rappresentanza percepita — https://www.quotidiano.net/politica/astensionismo-diffuso-motivi-e8488l3i
- Astensionismo e referendum, analisi CISE-LUISS — https://cise.luiss.it/2025/05/13/democrazia-senza-elettori/
- ISTAT, "Fiducia nelle istituzioni del Paese — Anno 2024" — https://www.istat.it/comunicato-stampa/fiducia-nelle-istituzioni-del-paese-anno-2024/
- Sintesi dei dati ISTAT sulla fiducia — https://tg24.sky.it/cronaca/2025/10/08/fiducia-istituzioni-2024-istat

**Consumo di informazione**
- Digital News Report 2025, dati Italia — https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025
- Analisi dei dati italiani del DNR 2025 — https://www.agendadigitale.eu/mercati-digitali/digital-news-report-2025-litalia-si-informa-ma-non-ci-crede-piu/
- Dati su abbonamenti e disponibilità a pagare — https://www.newslinet.com/editoria-digital-news-report-2025-di-reuters-institute-italia-e-informazione-digitale-il-grande-disincanto-italiani-non-abituati-a-pagare/

**Efficacia dei fatti e percezione di parzialità**
- "The global effectiveness of fact-checking", PNAS — https://www.pnas.org/doi/10.1073/pnas.2104235118
- Credibilità percepita dei fact-checker e differenze individuali — https://journals.sagepub.com/doi/10.1177/00936502231206419
- Percezione delle entità di fact-checking — https://arxiv.org/pdf/2410.00866
- Asimmetrie ideologiche nella fiducia verso le fonti — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10371040/

**Formati che funzionano**
- Quiz politici e interesse per le notizie, Center for Media Engagement — https://mediaengagement.org/research/political-quizzes/
- "Playful approaches to news engagement" — https://journals.sagepub.com/doi/full/10.1177/1354856520923964
- Giochi e puzzle come motore di abitudine editoriale — https://www.twipemobile.com/how-publishers-use-gamification-and-puzzles-in-newspapers-to-drive-engagement/
- Voting Advice Applications, panoramica — https://en.wikipedia.org/wiki/Voting_advice_application
- VAA e intelligenza artificiale, ricerca 2024 — https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2024.1286893/full
- Polimeter, metodologia e risultati — https://www.polimeter.org/en/trudeau
- Analisi dei dati del Polimeter — https://policyoptions.irpp.org/2025/04/elections-promises/

**Chi c'è già in Italia**
- openparlamento — https://parlamento19.openpolis.it/
- Indicatori openpolis — https://parlamento19.openpolis.it/indicatori
- Voti chiave di Camera e Senato — https://parlamento19.openpolis.it/votazioni

**Dati pubblici disponibili**
- Portale open data ANAC — https://www.anticorruzione.it/en/-/portale-dei-dati-aperti-dell-autorita-nazionale-anticorruzione
- Annuncio del portale ANAC su dati.gov.it — https://www.dati.gov.it/notizie/open-data-sugli-appalti-pubblici-line-il-nuovo-portale-anac
- OpenCoesione, open data — https://opencoesione.gov.it/it/opendata/
- OpenCUP — https://open.gov.it/consultazione-terzo-nap/portale-opencup-anagrafe-nazionale-dei-progetti-dinvestimento-pubblico/
