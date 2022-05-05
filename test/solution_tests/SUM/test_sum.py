import sys
import unittest

PROJECT_ROOT = "C:/Users/cibele/Documents/Projects/runner-for-python-windows/accelerate_runner/"

sys.path.append(PROJECT_ROOT)

from lib.solutions.SUM import sum_solution

class TestSum(unittest.TestCase):
    def test_sum_equal(self):
        result = sum_solution.compute(1, 2) 
        self.assertEqual(result, 3)

    def test_sum_diff(self):
        result = sum_solution.compute(1, 2) 
        self.assertEqual(result, 4) 

    def test_sum_equal(self):
        result = sum_solution.compute(2, 2) 
        self.assertEqual(result, 4)

# if __name__ == '__main__':
#     unittest.main()           
