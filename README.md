# PokeAPI- From API to .csv

### Introduction

This project involved calling upon the open API PokeAPI and converting the aquired .json file into a .csv format highlighting
only the important pieces of information, in this case being ID number, Pokemon name, base experience, Pokemon height, 
whether it is a default Pokemon, what order the Pokemon is, the Pokemon weight and a shortlist of its abilities.

The main.py file includes a user interface that gives the ability to add several pokemon all at once or individual pokemon, as 
well as a default set. This also accounts for edge cases and invalid inputs and where possible continues the application for 
further input. 

The requirements to run this file are unittest, requests, json, and csv installed on python version 3.14.7 or newer. 

### Testing

We also have a testing file that ensure everything is working in the file, and asserts whether the pulling function and the 
parsing function both give the right result with test case "Bulbasaur". These check various variables and ensure that the whole
function gives correct information in the csv file.


### Functions 

 . . .
