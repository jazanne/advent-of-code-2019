from fuel import calculate_fuel_of_modules

def get_ints_from_file(filename):
    p = open(filename)

    #List:
    linelist = [int(line) for line in p.readlines()]
    return linelist

def main():
    # Day 1
    mods = get_ints_from_file('data-day1')
    fuel = calculate_fuel_of_modules(mods)
    print(fuel)

if __name__ == '__main__':
    main()