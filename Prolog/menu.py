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
        elif user_input == 4:
            # info/help
            userManualTextEng()
        elif user_input == 5:
            # exit
            break
        else:
            print("\n [!] I don't know this command!")

def styleSectionMenu():
    while(True):
        beerMenuTextEng()

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:
            # print 5 random styles or all
            printStyleMenu()
        elif user_input == 2:
            # find a style by name/id
            findStyleMenu()
        elif user_input == 4:
            # info/help
            userManualTextEng()
        elif user_input == 5:
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
            userManualTextEng()
        elif user_input == 4:
            # exit
            break
        else:
            print("\n [!] I don't know this command!")

def printBeerMenu():
    beers = pl.getBeers()

    while(True):
        print("\n 1 -- Print all random beers"
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
                    found = True

            if found:
                print(f"\nFound it!")
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
            print(f"\nStyle name: {styles[r]['Style_name']} (ID: {styles[r]['Style_id']})")
        elif user_input == 3:
            # exit
            break
        else:
            print("\n [!] I don't know this command!")

def findStyleMenu():
    styles = pl.getBeers()

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
                if input_name == s['Beer_style']:
                    found = True

            if found:
                print(f"\nFound it!")
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
    +"\n> Flavour (smell)")

    first_input = input("\n[Astringent, body, alcohol?]: ")
    second_input = input("\n[Bitter, sweet, sour, salty?]: ")
    third_input = input("\n[Fruits, hoppy, spices, malty?]: ")

    desc = pl.userDesc(first_input, second_input, third_input)

    found = False

    if len(desc) > 0:
        for s in styles:
            if s['Style_id'] == desc[0]['X']:
                name = s['Style_name']
                id = s['Style_id']
                found = True
    
    if found:
        print(f"\nYour generic style is {name} (ID: {id})")
    else:
        print("Sorry, I don't know what to recommend...")


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
 

def menuStyle():
    # print some styles
    all_style_list = pl.getStyles()

    while(True):

        #system('cls')

        print("\n --- Beer Menu ---\n"
        +"\n 1 -- Show all styles"
        +"\n 2 -- Show a random style"
        +"\n 3 -- Return to menu")

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:

            # print all beers in all_beer_list
            for style in all_style_list:
                print(f"\nStyle name: {style['Style_name']} (ID: {style['Style_id']})")

        elif user_input == 2:

            # print a random beer in all_beer_list
            random_style = random.randint(0,110)
            print(f"\nStyle name: {all_style_list[random_style]['Style_name']} (ID: {all_style_list[random_style]['Style_id']})\n")

        elif user_input == 3:
            break

        else:
            print("\n[!] I don't know this command!")

def menuFindBeer():
    # find a beer by name or ID
    all_beer_list = pl.getBeers()

    while(True):

        #system('cls')

        print("\n --- Find-A-Beer Menu ---\n"
        +"\n 1 -- Find by name"
        +"\n 2 -- Find by ID"
        +"\n 3 -- Return to menu")

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:

            print("\n > Beer name: ")

            input_name = input()

            found_it = False

            # find a beer by name
            for beer in all_beer_list:
                if beer['Beer_name'] == input_name:
                    found_it = True

            if found_it:
                print("Found it!")
            else:
                print("Not found...")

        elif user_input == 2:

            print("\n > Beer ID (0 to 3600): ")

            input_id = input()

            found_it = False

            # find a beer by ID
            for beer in all_beer_list:
                if beer['Beer_id'] == input_id:
                    found_it = True

            if found_it:
                print("Found it!")
            else:
                print("Not found...")

        elif user_input == 3:
            break

        else:
            print("\n[!] I don't know this command!")

def menuFindStyle():
    # find a style by name or ID
    all_style_list = pl.getStyles()

    while(True):

        #system('cls')

        print("\n --- Find-A-Style Menu ---\n"
        +"\n 1 -- Find by name"
        +"\n 2 -- Find by ID"
        +"\n 3 -- Return to menu")

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:

            print("\n > Style name: ")

            input_name = input()

            found_it = False

            # find a beer by name
            for style in all_style_list:
                if style['Style_name'] == input_name:
                    found_it = True

            if found_it:
                print("Found it!")
            else:
                print("Not found...")

        elif user_input == 2:

            print("\n > Style ID (0 to 110): ")

            input_id = input()

            found_it = False

            # find a beer by ID
            for style in all_style_list:
                if style['Style_id'] == input_id:
                    found_it = True

            if found_it:
                print("Found it!")
            else:
                print("Not found...")

        elif user_input == 3:
            break

        else:
            print("\n[!] I don't know this command!")

def menuUserStyle():
    # find user's style
    all_style_list = pl.getStyles()

    while(True):

        print("\n --- What's my style? --- \n"
        +"\n 1 -- Taste related style"
        +"\n 2 -- Flavour related style"
        +"\n 3 -- Mouthfeel related style"
        +"\n 4 -- My generic style"
        +"\n 5 -- Return to menu")

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:

            a_input = input("\nSweetness: ")
            b_input = input("\nBitterness: ")
            c_input = input("\nSourness: ")
            d_input = input("\nSaltiness: ")

            taste = pl.userTaste(a_input, b_input, c_input, d_input)

            for style in all_style_list:
                if style['Style_id'] == taste[0]['Style']:
                    print(f"\nYour taste related style is {style['Style_name']} (ID: {style['Style_id']})")

        elif user_input == 2:

            a_input = input("\nFruitness: ")
            b_input = input("\nHoppiness: ")
            c_input = input("\nMaltiness: ")
            d_input = input("\nSpiciness: ")

            flavour = pl.userFlavour(a_input, b_input, c_input, d_input)

            for style in all_style_list:
                if style['Style_id'] == flavour[0]['Style']:
                    print(f"\nYour flavour related style is {style['Style_name']} (ID: {style['Style_id']})")

        elif user_input == 3:

            a_input = input("\nAstringenciness: ")
            b_input = input("\nBodiness: ")
            c_input = input("\nAlcholiness: ")

            mouthfeel = pl.userMouthfeel(a_input, b_input, c_input)
            
            for style in all_style_list:
                if style['Style_id'] == mouthfeel[0]['Style']:
                    print(f"\nYour taste related style is {style['Style_name']} (ID: {style['Style_id']})")

        elif user_input == 4:

            astringency_input = input("\nAstringent, Body or Alcohol: ")
            taste_input = input("\nBitter, sweet, sour or salty: ")
            flavour_input = input("\nFruits, hoppy, spices or malty: ")

            desc = pl.userDesc(astringency_input, taste_input, flavour_input)

            found = False

            for style in all_style_list:
                if style['Style_id'] == desc[0]['X']:
                    print(f"\nYour generic style is {style['Style_name']} (ID: {style['Style_id']})")
                    found = True

            if found == False: print("You have unique taste...")

        elif user_input == 5:
            break

        else:
            print("\n[!] I don't know this command!")

def localization():
    print("\n Select your language:"
    +" 1 -- Italiano"
    +" 2 -- English")

def mainMenuTextEng():
    print("\n Welcome!"
    +"\n 1 -- Beer section"
    +"\n 2 -- Style section"
    +"\n 3 -- Recommend me"
    +"\n 4 -- User Manual"
    +"\n 5 -- Exit")

def mainMenuTextIta():
    print("\n Benvenuto!"
    +"\n 1 -- Sezione birre"
    +"\n 2 -- Sezione stili"
    +"\n 3 -- Consigliami tu"
    +"\n 4 -- Manuale utente"
    +"\n 5 -- Esci")

def beerMenuTextEng():
    print("\n # --- Beer section --- #"
    +"\n 1 -- Show me all beers"
    +"\n 2 -- I want to find a beer"
    +"\n ? -- Coming soon..."
    +"\n 4 -- Information/help"
    +"\n 5 -- Return to main menu")

def beerMenuTextIta():
    print("\n # --- Sezione birre --- #"
    +"\n 1 -- Mostrami tutte le birre"
    +"\n 2 -- Voglio cercare una birra"
    +"\n ? -- Prossimamente..."
    +"\n 4 -- Informazioni/aiuto"
    +"\n 5 -- Torna al menu principale")

def styleMenuTextEng():
    print("\n # --- Style section --- #"
    +"\n 1 -- Show me all styles"
    +"\n 2 -- I want to find a style"
    +"\n ? -- Coming soon..."
    +"\n 4 -- Information/help"
    +"\n 5 -- Return to main menu")

def styleMenuTextIta():
    print("\n # --- Sezione stili --- #"
    +"\n 1 -- Mostrami tutti gli stili"
    +"\n 2 -- Voglio cercare uno stile"
    +"\n ? -- Prossimamente..."
    +"\n 4 -- Informazioni/aiuto"
    +"\n 5 -- Torna al menu principale")

def recommendMenuTextEng():
    print("\n # --- Recommend me --- #"
    +"\n 1 -- Fast recommendation"
    +"\n 2 -- Slow recommendation"
    +"\n 3 -- Information/help"
    +"\n 4 -- Return to main menu")

def recommendMenuTextIta():
    print("\n # --- Consigliami --- #"
    +"\n 1 -- Consiglio rapido"
    +"\n 2 -- Consiglio lento"
    +"\n 3 -- Informazioni/aiuto"
    +"\n 4 -- Torna al menu principale")

def userManualTextEng():
    print("\n # --- User Manual --- #"
    +"\n 1 -- Beer section"
    +"\n     In this section you can read and search between 3600 worldwide beers."
    +"\n     Maybe there's your favourite beer too!"
    +"\n 2 -- Style section"
    +"\n     In this section you can read and search between 110 worldwide styles.") 