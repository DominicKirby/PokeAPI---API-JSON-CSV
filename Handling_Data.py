from Pulling_data import *
import csv

test_json = get_information("ditto")

def json_create(pokemon: str):
    pokemon_info = get_information(pokemon)
    json.dump(pokemon_info, open("pokemon.json", "w"))


def key_information_parsing(pokemon: str):
    pokemon_info = get_information(pokemon)
    id = pokemon_info["id"]
    name = pokemon_info["name"]
    base_experience = pokemon_info["base_experience"]
    height = pokemon_info["height"]
    is_default = pokemon_info["is_default"]
    order = pokemon_info["order"]
    weight = pokemon_info["weight"]

    return [id, name, base_experience, height, is_default, order, weight]


print(key_information_parsing("ditto"))


def create_csv(pokemon: list):
    header = ["id", "name", "base_experience", "height", "is_default", "order", "weight"]
    with open("pokemon.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for pokemon in pokemon:
            writer.writerow(key_information_parsing(pokemon))

pokemon_list = ["abra", "charmander", "ditto"]

create_csv(pokemon_list)