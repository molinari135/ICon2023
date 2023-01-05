from pyswip import Prolog

prolog = Prolog()
prolog.consult("beer.pl")

# mette tutte le birre della kb in una lista
def getBeers():
    myQuery = "beer(A,_)"
    beers = list(prolog.query(myQuery))
    return beers

# stampa la lista di birre
def printBeers(beers):
    print("\nList of beers:")
    for elem in beers:
        queryBeers = "> " +elem["Beer_name"]+""
        print(queryBeers)