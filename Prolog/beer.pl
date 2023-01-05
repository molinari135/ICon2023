:- dynamic(beer/2).
:- dynamic(brewery/2).
:- dynamic(style/2).

use_module(library(csv)).

% FATTI (DA CSV)
:-
    csv_read_file('Prolog/csv/beer_name.csv',Beer,[functor(beer),separator(0';)]),
    maplist(assert,Beer),
    csv_read_file('Prolog/csv/style_id.csv',StyleId,[functor(styleid),separator(0';)]),
    maplist(assert,StyleId),
    csv_read_file('Prolog/csv/beer_style.csv',Style,[functor(style),separator(0';)]),
    maplist(assert,Style),
    csv_read_file('Prolog/csv/beer_abv.csv',Abv,[functor(abv),separator(0';)]),
    maplist(assert,Abv),
    csv_read_file('Prolog/csv/style_mouthfeel.csv',MF,[functor(mouthfeel),separator(0';)]),
    maplist(assert,MF),
    csv_read_file('Prolog/csv/style_taste.csv',Taste,[functor(taste),separator(0';)]),
    maplist(assert,Taste),
    csv_read_file('Prolog/csv/style_flavour.csv',Flavour,[functor(flavour),separator(0';)]),
    maplist(assert,Flavour),
    csv_read_file('Prolog/csv/beer_review.csv',Review,[functor(review),separator(0';)]),
    maplist(assert,Review).

%ANNOTAZIONI
%Tutti i valori numerici vanno da 1 a 5
%Low = [1,2.5]
%Neutral = (2.5,3.5)
%High = [3.5,5]
%Il problema sta nel selezionare le birre con valori
%non per forza esclusivi, valutando anche OR

%REGOLE

what_idbeer(Beer_name):-
    beer(Beer_id, Beer_name),
    write("Beer Id:"),write(Beer_id).

what_beer(Beer_id):-
    beer(Beer_id,Beer_name),
    style(Beer_id,Style_name),
    write("Beer: "),write(Beer_name).

what_style(BeerStyle_id):-
    style(BeerStyle_id,Style_name),
    styleid(Style_id,Style_name),
    write("Style: "),write(Style_name).

has_style(Beer_id):-
    style(Beer_id,Style_name),
    styleid(Style_id,Style_name),
    write("Style Id: "),write(Style_id).

what_abv(Beer_name):-
    beer(A,Beer_name),
    abv(A,Abv_value),
    write("Abv: "),write(Abv_value).

what_mouthfeel(Beer_name):-
    beer(A,Beer_name),
    mouthfeel(A,Astringency_value,Body_value,Alcohol_value),
    write("Astringency: "),write(Astringency_value),nl,
    write("Body: "),write(Body_value),nl,
    write("Alcohol: "),write(Alcohol_value).

what_taste(Beer_name):-
    beer(A,Beer_name),
    taste(A,Sweet_value,Bitter_value,Sour_value,Salty_value),
    write("Sweet: "),write(Sweet_value),nl,
    write("Bitter: "),write(Bitter_value),nl,
    write("Sour: "),write(Sour_value),nl,
    write("Salty: "),write(Salty_value).

what_flavour(Beer_name):-
    beer(A,Beer_name),
    flavour(A,Fruits_value,Hoppy_values,Malty_values,Spices_value),
    write("Fruits: "),write(Fruits_value),nl,
    write("Hoppy: "),write(Hoppy_values),nl,
    write("Malty: "),write(Malty_values),nl,
    write("Spices: "),write(Spices_value).

what_review(Beer_name):-
    beer(A,Beer_name),
    review(A,Review_value),
    write("Review: "),write(Review_value).

% CLASSIFICAZIONE
% L'utente fornisce in input i suoi "gusti"
% e il sistema gli consiglia lo stile di birra
% che pi� si avvicina ad essi
max(X,Y,Max):-
    X >= Y, !,
    Max = X; Max = Y.

% Identifica lo stile dell'utente
identify_taste(Sweet_value,Bitter_value,Sour_value,Salty_value):-

    taste(A,Sweet,Bitter,Sour,Salty),

    Sweet is Sweet_value,
    Bitter is Bitter_value,
    Sour is Sour_value,
    Salty is Salty_value,

    beer(A,_Beer_name),
    style(A,Style_name),
    write("Recommended style: "),write(Style_name),nl.

identify_mouthfeel(Astringency_value,Body_value,Alcohol_value):-

    mouthfeel(A,Astringency,Body,Alcohol),

    Astringency > Astringency_value,
    Body > Body_value,
    Alcohol > Alcohol_value,

    beer(A,_Beer_name),
    style(A,Style_name),
    write("Recommended style: "),write(Style_name),nl.

identify_flavour(Fruity_value,Hoppy_value,Malty_value,Spices_value):-

    flavour(A,Fruity,Hoppy,Malty,Spices),

    Fruity > Fruity_value,
    Hoppy > Hoppy_value,
    Malty > Malty_value,
    Spices > Spices_value,

    beer(A,_Beer_name),
    style(A,Style_name),
    write("Recommended style: "),write(Style_name),nl.

identify_user(A,B,C,D,E,F,G,H,J,K,L):-
    identify_flavour(A,B,C,D),
    identify_mouthfeel(E,F,G),
    identify_flavour(H,J,K,L).
