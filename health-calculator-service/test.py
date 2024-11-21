import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):

    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)  # weight in kg, height in meters

    def test_calculate_bmr_male(self):
        self.assertAlmostEqual(calculate_bmr(70, 175, 25, 'male'), 1706.69, places=2)  # weight in kg, height in cm
        
    def test_calculate_bmr_female(self):
        self.assertAlmostEqual(calculate_bmr(60, 160, 30, 'female'), 1384.14, places=2)  # weight in kg, height in cm


if __name__ == '__main__':
    unittest.main()