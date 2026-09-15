import requests
import json
import csv

def get_information(pokemon: str):
    """
    Requests the information about a given string of a pokemon
    """

    # Initial URL
    url = "https://pokeapi.co/api/v2/pokemon/"

    # Building new URL
    request = requests.get((url + pokemon))

    # Requesting the information from the API
    key_information = json.loads(request.text)
    return key_information



def key_information_parsing(pokemon: str):
    """
    Parses the key pokemon information from the JSON recieved from the get_information functions, takes json input and
    gives output including id, name, base_experience, height, is_default, order, weight, and names of abilities
    """
    # Using API to get pokemon information
    pokemon_info = get_information(pokemon)

    # Parsing key data
    id = pokemon_info["id"]
    name = pokemon_info["name"].capitalize()
    base_experience = pokemon_info["base_experience"]
    height = pokemon_info["height"]
    is_default = pokemon_info["is_default"]
    order = pokemon_info["order"]
    weight = pokemon_info["weight"]


    # Going into the abilities sub dictionary and retrieving the names to add to an abilities list in a unique format
    abilities = pokemon_info["abilities"]
    all_abilities = ""
    for ability in abilities:

        # Retrieving the name
        ability_name = ability["ability"]["name"]

        # Reformating the name
        ability_name = ability_name.capitalize()
        ability_name = ability_name.replace("-", " ")

        # Adding the abilities to a set list in the format of Blast, Attack move, etc.
        if all_abilities == "":
            all_abilities = ability_name
        else:
            all_abilities += ", " + ability_name

    # Returining all key information
    return [id, name, base_experience, height, is_default, order, weight, all_abilities]



def create_csv(pokemon: list):
    """
    Creating csv from the data we have parsed previously
    """

    # Headers of the csv
    header = ["id", "name", "base_experience", "height", "is_default", "order", "weight", "abilities"]

    # Adding the new row to the csv for that pokemon using the previous function
    with open("pokemon.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for each in pokemon:
            writer.writerow(key_information_parsing(each))
