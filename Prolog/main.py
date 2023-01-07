import prolog as pl

if __name__ == "__main__":
    styles = pl.getStyles()
    beers = pl.getBeers()
    beerstyle = pl.getBeerStyle()

    taste = pl.userTaste(1,2,1,1)

    for t in taste:
        print(t['Style'])