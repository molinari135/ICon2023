# [ICon] Consigliatore di Birre

### Gruppo di lavoro
- [Ester Molinari](https://github.com/burraco135), 716555
- [Giacomo Signorile](https://github.com/GiacomoSignorile), 704897

###### AA 2022-2023

## Introduzione
> Paragrafo sul dominio di interesse

Inizialmente, il dominio di interesse del KBS era basato su un dataset di [1.5 milioni di recensioni di birre](https://www.kaggle.com/datasets/rdoume/beerreviews) per poi essere sostituito da un dataset basato su [profili e valutazioni di birre](https://www.kaggle.com/datasets/ruthgn/beer-profile-and-ratings-data-set), che sfrutta i dati del dataset precedente e un dataset che analizza le [parole contenute nelle recensioni di birre](https://www.kaggle.com/datasets/stephenpolozoff/top-beer-information). Tutti i dataset raccolgono i dati forniti dal sito [BeerAdvocate](https://www.beeradvocate.com/). Durante la fase di progettazione abbiamo sfruttato l'organizzazione dei dati per realizzare i facts della KB a cui abbiamo aggiunto le features del secondo dataset, utilizzato a tutti gli effetti.

---

## Sommario
> Paragrafo sul KBS e su come integri moduli che dimostrino competenze sui diversi argomenti (specificati sotto)

## Elenco argomenti di interesse
- [Preprocessing e regressione](#preprocessing-e-regressione)
- [Apprendimento Supervisionato](#apprendimento-supervisionato)
- [Sistema Basato su Conoscenza](#sistema-basato-su-conoscenza)

## Preprocessing e regressione

### Sommario
> Un paragrafo che chiarisca la rappresentazione della conoscenza scelta per la KB (modelli di ragionamento/apprendimento), dati, BK, ...

```prolog
% inserire alcune immagini (heatmap) con spiegazione delle operazioni effettuate prima di passare all'apprendimento supervisionato
```

### Strumenti utilizzati
> Breve: non serve spiegare come funzionano se implementano modelli ben noti (basta indicare dei riferimenti bibliografici)
Dilungarsi solo su eventuali modelli/algoritmi originali ideati dal gruppo.

```prolog
% inserire le funzioni utilizzate in pandas per fare la manipolazione dei dati
```

### Decisioni di Progetto
> Configurazione dei componenti (e.g. API/librerie) utilizzati, ad es. parametri, soglie, ecc. e di eventuali metodi specifici utilizzati a tale scopo.

```prolog
% spiegare il perché delle eliminazioni delle colonne, l'utilità delle librerie, l'arrotondamento dei valori
```

### Valutazione
> Paragrafi che richiamino (non spieghino, se standard) le metriche adottate + tabelle sui risultati e loro discussione.

```prolog
% inserire le immagini del prima e dopo manipolazione
```

[Torna su](#elenco-argomenti-di-interesse)

## Apprendimento Supervisionato

### Sommario
> Un paragrafo che chiarisca la rappresentazione della conoscenza scelta per la KB (modelli di ragionamento/apprendimento), dati, BK, ...

```prolog
% spiegare quali modelli di apprendimento sono stati usati
```

### Strumenti utilizzati
> Breve: non serve spiegare come funzionano se implementano modelli ben noti (basta indicare dei riferimenti bibliografici)
Dilungarsi solo su eventuali modelli/algoritmi originali ideati dal gruppo.

```prolog
% inserire le funzioni usate per fare i calcoli
```

### Decisioni di Progetto
> Configurazione dei componenti (e.g. API/librerie) utilizzati, ad es. parametri, soglie, ecc. e di eventuali metodi specifici utilizzati a tale scopo.

```prolog
% spiegare il motivo per cui abbiamo unificato i dati per stile e non li abbiamo più considerati come singole birre (facendo apprendimento abbiamo visto che i falsi negativi e i veri positivi corrispondevano alle informazioni del csv quindi abbiamo lavorato solo sugli stili e le medie dei loro valori)
```

### Valutazione
> Paragrafi che richiamino (non spieghino, se standard) le metriche adottate + tabelle sui risultati e loro discussione.

```prolog
% qui spiegare quanto hanno funzionato gli algoritmi
```

[Torna su](#elenco-argomenti-di-interesse)

## Sistema Basato su Conoscenza

### Sommario
> Un paragrafo che chiarisca la rappresentazione della conoscenza scelta per la KB (modelli di ragionamento/apprendimento), dati, BK, ...

1. [Fatti](#fatti)
2. [Regole](#regole)
3. [Apprendimento](#apprendimento)

---

#### 1. Fatti
Il nostro KBS si basa su una **ontologia** realizzata dall'interpretazione dei dati inseriti da alcuni esperti del dominio che vengono memorizzati sottoforma di **database di fatti** con le loro **regole generali** nel Sistema di learning. Mediante una **interfaccia utente**, l'utente può comunicare con il Motore Inferenziale per inserire i propri "gusti" e ricevere lo stile associato come risposta. Ogni risposta verrà sfruttata dal KBS per imparare le preferenze di utenti simili. I dati nella KB vengono sottoposti ad **Apprendimento Supervisionato** prima di essere inseriti e presentano regole derivate dai risultati dell'**Apprendimento probabilistico** applicato su di essi.

Il nostro dataset `beer_profile_and_ratings.csv` presenta numerose feature non normalizzate o con valori nulli, quindi prima di popolare la KB abbiamo applicato regressione e classificazione lineare per ottenere dei valori utilizzabili dalle regole del KBS. Dopo aver corretto il dataset, abbiamo effettuato una operazione di divisione del dominio in sotto-domini che permettono di ottenere relazioni di sottoinsiemi interrogabili tramite regole Prolog.

La directory `csv` è strutturata nel seguente modo:

```c
|-- csv
|   |-- beer_abv.csv            // Colonne: beer_id,abv_value
|   |-- beer_brewery.csv        // Colonne: beer_id,brewery_name
|   |-- beer_flavour.csv        // Colonne: beer_id,fruits,hoppy,malty,spices
|   |-- beer_mouthfeel.csv      // Colonne: beer_id,astringency,body,alcohol
|   |-- beer_name.csv           // Colonne: beer_id,beer_name
|   |-- beer_review.csv         // Colonne: beer_id,review_overall
|   |-- beer_style.csv          // Colonne: beer_id,style_name
|   |-- beer_taste.csv          // Colonne: beer_id,sweet,bitter,sour,salty
|   |-- style_flavour.csv       // Colonne: style_id,fruits,hoppy,malty,spices
|   |-- style_id.csv            // Colonne: style_id,style_name
|   |-- style_mouthfeel.csv     // Colonne: style_id,astringency,body,alcohol
|   |-- style_taste.csv         // Colonne: style_id,sweet,bitter,sour,salty
```

Tutti questi file servono per popolare la KB e realizzare i fatti con `functor(nome)`, ad esempio, caricando `beer_abv.csv` nella KB si otterrà il fatto `abv(Beer_id,Abv_value)`.

#### 2. Regole
Il KBS presenta numerose regole per ottenere qualsiasi tipo di informazione dalla KB. Queste si possono dividere in:

- N° 8 regole basate su fatti relativi alle birre (`Beer_id`)
- N° 5 Regole basate su fatti relativi agli stili (`Style_id`)

Con un totale di 13 regole che vengono successivamente utilizzate nella fase di apprendimento/classificazione.

```prolog
% Regole basate su fatti relativi alle birre
what_beer_id(Beer_name) :- ... write(Beer_id).
what_beer_name(Beer_id) :- ... write(Beer_name).
what_beer_abv(Beer_name) :- ... write(Abv_value).
what_beer_style(Beer_name) :- ... write(Style_name).
what_beer_review(Beer_name) :- ... write(Review_overall).

what_beer_mouthfeel(Beer_name) :- ... write("Astringency: ") ...
what_beer_taste(Beer_name) :- ... write("Sweet: ") ...
what_beer_flavour(Beer_name) :- ... write("Fruits: ") ...

% Regole basate su fatti relativi agli stili
what_style_id(Style_name) :- ... write(Style_id).
what_style_name(Style_id) :- ... write(Style_name).

what_style_mouthfeel(Style_name)  :- ... write("Astringency: ") ...
what_style_taste(Style_name) :- ... write("Sweet: ") ...
what_style_flavour(Style_name) :- ... write("Fruits: ") ...
```

#### 3. Apprendimento
Il KBS, basandosi sui gusti dell'utente, cerca di identificare (classificare) lo stile a cui appartengono per poi proporre le birre con la valutazione maggiore per quello stile.
L'identificazione avviene in 3 step, uno per ogni qualità della birra per poi essere combinate in un'unica operazione che può quindi portare ad un minimo di 0 soluzioni (se non esiste uno stile con quelle caratteristiche) e ad un massimo di 3 soluzioni diverse.

In realtà si potrebbe valutare l'utilizzo di assert per ogni inserimento da parte dell'utente...

```prolog
% Apprendimento del gusto
identify_taste(Sweet,Bitter,Sour,Salty) :- ... write(Style_name).

% Apprendimento della sensazione del gusto
identify_mouthfeel(Astringency,Body,Alcohol) :- write(Style_name).

% Apprendimento del sapore
identify_flavour(Fruity,Hoppy,Malty,Spices) :- write(Style_name).

% Apprendimento delle preferenze dell'utente
identify_user(Sweet,Bitter,Sour,Salty,
                Astringency,Body,Alcohol,
                Fruity,Hoppy,Malty,Spices) :- write(Style_name).
```

### Strumenti utilizzati
> Breve: non serve spiegare come funzionano se implementano modelli ben noti (basta indicare dei riferimenti bibliografici)

La parte che si occupa di trovare lo stile corrispondente ai gusti dell'utente, realizzata in Prolog, applica dei principi del **KNN** e del **Naive Bayes**.

Per realizzarlo in Prolog, abbiamo creato una regola particolare:

```prolog
% Inserire la regola che trova lo stile
```

### Decisioni di Progetto
> Configurazione dei componenti (e.g. API/librerie) utilizzati, ad es. parametri, soglie, ecc. e di eventuali metodi specifici utilizzati a tale scopo.

Durante la fase di progettazione della KB avevamo proposto due tipi di rappresentazione dei fatti mediante proposizioni:

```prolog
% rappresentazione standard
verbo(soggetto,oggetto).

% rappresentazione classe
proposizione(soggetto,verbo,oggetto).
```

Abbiamo scelto di utilizzare la prima rappresentazione dopo aver consultato il dataset in formato `.csv`. Abbiamo sfruttato la funzione `csv_read_file()` di Prolog insieme alla funzione `maplist()` in modo da popolare la KB senza dover inserire i valori manualmente. Per ottenere delle proposizioni composte da `verbo(soggetto,oggetto)` abbiamo scomposto il `.csv` in file composti da 2 colonne, in modo da facilitare l'inserimento nella KB.

Abbiamo anche realizzato un'altra rappresentazione dei fatti per le caratteristiche della birra e dello stile:

```prolog
% rappresentazione caratteristiche
caratteristica(valore1,valore2,valore3)
caratteristica(valore1,valore2,valore3,valore4)
```

Questa rappresentazione è stata realizzata per soddisfare un criterio logico su cui si basa la valutazione delle birre e dei loro stili, in quanto le tre sezioni in questione sono indipendenti tra loro ma gli argomenti al loro interno sono strettamente legati.

### Valutazione
> Paragrafi che richiamino (non spieghino, se standard) le metriche adottate + tabelle sui risultati e loro discussione.

```prolog
% Inserire immagini dei grafici dei dati prima e dopo l'unificazione degli stili
```


[Torna su](#elenco-argomenti-di-interesse)

## Conclusioni
> Un paragrafo che delinei anche possibili sviluppi (per altri gruppi)

## Riferimenti Bibliografici
[1] ...

[2] ...

[3] ...

[Torna su](#elenco-argomenti-di-interesse)
