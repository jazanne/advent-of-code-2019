from functools import reduce
from math import floor as round_down

def find_feul_by_mass(mass):
    fuel = round_down(mass / 3) - 2
    return fuel

def calculate_fuel_of_modules(modules):
    pass