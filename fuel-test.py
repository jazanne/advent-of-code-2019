from ddt import ddt, data, unpack
import unittest

from fuel import calculate_fuel_of_modules, find_feul_by_mass

@ddt
class TestFeul(unittest.TestCase):

    @data([12, 2], [14, 2], [1969, 654], [100756, 33583])
    @unpack
    def test_find_feul_by_mass(self, mass, expected_fuel):
        '''Verify that fuel is calculated based on mass'''
        fuel = find_feul_by_mass(mass)

        self.assertEqual(fuel, expected_fuel)


    def test_calculate_fuel_of_modules(self):
        '''Verify that fuel can be calculated for multiple modules'''
        modules = [12, 14, 1969, 33583]
        expected_fuel = 2 + 2 + 654 + 33583
        fuel = calculate_fuel_of_modules(modules)

        self.assertEqual(fuel, expected_fuel)

if __name__ == '__main__':
    unittest.main()