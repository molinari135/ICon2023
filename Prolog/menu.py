import prolog as pl

def menu():

    inside_menu = True

    while(inside_menu):
        print("\nWelcome!"
        +"\n1) Show all beers"
        +"\n2) Show all styles"
        +"\n3) Find a beer"
        +"\n4) Find a style"
        +"\n5) What's my style?")

    command = input("\nEnter a number > ")

    all_beer_list = pl.getBeers()
    all_style_list = pl.getStyles()
    all_beer_style_list = pl.getBeerStyle()

    