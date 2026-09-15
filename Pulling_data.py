import requests
import json
import csv

def get_information(pokemon: str):
    url = "https://pokeapi.co/api/v2/pokemon/"

    request = requests.get((url + pokemon))

    key_information = json.loads(request.text)

    return key_information


