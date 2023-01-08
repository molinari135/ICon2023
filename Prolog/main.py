import prolog as pl
import menu as m

if __name__ == "__main__":

    m.menu()
    
    styles = pl.getStyles()
    beers = pl.getBeers()
    beerstyle = pl.getBeerStyle()

    taste = pl.userTaste(1,2,1,1)
    flavour = pl.userFlavour(1,3,2,1)

    print(flavour[0]['Style'])