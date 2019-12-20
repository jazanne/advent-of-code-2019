from ddt import ddt, data, unpack
import unittest

from fuel import find_feul_by_mass

@ddt
class TestFeul(unittest.TestCase):

    @data([12, 2], [14, 2], [1969, 654], [100756, 33583])
    @unpack
    def test_find_feul_by_mass(self, mass, expected_fuel):
        '''Verify that fuel is calculated based on mass'''
        fuel = find_feul_by_mass(mass)

        self.assertEqual(fuel, expected_fuel)

if __name__ == '__main__':
    unittest.main()