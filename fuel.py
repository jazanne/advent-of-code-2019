from functools import reduce
from math import floor as round_down

def find_fuel_by_mass(mass):
    fuel = round_down(mass / 3) - 2
    return fuel

def calculate_fuel_for_mass_and_fuel(mass):
    pass

def calculate_fuel_of_modules(modules):
    fuel = 0
    for mass in modules:
        fuel += find_fuel_by_mass(mass)
    return fuel