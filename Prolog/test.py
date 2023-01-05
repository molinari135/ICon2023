from pyswip import Prolog

p = Prolog()

p.consult('Prolog/beer.pl')
#p.query('import')

myQuery = "beer(_,X)."
l = list(p.query(myQuery))

for beer[X] in l:
    print(beer[X])
