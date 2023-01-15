import prolog as pl
from os import system
import random

def menu():
    
    while(True):
        #system('cls')

        mainMenuTextEng()

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:
            # beer section
            beerSectionMenu()

        elif user_input == 2:
            # style section
            styleSectionMenu()

        elif user_input == 3:
            # recommend me
            recommendMenu()      

        elif user_input == 4:
            # user manual
            userManualTextEng()

        elif user_input == 5:
            # exit
            break

        else:
            print("\n [!] I don't know this command!")

def beerSectionMenu():
    while(True):
        beerMenuTextEng()

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:
            # print 5 random beers or all
            printBeerMenu()

        elif user_input == 2:
            # find a beer by name/id
            findBeerMenu()
            
        elif user_input == 3:
            # info/help
            styleManualEng()

        elif user_input == 4:
            # exit
            break

        else:
            print("\n [!] I don't know this command!")

def styleSectionMenu():
    while(True):
        styleMenuTextEng()

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:
            # print 5 random styles or all
            printStyleMenu()

        elif user_input == 2:
            # find a style by name/id
            findStyleMenu()

        elif user_input == 3:
            # info/help
            styleManualEng()

        elif user_input == 4:
            # exit
            break

        else:
            print("\n [!] I don't know this command!")

def recommendMenu():
    while(True):
        recommendMenuTextEng()

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:
            # logic classifier
            fastRecommenderMenu()

        elif user_input == 2:
            # probabilistic classifier
            slowRecommenderMenu()

        elif user_input == 3:
            # info/help
            styleManualEng()

        elif user_input == 4:
            # exit
            break
        else:
            print("\n [!] I don't know this command!")

def printBeerMenu():
    beers = pl.getBeers()

    while(True):
        print("\n 1 -- Print all beers"
        +"\n 2 -- Print a random beer"
        +"\n 3 -- Return to main menu")

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:
            # all beers
            for b in beers:
                print(f"\nBeer name: {b['Beer_name']} (ID: {b['Beer_id']}")

        elif user_input == 2:
            # 1 random beer
            r = random.randint(1,110)

            print(f"\nBeer name: {beers[r]['Beer_name']} (ID: {beers[r]['Beer_id']})")

        elif user_input == 3:
            # exit
            break

        else:
            print("\n [!] I don't know this command!")

def findBeerMenu():
    beers = pl.getBeers()
    abvs = pl.getBeerAbvs()
    reviews = pl.getBeerReviews()

    while(True):
        print("\n 1 -- Find by name"
        +"\n 2 -- Find by ID"
        +"\n 3 -- Return to Beer section")

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:
            # by name
            input_name = input("\nEnter beer name: ")

            found = False

            for b in beers:
                if input_name == b['Beer_name']:
                    id = b['Beer_id']
                    found = True

            if found:
                print(f"\nFound it!")
                print(f"\nID: {beers[id]['Beer_id']}")
                print(f"ABV: {abvs[id]['Abv']}")
                print(f"Review: {reviews[id]['Review']}")
            else:
                print(f"\nNot found...")

        elif user_input == 2:
            # by id
            input_id = int(input("\nEnter beer ID: "))

            found = False

            for b in beers:
                if input_id == b['Beer_id']:
                    found = True

            if found:
                print("\nFound it!")
                print(f"\nName: {beers[input_id]['Beer_name']}")
                print(f"ABV: {abvs[input_id]['Abv']}")
                print(f"Review: {reviews[input_id]['Review']}")
            else:
                print("\nNot found...")

        elif user_input == 3:
            break
        else:
            print("\n [!] I don't know this command!")

def printStyleMenu():
    styles = pl.getStyles()

    while(True):
        print("\n 1 -- Print all styles"
        +"\n 2 -- Print a random style"
        +"\n 3 -- Return to main menu")

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:
            # all styles
            for s in styles:
                print(f"\nStyle name: {s['Style_name']} (ID: {s['Style_id']})")

        elif user_input == 2:
            # 1 random style
            r = random.randint(1,110)
            desc = list(pl.prolog.query(f"desc(X, Mouthfeel, Taste, Flavour)"))
            print(f"\nStyle name: {styles[r]['Style_name']} (ID: {styles[r]['Style_id']})")
            print(f"Description: {desc[r]['Mouthfeel']}, {desc[r]['Taste']}, {desc[r]['Flavour']}")
            
        elif user_input == 3:
            # exit
            break

        else:
            print("\n [!] I don't know this command!")

def findStyleMenu():
    styles = pl.getStyles()
    desc = list(pl.prolog.query(f"desc(X, Mouthfeel, Taste, Flavour)"))

    while(True):
        print("\n 1 -- Find by name"
        +"\n 2 -- Find by ID"
        +"\n 3 -- Return to Style section")

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:
            # by name
            input_name = input("\nEnter style name: ")

            found = False

            for s in styles:
                if input_name == s['Style_name']:
                    id = s['Style_id']
                    found = True

            if found:
                print(f"\nFound it!")
                print(f"ID: {id}")
                print(f"Description: {desc[id]['Mouthfeel']}, {desc[id]['Taste']}, {desc[id]['Flavour']}")
            else:
                print(f"\nNot found...")

        elif user_input == 2:
            # by id
            input_id = int(input("\nEnter style ID: "))

            found = False

            for s in styles:
                if input_id == s['Style_id']:
                    found = True

            if found:
                print("\nFound it!")
                print(f"\nStyle: {styles[input_id]['Style_name']}")
                print(f"Description: {desc[input_id]['Mouthfeel']}, {desc[input_id]['Taste']}, {desc[input_id]['Flavour']}")
            else:
                print("\nNot found...")

        elif user_input == 3:
            break
        else:
            print("\n [!] I don't know this command!")

def fastRecommenderMenu():
    styles = pl.getStyles()

    print("\nI will ask you about:"
    +"\n> Mouthfeell (or texture)"
    +"\n> Taste (perception)"
    +"\n> Flavour (smell)"
    +"\nThen I will show you 2 different recommended styles!")

    first_input = input("\n[Astringent, body, alcohol?]: ")
    second_input = input("\n[Bitter, sweet, sour, salty?]: ")
    third_input = input("\n[Fruits, hoppy, spices, malty?]: ")

    desc = pl.userDesc(first_input, second_input, third_input)
    

    found = False
    found_bayes = False

    if len(desc) > 0:
        for s in styles:
            if s['Style_id'] == desc[0]['X']:
                name = s['Style_name']
                id = s['Style_id']
                found = True
    else: id = -1

    bayes = pl.userBayes(id, first_input, second_input, third_input)
    perc = 100 - bayes[0]['Value']*100

    if id != -1:
        if found:
            print(f"\nYour generic style is {name} (ID: {id})")
            print(f"Recommendation rate: {perc:.2f}%")
        else:
            print("\nSorry, I don't know what to recommend...")
    else:
        print("\nSorry, I don't know what to recommend...")
    


def slowRecommenderMenu():
    styles = pl.getStyles()

    print("\nI will ask you about:"
    +"\n> Mouthfeell (or texture)"
    +"\n> Taste (perception)"
    +"\n> Flavour (smell)")

    astringency = int(input("\nAstringency (1 to 5): "))
    body = int(input("\nBody (1 to 5): "))
    alcohol = int(input("\nAlcohol (1 to 5): "))

    bitter = int(input("\nBitterness (1 to 5): "))
    sweet = int(input("\nSweetness (1 to 5): "))
    sour = int(input("\nSourness (1 to 5): "))
    salty = int(input("\nSaltiness (1 to 5): "))

    fruity = int(input("\nFruits (1 to 5): "))
    hoppy = int(input("\nHoppiness (1 to 5): "))
    spices = int(input("\nSpices (1 to 5): "))
    malty = int(input("\nMaltiness (1 to 5): "))

    mouthfeel = pl.userMouthfeel(astringency, body, alcohol)
    taste = pl.userTaste(bitter, sweet, sour, salty)
    flavour = pl.userFlavour(fruity, hoppy, spices, malty)

    if len(mouthfeel) > 0:
        for s in styles:
            if s['Style_id'] == mouthfeel[0]['Style']:
                print(f"\nYour mouthfeel related style is {s['Style_name']} (ID: {s['Style_id']})")

    elif len(taste) > 0:
        for s in styles:
            if s['Style_id'] == taste[0]['Style']:
                print(f"\nYour taste related style is {s['Style_name']} (ID: {s['Style_id']})")

    elif len(flavour) > 0:
        if s['Style_id'] == flavour[0]['Style']:
            print(f"\nYour flavour related style is {s['Style_name']} (ID: {s['Style_id']})")

def mainMenuTextEng():
    print("\n Welcome!\n"
    +"\n 1 -- Beer section"
    +"\n 2 -- Style section"
    +"\n 3 -- Recommend me"
    +"\n 4 -- User Manual"
    +"\n 5 -- Exit")

def beerMenuTextEng():
    print("\n # --- Beer section --- #\n"
    +"\n 1 -- Show beers"
    +"\n 2 -- Find a beer"
    +"\n 3 -- Information/help"
    +"\n 4 -- Return to main menu")

def styleMenuTextEng():
    print("\n # --- Style section --- #\n"
    +"\n 1 -- Show styles"
    +"\n 2 -- Find a style"
    +"\n 3 -- Information/help"
    +"\n 4 -- Return to main menu")

def recommendMenuTextEng():
    print("\n # --- Recommend me --- #\n"
    +"\n 1 -- Fast recommendation"
    +"\n 2 -- Slow recommendation"
    +"\n 3 -- Information/help"
    +"\n 4 -- Return to main menu")

def userManualTextEng():
    print("\n # ------ User Manual ------ #"
    +"\n\n [Beer section]"
    +"\n     In this section you can read and search between 3600 worldwide beers."
    +"\n     Maybe there's your favourite beer too!"
    +"\n\n [Style section]"
    +"\n     In this section you can read and search between 110 worldwide styles."
    +"\n     Maybe there's your favourite style too!"
    +"\n\n [Recommend me]"
    +"\n     There are two different recommender:"
    +"\n     1. Fast recommender: 3 words in, 1 style out"
    +"\n     2. Slow recommender: 11 numbers in, 1 style out"
    +"\n     The fast one is less accurate then the second one but is faster!!!")

def styleManualEng():
    print("\n # ------ Style Manual ------ #"
    +"\n\n [Mouthfeel]"
    +"\n     Refers to the physical sensations in the mouth caused by food or drink;"
    +"\n     is often related to a product's water activity."
    +"\n\n [Taste]"
    +"\n     Determines flavors of food and other substances. "
    +"\n\n [Flavour]"
    +"\n     Taste of smell.")