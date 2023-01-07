:- dynamic(beer/2).
:- dynamic(brewery/2).
:- dynamic(style/2).

use_module(library(csv)).

% -------------------- CSV -------------------- %
:-
    % inizializzazione fatti
    retractall(beer(X, Y)),
    retractall(style(X, Y)),
    retractall(beerstyle(X,Y)),
    retractall(abv(X,Y)),
    retractall(mouthfeel(A,B,C,D)),
    retractall(taste(A,B,C,D,E)),
    retractall(flavour(A,B,C,D,E)),
    retractall(review(X,Y)),
    retractall(dist_flavour(X,Y)),
    retractall(dist_mouthfeel(X,Y)),
    retractall(dist_taste(X,Y)),

    % importazione fatti
    csv_read_file('csv/beer_name.csv', Beer, [functor(beer), separator(0';)]),
    maplist(assert, Beer),
    csv_read_file('csv/style_id.csv', Style, [functor(style), separator(0';)]),
    maplist(assert, Style),
    csv_read_file('csv/beer_style.csv', BeerStyle, [functor(beerstyle), separator(0';)]),
    maplist(assert, BeerStyle),
    csv_read_file('csv/beer_abv.csv', Abv, [functor(abv), separator(0';)]),
    maplist(assert, Abv),
    csv_read_file('csv/style_mouthfeel.csv', MF, [functor(mouthfeel), separator(0';)]),
    maplist(assert, MF),
    csv_read_file('csv/style_taste.csv', Taste, [functor(taste), separator(0';)]),
    maplist(assert, Taste),
    csv_read_file('csv/style_flavour.csv', Flavour, [functor(flavour), separator(0';)]),
    maplist(assert, Flavour),
    csv_read_file('csv/beer_review.csv', Review, [functor(review), separator(0';)]),
    maplist(assert, Review).

% -------------------- FATTI -------------------- %
% beer(Beer_id, Beer_name).
% style(Style_id, Style_name).
% beerstyle(Beer_id, Style_id).
% abv(Beer_id, Abv_value).

% mouthfeel(Style_id, Astringency_value, Body_value, Alcohol_value).
% taste(Style_id, Sweet_value, Bitter_value, Sour_value, Salty_value).
% flavour(Style_id, Fruits_value, Hoppy_value, Malty_value, Spices_value).

% -------------------- REGOLE -------------------- %

% Regole basate su fatti relativi alle birre
what_beer_id(Beer_name) :-
    beer(Beer_id, Beer_name),

    write(Beer_id).

what_beer_name(Beer_id) :-
    beer(Beer_id, Beer_name),

    write(Beer_name).

what_beer_abv(Beer_name) :-
    beer(A, Beer_name),
    abv(A, Abv_value),

    write(Abv_value).

what_beer_style(Beer_name) :-
    beer(A, Beer_name),
    beerstyle(A, Style_name),

    write(Style_name).

what_beer_review(Beer_name) :-
    beer(A, Beer_name),
    review(A, Review_value),

    write(Review_value).


what_beer_mouthfeel(Beer_name) :-
    beer(A, Beer_name),
    beerstyle(A, Style_name),
    style(B, Style_name),

    mouthfeel(B, Astringency_value, Body_value, Alcohol_value),

    write(Astringency_value), nl,
    write(Body_value), nl,
    write(Alcohol_value).

what_beer_taste(Beer_name) :-
    beer(A, Beer_name),
    beerstyle(A, Style_name),
    style(B, Style_name),

    taste(B, Sweet_value, Bitter_value, Sour_value, Salty_value),

    write(Sweet_value), nl,
    write(Bitter_value), nl,
    write(Sour_value), nl,
    write(Salty_value).

what_beer_flavour(Beer_name) :-
    beer(A, Beer_name),
    beerstyle(A,Style_name),
    style(B, Style_name),

    flavour(B, Fruits_value, Hoppy_value, Malty_value, Spices_value),

    write(Fruits_value), nl,
    write(Hoppy_value), nl,
    write(Malty_value), nl,
    write(Spices_value).

% Regole basate su fatti relativi agli stili
what_style_id(Style_name) :-
    style(Style_id, Style_name),

    write(Style_id).

what_style_name(Style_id) :-
    style(Style_id, Style_name),

    write(Style_name).

what_style_mouthfeel(Style_name) :-
    style(A, Style_name),

    mouthfeel(A, Astringency_value, Body_value, Alcohol_value),

    write(Astringency_value), nl,
    write(Body_value), nl,
    write(Alcohol_value).

what_style_taste(Style_name) :-
    style(A, Style_name),

    taste(A, Sweet_value, Bitter_value, Sour_value, Salty_value),

    write(Sweet_value), nl,
    write(Bitter_value), nl,
    write(Sour_value), nl,
    write(Salty_value).

what_style_flavour(Style_name) :-
    style(A, Style_name),

    flavour(A, Fruits_value, Hoppy_value, Malty_value, Spices_value),

    write(Fruits_value), nl,
    write(Hoppy_value), nl,
    write(Malty_value), nl,
    write(Spices_value).

% -------------------- APPRENDIMENTO -------------------- %
% L'utente fornisce in input i suoi "gusti"
% e il sistema gli consiglia lo stile di birra
% che pi� si avvicina ad essi

% Apprendimento del gusto
identify_taste(Sweet_input, Bitter_input, Sour_input, Salty_input) :-
    taste(A, Sweet_value, Bitter_value, Sour_value, Salty_value),

    % implementare knn
    Sweet_value >= Sweet_input,
    Bitter_value >= Bitter_input,
    Sour_value >= Sour_input,
    Salty_value >= Salty_input,

    style(A, Style_name),
    write(Style_name).

% Apprendimento della sensazione al palato
identify_mouthfeel(Astringency_input, Body_input, Alcohol_input) :-
    mouthfeel(A, Astringency_value, Body_value, Alcohol_value),

    % implementare knn
    Astringency_value >= Astringency_input,
    Body_value >= Body_input,
    Alcohol_value >= Alcohol_input,

    style(A, Style_name),
    write(Style_name).

% Apprendimento del sapore
identify_flavour(Fruity_input, Hoppy_input, Malty_input, Spices_input) :-
    flavour(A, Fruity_value, Hoppy_value, Malty_value, Spices_value),

    % implementare knn
    Fruity_value >= Fruity_input,
    Hoppy_value >= Hoppy_input,
    Malty_value >= Malty_input,
    Spices_value >= Spices_input,

    style(A, Style_name),
    write(Style_name).

% Apprendimento delle preferenze dell'utente
identify_user(Sweet_input, Bitter_input, Sour_input, Salty_input,
                Astringency_input, Body_input, Alcohol_input,
                    Fruity_input, Hoppy_input, Malty_input, Spices_input) :-

    identify_taste(Sweet_input, Bitter_input, Sour_input, Salty_input),
    identify_mouthfeel(Astringency_input, Body_input, Alcohol_input),
    identify_flavour(Fruity_input, Hoppy_input, Malty_input, Spices_input).

% Test KNN (K = 2)
% Calcolo la distanza euclidea tra due valori della stessa valutazione
% lo ripeto per tutte le valutazioni e per tutti gli stili presenti nella KB
% memorizzando tutti i valori in una lista.
% Cerco il valore minore della lista, risalgo alla sua posizione e stampo il risultato
% Alternativa: memorizzo codice stile e valore minore

diff(X,Y,Z) :- Z is abs(X-Y).

%min(X,Y,Min) :- X =< Y, !, Min = X; Min = Y.

min_dist(Data) :-
    aggregate(min(X,Y), list_mouthfeel(X,Y), min(_,Data)),
    order_by([asc(Y)], list_mouthfeel(X,Y)).

% 1. Prende in input le 3 valutazioni
% 2. Prende un fatto dalla KB e ne prende le valutazioni
% 3. Calcola la distanza euclidea tra le due valutazioni
% 4. Memorizza Style_id e distanza euclidea in data
dist_style_mouthfeel(Astringency_input, Body_input, Alcohol_input) :-

    retractall(dist_mouthfeel(_X,_Y)),

    mouthfeel(A, Astringency_value, Body_value, Alcohol_value),

    diff(Astringency_input, Astringency_value, Ast),
    diff(Body_input, Body_value, Bod),
    diff(Alcohol_input, Alcohol_value, Alc),

    sqrt(((Ast*Ast)+(Bod*Bod)), S1),
    %sqrt(((S1*S1)+(Alc*Alc)), S),
    S is (S1+Alc),

    assert(dist_mouthfeel(A, S)).
% alla fine della procedura, va effettuato retract(list_mouthfeel)
% per rimuovere il fatto dell'utente

dist_style_taste(Sweet_input, Bitter_input, Sour_input, Salty_input) :-

    retractall(dist_taste(_X,_Y)),

    taste(A, Sweet_value, Bitter_value, Sour_value, Salty_value),

    diff(Sweet_input, Sweet_value, Swe),
    diff(Bitter_input, Bitter_value, Bit),
    diff(Sour_input, Sour_value, Sou),
    diff(Salty_input, Salty_value, Sal),

    sqrt(((Swe*Swe)+(Bit*Bit)), S1),
    sqrt(((Sou*Sou)+(Sal*Sal)), S2),
    S is (S1+S2),

    assert(dist_taste(A, S)).

dist_style_flavour(Fruity_input, Hoppy_input, Malty_input, Spices_input) :-

    retractall(dist_flavour(_X,_Y)),

    flavour(A, Fruity_value, Hoppy_value, Malty_value, Spices_value),

    diff(Fruity_input, Fruity_value, Fru),
    diff(Hoppy_input, Hoppy_value, Hop),
    diff(Malty_input, Malty_value, Mal),
    diff(Spices_input, Spices_value, Spi),

    sqrt(((Fru*Fru)+(Hop*Hop)), S1),
    sqrt(((Mal*Mal)+(Spi*Spi)), S2),
    S is (S1+S2),

    assert(dist_flavour(A, S)).
