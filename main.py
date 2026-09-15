from Handling_Data import *


application = True

pokemon_list = []

print("\nThis is an interface to create the pokemon csv list of the key information per pokemon you input. Please input values of a format: a, b, c, d. Type N to exit and type Clear to clear the list ")

while application:
    old_list = input("\nWhich pokemon do you want to see? ")

    if old_list == "default":
        old_list = "charmander, charmeleon, charizard, squirtle, wartortle, blastoise, bulbasaur, ivysaur, venusaur"

    try:
        old_list = old_list.split(",")
        pokemon_added = []

        if old_list[0].lower() == "n":
            application = False

        elif old_list[0].lower() == "clear":
            pokemon_list.clear()
            print("List cleared")

        else:
            for pokemon in old_list:
                pokemon = pokemon.strip()
                try:
                    if pokemon.strip() in pokemon_list:
                        print(f"{pokemon.capitalize()} is already in the csv. ")
                    else:
                        pokemon_list.append(pokemon)
                        create_csv(pokemon_list)
                        pokemon_added.append(pokemon)
                except KeyError:
                    print(f"The pokemon {pokemon} is not in the database. Please give valid input.")
                    application = False

            if len(pokemon_added) == 0:
                print("No pokemon were added to the csv")
            else:
                print("The following pokemon have been added to the csv file:", pokemon_added)
    except:
        print("Please give a valid input")