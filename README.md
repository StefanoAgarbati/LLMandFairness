# LLM and Fairness
<br/>

## Introduzione
Scopo di questo progetto è quello di provare ad automatizzare, con l'ausilio di un LLM (large language model), alcuni dei passi compiuti da un data scientist nel processo di analisi di un insieme di dati.
Quando si opera nel campo delle scienze sociali, una delle prime cose che un analista cerca di capire, è se l'insieme di dati di cui dispone mostra dei difetti, delle distorsioni che possano portare
a fenomeni di bias edd unfaireness nelle fasi successive del processo di analisi.
Questa prima fase di ricerca viene svolta, di norma, manualmente e richiede:
* la capacità, di natura tecnica, del saper gestire, manipolare i dati presenti in un dataset
* la conoscenza del contesto applicativo per capire come selezionare le caratteristiche e le variabili target (ad es. se si operasse nel campo bancario l'analista dovrebbe conoscere i concetti e 
  processi utilizzati dalle persone che operano in tale campo come mutuo, reddito ecc..... se volesse definire un modello che consenta di decidere se assegnare o meno un mutuo ad un determinato soggetto) 
* un po' di buonsenso (comunque soggettivo).
Ogni problema da risolvere è inquadrabile in uno specifico contesto. La questione del contesto è importante perché alcuni attributi possono essere considerati biased in certi contesti e non biased
in altri rendendo difficoltoso il processo di automatione del processo di analisi: una macchina così com'è, non è in grado di capire questa cosa.
L'utilizzo di un LLM addestrato consente, in qualche modo, di affrontare questa questione del contesto e fornire supporto all'automazione del processo di analisi.

Quelli che seguono sono alcuni passi eseguiti da un data scientist durante l'analisi di un dataset:
* Individuazione delle caratteristiche sensibili relativamente al contesto
  * una caratteristica è detta sensibile quando è potenzialmente fonte di unfairenss, disparità (come ad es. l'etnia, l'orientamento sessuale, informazioni sanitarie.....)
* caratteristiche non presenti nel dataset ma che ci si aspetterebbe di trovare nello specifico conteste applicativo
* valori non considerati nelle caratteristiche presenti
  * come ad esempio il genere non binario per la caratteristica 'genere'
* identificazione di caratteristiche proxy, nicchie e disproporzioni presenti nei dati di cui si dispone
  * (**spiegare cosa si intende per proxy, nicchia e disproporzione e perché è importante la loro identificazione**)
* identificare la caratteristica target
  * cioè la caratteristica sulla quale il modello dovrà fare una previsione usando come input le altre caratteristiche del dataset
* individuare il modello di problema di learning più 'appropriato' per il problema in esame
  * capire se è più 'consono' trattare il problema come problema di classificazione o regressione o clustering o ranking .....
L'obiettivo principale del progetto è quello di riuscire ad automatizzare, attraverso il supporto di un LLM, almeno i punti descritti precedentemente.

## Tecnologie
***In questa sezione il tirocinante elenca e commenta brevemente le
tecnologie utilizzate (linguaggi, piattaforme, sistemi operativi, ecc.)***
Nello sviluppo del progetto software sono state utilizzate diverse tecnologie.
### Linguaggio di programmazione Python
Il codice è stato realizzato interamente in linguaggio python. Si tratta di un liguaggio interpretato e di tipo dinamico (non è necessario dichiarare il tipo delle variabili come in js)
E' uno dei linguaggi più utilizzati nel campo dell'inteligenza artificiale poiché supportato da un'ampia gamma di librerie e framework
### Libreria Pandas
Per la parte legata alla manipolazione e gestione dei dati è stata utiilzzata la libreria Pandas. Questa fornisce strutture dati adatte a modellare insiemi di dati ed operazioni 
per la loro manipolazione e selezione.
### Framework LangChain
LancgChain è un framework che fornisce supporto allo sviluppo di applicazioni che fanno uso di LLM (large language model). Fornisce un'iterfaccia uniforme verso le diverse api fornite dai
diversi vendor è produttori di LLM. Implementa omogeneità al di sopra dell'eterogeità derivante dalle diverse api
### Libreria Scikit-learn
Scikit-learn è una libreria python di supporto allo sviluppo di applicazioni che utilizzano il machine learning.
### Libreria Seaborn
Seaborn è una libreria python che fornisce funzioni per la visualizzazione di dati statistici come istogrammi, heatmap, diagrammi di dispersione.......
### Jupyter Lab


## Attività
***Questa sezione, eventualmente frazionata in sottosezioni, è quella
centrale e più corposa dell’elaborato e deve illustrare (dal punto di vista tecnico, non
necessariamente cronologico) le attività svolte durante il tirocinio. A eccezione di
eventuali esempi, non deve includere il codice sviluppato; per descrivere algoritmi si
usino piuttosto pseudo-codice e/o diagrammi di vario tipo. Per lavori di tipo progettuale
è utile includere una sintetica documentazione formale di progetto***
#### Requisiti del software
Scopo del progetto software è quello di cercare di automatizzare il più possibile certe azioni che un data scientist esegue durante il processo di analisi di un dataset.  
Alcune di queste azioni sono state descritte nella sezione [Introduzione](#introduzione) di questo documento:
* Indentificazione delle caratteristiche sensibili relativamente al contesto
  * una caratteristica è detta sensibile quando è potenzialmente fonte di unfairenss, disparità (come ad es. l'etnia, l'orientamento sessuale, informazioni sanitarie.....)
* identificazione di caratteristiche non presenti nel dataset ma che ci si aspetterebbe di trovare nello specifico contesto applicativo
* identificazione di valori non considerati nelle caratteristiche presenti
  * come ad esempio il genere non binario per la caratteristica 'genere'
* identificazione di caratteristiche proxy, nicchie e disproporzioni presenti nei dati di cui si dispone
* identificazione della caratteristica target
  * cioè la caratteristica sulla quale il modello dovrà fare una previsione usando come input le altre caratteristiche del dataset
* identificazione del modello di problema di learning più 'appropriato' per il problema in esame
  * capire se è più 'consono' trattare il problema come problema di classificazione o regressione o clustering o ranking .....

Si richiede che il software da sviluppare, per poter soddisfare tali requisiti, faccia uso di un LLM come supporto all'attività di analisi  
#### Analisi dei requisiti
L'artefatto software deve:  
* inviare richieste ad un LLM
* ricevere ed elaborare risposte ricevute da un LLM
* visualizzare le richieste inoltrare all'LLM e le risposte ricevute
* calcolare alcune metriche statistiche relative alle caratteristiche
* visualizzare le metriche statistiche attraverso grafici
* caricare un dataset
* effettuare operazioni di data cleaning sul dataset
* * trasformare il dataset in forma numerica per l'addestramento di modelli di ML
* fornire informazioni relative ad eventuali sbilanciamenti presenti nei dati
* fornire informazioni relative a valori non non considerati nelle caratteristiche
* fornire informazioni relative a caratteristiche non presenti nel dataset ma che potrebbero essere importanti nello specifico contesto
* fornire informazioni in merito alla presenza di caratteristiche proxy
* fornire informazioni su quale potrebbe essere la caratteristica target in relazione al contesto
* fornire informazioni relative alla tipologia di problema di learning più adatta alla risoluzione del problema (classificazione, regressione ....)
* fornire informazioni relative al modello di machine learning più appropriato in relazione ai risultati di performance ottenuti testando alcuni modelli disponibili
* preparare il dataset suddividendolo in un insieme per il testing e un insieme per il training di un modello
* addestramento del modello più appropriato e relativa previsione del target
* fornire informazioni relative alla analisi delle prestazioni del modello

#### Analisi del problema
L'applicazione invia ad un LLM una sequenza di messaggi predeterminati e definiti dall'utente. I messaggi sono memorizzati all'interno di una base dati. Essi vengono inviati all'LLM una alla volta  
seguendo un'interazione di tipo request-response sincrona. Successivamente all'invio di un messaggio l'LLM può rispondere con un semplice messaggio testuale il quale verrà semplicemente visualizzato  
all'utente attraverso un dispositivo di output oppure può rispondere attraverso un messaggio che richiede l'esecuzione di un tool. In quest'ultimo caso il messaggio contiene i parametri da passare al  
tool che deve essere eseguito. Il tool viene eseguito localmente ma i parametri vengono generati dall'LLM in base al messaggio di richiesta che esso ha ricevuto. L'esecuzione di un tool porta ad un  
risultato parte del quale viene usato per arricchire la memoria dell'LLM. Infatti sorge il problema della memoria che può essere risolto passando, ad ogni richiesta fatta all'LLM,  
tutti i messaggi inviati e ricevuti fino a quel momento. L'esecuzione di un tool porterà all'innesco di una specifica logica applicativa.  
La descrizione a parole di cui sopra può essere espressa anche attraverso un disegno che mostra l'architettura generale del sistema software




## Conclusioni
***In questa parte lo studente trae le conclusioni del lavoro svolto,
valutando pregi e difetti dell’esperienza e, più specificamente, riassumendo quanto
appreso.***

## Bibliografia
***Questa sezione, opzionale, include i riferimenti a manuali, testi e
articoli scientifici eventualmente consultati durante il lavoro, ordinati per cognome del
primo autore***
