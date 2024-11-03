import unittest

class TestFactorielle(unittest.TestCase):
    
    def test_factorielle_positive(self):
        self.assertEqual(factorielle(5), 120)
        self.assertEqual(factorielle(3), 6)
    
    def test_factorielle_zero(self):
        self.assertEqual(factorielle(0), 1)
    
    def test_factorielle_un(self):
        self.assertEqual(factorielle(1), 1)

    def test_factorielle_negative(self):
        with self.assertRaises(ValueError):
            factorielle(-5)

if __name__ == "__main__":
    unittest.main()
