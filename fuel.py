from functools import reduce
from math import floor as round_down

def find_fuel_by_mass(mass):
    fuel = round_down(mass / 3) - 2
    return fuel

def calculate_fuel_for_mass_and_fuel(mass):
    fuel = 0
    new_fuel = find_fuel_by_mass(mass)
    while new_fuel > 0:
        fuel += new_fuel
        new_fuel = find_fuel_by_mass(new_fuel)

    return fuel

def calculate_fuel_of_modules(modules):
    fuel = 0
    for mass in modules:
        fuel += calculate_fuel_for_mass_and_fuel(mass)
    return fuel