from pyswip import Prolog

prolog = Prolog()

def start():
    prolog.consult('c:/Users/Ester/Documents/GitHub/ICon2023/Prolog/beer.pl')
    prolog.query("import")

# mette tutte le birre della kb in una lista
def getBeers():
    #beers = list(prolog.query("beer(A,B)"))
    beers = prolog.query('beer(_,"Amber").')
    return beers

# stampa la lista di birre
def printBeers(beers):
    print("\nList of beers:")
    for elem in beers:
        queryBeers = "> " + elem + ""
        print(queryBeers)