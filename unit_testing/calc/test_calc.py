import calc
import unittest

class TestCalc(unittest.TestCase):

    def test_add(self):
        # Method's name must follow test_<function_name> convention

        # It is not about writing a lot of tests but writing good
        # tests on edges cases
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)

    def test_divide(self):
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(1, -1), -1)
        self.assertRaises(ValueError, calc.divide, 1, 0)
        # You can also use a context manager to test exceptions
        with self.assertRaises(ValueError):
            calc.divide(2, 0)

if __name__ == "__main__":
    unittest.main()
