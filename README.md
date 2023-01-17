# BeerSpotter
> Consigliatore di birre in Prolog con interfaccia CLI in Python

### Gruppo di lavoro
- [Ester Molinari](https://github.com/burraco135), 716555
- [Giacomo Signorile](https://github.com/GiacomoSignorile), 704897

###### AA 2022-2023

## Istruzioni
Si consiglia di scaricare il file zip del programma ed estrarlo nella cartella di lavoro di SWI Prolog per evitare conflitti con le directory dei files.
Per avviare il programma, posizionarsi nella cartella con main.py ed aprire nel terminale, digitare `python main.py` per iniziare.
Bisogna inoltre lanciare il comando per installare PySwip:

`python -m pip install git+https://github.com/yuce/pyswip@master#egg=pyswip`

## Introduzione
|Notebook|Link|
|---|---|
|Documentazione|[pdf](https://github.com/burraco135/ICon2023/blob/master/Documentazione/BeerSpotter%20-%20Molinari%2C%20Signorile.pdf)|
|Notebook Colab|[link](https://github.com/burraco135/ICon2023/blob/master/Documentazione/BeerClassification.ipynb)|
|Notebook SWISH|[web](https://swish.swi-prolog.org/p/[ICon2023]%20BeerSpotter.swinb) - [pdf](https://github.com/burraco135/ICon2023/blob/master/Documentazione/SWISHBeerSpotter.pdf)|

Il dominio di interesse che abbiamo scelto si basa su un dataset di profili e valutazioni di birre che sfrutta 1.5 milioni di recensioni di birre presenti sul sito BeerAdvocate.

I dati comprendono tre tipi di informazioni:

- **Qualità fisiche della birra** (in inglese, *mouthfeel*)

  - **Astringenza** (in inglese, *astringency*): deriva dai fenoli, in particolare dai polifenoli nella birra. Questi includono tannini che danno una sensazione di secco in bocca.
  - **Corposità** (in inglese, *body*): caratterizzata dalla pienezza del sapore e dalla sensazione al palato.
  - **Alcolicità** (in inglese, *alcohol*): deriva dalla concentrazione alcolica della birra.

- **Sapore della birra** (in inglese, *taste*)

  - **Amarezza** (in inglese, *bitter*): sapore amaro nella birra.
  - **Dolcezza** (in inglese, *sweet*): sapore dolce nella birra.
  - **Asprezza** (in inglese, *sour*): sapore aspro nella birra.
  - **Salinità** (in inglese, *salty*): sapore di salino nella birra.

- **Aromaticità della birra** (in inglese, *flavour*)

  - **Fruttata** (in inglese, *fruity*): la birra presenta note di frutta.
  - **Luppolata** (in inglese, *hoppy*): la birra presenta note di luppolo.
  - **Speziata** (in inglese, *spices*): la birra presenta note di spezie.
  - **Maltosa** (in inglese, *malty*): la birra presenta note di malto.

Il dataset contiene, per ogni caratteristica (feature) elencata sopra, il conteggio delle parole usate per recensire la birra, rispetto alle recensioni totali.
