import prolog as pl
from os import system
import random

def menuOptions():
    print("\nWelcome!\n"
        +"\n 1 -- Show all beers"
        +"\n 2 -- Show all styles"
        +"\n 3 -- Find a beer"
        +"\n 4 -- Find a style"
        +"\n 5 -- What's my style?"
        +"\n 6 -- Exit")

def menu():
    
    while(True):

        #system('cls')

        menuOptions()

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:
            menuBeer()

        elif user_input == 2:
            menuStyle()

        elif user_input == 3:
            menuFindBeer()

        elif user_input == 4:
            menuFindStyle()

        elif user_input == 5:
            menuUserStyle()
        
        elif user_input == 6:
            break

        else:
            print("\n[!] I don't know this command!")

def menuBeer():
    # print some beers
    all_beer_list = pl.getBeers()

    while(True):

        #system('cls')

        print("\n --- Beer Menu ---\n"
        +"\n 1 -- Show all beers"
        +"\n 2 -- Show a random beer"
        +"\n 3 -- Return to menu")

        user_input = int(input("\nEnter a number: "))

        if user_input == 1:

            # print all beers in all_beer_list
            for beer in all_beer_list:
                print(f"\nBeer name: {beer['Beer_name']} (ID: {beer['Beer_id']})")

        elif user_input == 2:

            # print a random beer in all_beer_list
            random_beer = random.randint(0,110)
            print(f"\nBeer name: {all_beer_list[random_beer]['Beer_name']} (ID: {all_beer_list[random_beer]['Beer_id']})")

        elif user_input == 3:
            break

        else:
            print("\n[!] I don't know this command!")
 

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
            # non mi va di farlo...
            print("TODO")

        elif user_input == 5:
            break

        else:
            print("\n[!] I don't know this command!")