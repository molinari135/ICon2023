from pyswip import Prolog

prolog = Prolog()

prolog.consult('c:/Users/Ester/Documents/GitHub/ICon2023/Prolog/beer.pl')

# mette tutte le birre della kb in una lista
def getStyles():
    styles = list(prolog.query("style(A,B)"))
    return styles

# stampa la lista di birre
def printBeers(beers):
    print("\nList of beers:")
    for elem in beers:
        queryBeers = "> " + elem + ""
        print(queryBeers)