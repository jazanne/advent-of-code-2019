from math import floor as round_down

def find_feul_by_mass(mass):
    fuel = round_down(mass / 3) - 2
    return fuel