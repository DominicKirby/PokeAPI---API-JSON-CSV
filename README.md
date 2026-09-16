# PokeAPI- From API to .csv

## Introduction

This project involved calling upon the open API PokeAPI and converting the aquired .json file into a .csv format highlighting
only the important pieces of information, in this case being ID number, Pokemon name, base experience, Pokemon height, 
whether it is a default Pokemon, what order the Pokemon is, the Pokemon weight and a shortlist of its abilities.

The main.py file includes a user interface that gives the ability to add several pokemon all at once or individual pokemon, as 
well as a default set. This also accounts for edge cases and invalid inputs and where possible continues the application for 
further input. 

The requirements to run this file are unittest, requests, json, and csv installed on python version 3.14.7 or newer. 

## Testing

We also have a testing file that ensure everything is working in the file, and asserts whether the pulling function and the 
parsing function both give the right result with test case "Bulbasaur". These check various variables and ensure that the whole
function gives correct information in the csv file.

## Usage

The output of the main file goes into the pokemon.csv file and is a table with pokemon ID, name, base experience, height, whether
it is default, order, weight, and all abilities. The user inputs a list seperated by commas of all pokemon they would like to
view the key information, and has the option of adding further rows to the table if they wish, or clearing the table and starting
over. The csv file is constantly updating while the application is running and actively changes based on the user input. 

The input also accounts for invalid input and if the pokemon does not exist and instead of crashing the app it gives the correct
error message and then closes the app fully. 

## Functions 

#### Getting all information about a specific pokemon
```{python}
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
```

#### Parsing the key information about a specific pokemon
```{python}
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
```

#### Creating csv file
```{python}
def create_csv(pokemon: list):
    """
    Creating csv from the data we have parsed previously
    """
    # Headers of the csv
    header = ["id", "name", "base_experience", "height", "is_default", "order", "weight", "abilities"]

    if pokemon == [""]:
        with open("pokemon.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            for each in pokemon:
                writer.writerow(key_information_parsing(each))
    else:
        # Adding the new row to the csv for that pokemon using the previous function
        with open("pokemon.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            for each in pokemon:
                writer.writerow(key_information_parsing(each))
```
