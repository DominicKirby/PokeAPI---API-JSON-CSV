from Handling_Data import *

# Setting the application to run until it is told to stop
application = True

# Empty list to be added to later
pokemon_list = []

# User information
print("\nThis is an interface to create the pokemon csv list of the key information per pokemon you input.\nPlease input values of a format: a, b, c, d.\nType N to exit, Clear to clear the list and default for a general set.")

while application:
    # Creating an old list to add to the pre-existing pokemon list
    old_list = input("\nWhich pokemon do you want to see? ")

    # Setting a default value for if you user wants a general output
    if old_list == "default":
        old_list = "bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise "

    # Trying to add the pokemon to the csv file and if it fails then determining this is an invalid input
    try:
        # Separating the input into an iterable list
        old_list = old_list.split(",")

        # Creating a list to give reference to the user about what has been added to the list
        pokemon_added = []

        # Giving the user the ability to exit
        if old_list[0].lower() == "n":
            application = False

        # Giving the user the ability to clear the current csv file
        elif old_list[0].lower() == "clear":
            pokemon_list.clear()
            print("List cleared")

        # Adding the new pokemon to the pre-existing list and csv file
        else:
            for pokemon in old_list:
                pokemon = pokemon.strip()
                try:
                    # Checking whether its already in the list and giving a message if so
                    if pokemon.strip() in pokemon_list:
                        print(f"{pokemon.capitalize()} is already in the csv. ")

                    # Adding the pokemon to the csv
                    else:
                        pokemon_list.append(pokemon)
                        create_csv(pokemon_list)
                        pokemon_added.append(pokemon)
                except KeyError:
                    # If the pokemon was not found in the database giving a real return and leaving the application
                    print(f"The pokemon {pokemon} is not in the database. Please give valid input.")
                    application = False

            # Giving a unique output for no pokemon added
            if len(pokemon_added) == 0:
                print("No pokemon were added to the csv")
            # General answer with the pokemon added in this iteration
            else:
                print("The following pokemon have been added to the csv file:", pokemon_added)
    # Error message
    except:
        print("Please give a valid input")