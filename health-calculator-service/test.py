import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):

    def test_calculate_bmi(self):
        # Valeurs modifiées pour l'IMC
        self.assertAlmostEqual(calculate_bmi(80, 1.80), 24.69, places=2)  # poids en kg, hauteur en mètres

    def test_calculate_bmr_male(self):
        # Valeurs modifiées pour le BMR d'un homme
        self.assertAlmostEqual(calculate_bmr(80, 1.80, 30, 'male'), 1886.18, places=2)  # poids en kg, hauteur en m
        
    def test_calculate_bmr_female(self):
        # Valeurs modifiées pour le BMR d'une femme
        self.assertAlmostEqual(calculate_bmr(65, 1.65, 28, 'female'), 1412.67, places=2)  # poids en kg, hauteur en m


if __name__ == '__main__':
    unittest.main()