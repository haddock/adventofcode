import unittest
import fuelcalculator

class TestFuelCalculation(unittest.TestCase):

    def test_mass_12(self):
        self.assertEqual(fuelcalculator.calculate_fuel(12), 2)
    
    def test_mass_14(self):
        self.assertEqual(fuelcalculator.calculate_fuel(14), 2)
    
    def test_mass_1969(self):
        self.assertEqual(fuelcalculator.calculate_fuel(1969), 654)
    
    def test_mass_100756(self):
        self.assertEqual(fuelcalculator.calculate_fuel(100756), 33583)
    
    def test_masses_from_file(self):
        self.assertEqual(fuelcalculator.calculate_total_fuel_from_file("massestest.txt"), 34241)

if __name__ == '__main__':
    unittest.main()