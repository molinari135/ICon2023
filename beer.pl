use_module(library(csv)).

import:-
    csv_read_file('csv/beer_name.csv',Beer,[functor(beer),separator(0';)]),
    maplist(assert,Beer),
    csv_read_file('csv/beer_brewery.csv',Brewery,[functor(brewery),separator(0';)]),
    maplist(assert,Brewery),
    csv_read_file('csv/beer_style.csv',Style,[functor(style),separator(0';)]),
    maplist(assert,Style),
    csv_read_file('csv/beer_abv.csv',Abv,[functor(abv),separator(0';)]),
    maplist(assert,Abv),
    csv_read_file('csv/beer_mouthfeel.csv',MF,[functor(mouthfeel),separator(0';)]),
    maplist(assert,MF),
    csv_read_file('csv/beer_taste.csv',Taste,[functor(taste),separator(0';)]),
    maplist(assert,Taste),
    csv_read_file('csv/beer_flavour.csv',Flavour,[functor(flavour),separator(0';)]),
    maplist(assert,Flavour),
    csv_read_file('csv/beer_review.csv',Review,[functor(review),separator(0';)]),
    maplist(assert,Review).

%RULES
what_brewery(Beer_name):-
    beer(A,Beer_name),
    brewery(A,Brewery_name),
    write("Brewery: "),write(Brewery_name).

what_beer(Brewery_name):-
    brewery(A,Brewery_name),
    beer(A,Beer_name),
    write("Beer: "),write(Beer_name).

what_style(Beer_name):-
    beer(A,Beer_name),
    style(A,Style_name),
    write("Style: "),write(Style_name).

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
