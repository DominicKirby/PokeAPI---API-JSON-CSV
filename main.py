from Handling_Data import *


application = True

pokemon_list = []

while application:
    old_list = input("\nWhich pokemon do you want to see? ")


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
                try:
                    if pokemon in pokemon_list:
                        print(f"Pokemon {pokemon} is already in the csv. ")
                    else:
                        pokemon_list.append(pokemon.split()[0])
                    create_csv(pokemon_list)
                    pokemon_added.append(pokemon)
                except KeyError:
                    print(f"The pokemon {pokemon.split()[0]} is not in the database.")
            print("The following pokemon have been added to the csv file:", pokemon_added)
    except:
        print("Please give a valid input")