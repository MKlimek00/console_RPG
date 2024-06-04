import unittest
import utils

class TestInput(unittest.TestCase):
    
    def test_normalize_probabilities_correct_input(self) -> None:
        """
        Sprawdzenie podstawowego działania funkcji
        """
        result = utils.normalize_probabilities([1,2,1])
        self.assertEqual(result, [0.25, 0.5, 0.25])

    def test_normalize_probabilities_negative_number_in_input(self) -> None:
        """
        Sprawdzenie zabezpieczeń na wypadek negatywnych liczb w liście
        """
        result = utils.normalize_probabilities([-3, -4, 3, 4, 1])
        self.assertEqual(result, [0.2, 0.2, 0.2, 0.2, 0.2])

    def test_normalize_probabilities_all_zeros(self) -> None:
        """
        Sprawdzenie zabezpieczeń na wypadek podania zer w liście
        """
        result = utils.normalize_probabilities([0,0,0,0])
        self.assertEqual(result, [0.25, 0.25, 0.25, 0.25])

if __name__ == '__main__':
    unittest.main()