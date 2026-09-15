import requests
import json
import csv

def get_information(pokemon: str):
    url = "https://pokeapi.co/api/v2/pokemon/"
    request = requests.get((url + pokemon))
    key_information = json.loads(request.text)
    return key_information

print(get_information("Bulbasaur")["id"])

def json_create(pokemon: str):
    pokemon_info = get_information(pokemon)
    json.dump(pokemon_info, open("pokemon.json", "w"))

def key_information_parsing(pokemon: str):
    pokemon_info = get_information(pokemon)
    id = pokemon_info["id"]
    name = pokemon_info["name"].capitalize()
    base_experience = pokemon_info["base_experience"]
    height = pokemon_info["height"]
    is_default = pokemon_info["is_default"]
    order = pokemon_info["order"]
    weight = pokemon_info["weight"]

    abilities = pokemon_info["abilities"]
    all_abilities = ""
    for ability in abilities:
        ability_name = ability["ability"]["name"]
        ability_name = ability_name.capitalize()
        ability_name = ability_name.replace("-", " ")

        if all_abilities == "":
            all_abilities = ability_name
        else:
            all_abilities += ", " + ability_name

    return [id, name, base_experience, height, is_default, order, weight, all_abilities]

def create_csv(pokemon: list):
    header = ["id", "name", "base_experience", "height", "is_default", "order", "weight", "abilities"]
    with open("pokemon.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for each in pokemon:
            writer.writerow(key_information_parsing(each))
