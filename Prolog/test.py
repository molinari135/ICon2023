from pyswip import Prolog

p = Prolog()

p.consult('Prolog/beer.pl')
#p.query('import')

myQuery = "beer(_,X)."
l = list(p.query(myQuery))

p.listProp(l)

for beer in l:
    print(beer)
