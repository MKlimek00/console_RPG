import unittest
import utils

class TestInput(unittest.TestCase):
    
    def test_normalize_probabilities(self):
        result = utils.normalize_probabilities([1,2,1])
        self.assertEqual(result, [0.25, 0.5, 0.25])

if __name__ == '__main__':
    unittest.main()