from ddt import ddt, data, unpack
import unittest

from fuel import calculate_fuel_for_mass_and_fuel, calculate_fuel_of_modules, find_fuel_by_mass

@ddt
class TestFeul(unittest.TestCase):

    @data([12, 2], [14, 2], [1969, 654], [100756, 33583])
    @unpack
    def test_find_fuel_by_mass(self, mass, expected_fuel):
        '''Verify that fuel is calculated based on mass'''
        fuel = find_fuel_by_mass(mass)

        self.assertEqual(fuel, expected_fuel)

    @data([14, 2], [1969, 966], [100756, 50346])
    @unpack
    def test_calculate_fuel_for_mass_and_fuel(self, mass, expected_fuel):
        '''Verify that we calculate the fuel for the fuel'''
        fuel = calculate_fuel_for_mass_and_fuel(mass)

        self.assertEqual(fuel, expected_fuel)

    def test_calculate_fuel_of_modules(self):
        '''Verify that fuel can be calculated for multiple modules'''
        modules = [14, 1969, 100756]
        expected_fuel = 2 + 966 + 50346
        fuel = calculate_fuel_of_modules(modules)

        self.assertEqual(fuel, expected_fuel)

if __name__ == '__main__':
    unittest.main()