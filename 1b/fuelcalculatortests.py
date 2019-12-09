import unittest
import fuelcalculator

class TestFuelCalculation(unittest.TestCase):

    def test_mass_14(self):
        self.assertEqual(fuelcalculator.calculate_fuel(14), 2)
    
    def test_mass_1969(self):
        self.assertEqual(fuelcalculator.calculate_fuel(1969), 966)
    
    def test_mass_100756(self):
        self.assertEqual(fuelcalculator.calculate_fuel(100756), 50346)

if __name__ == '__main__':
    unittest.main()