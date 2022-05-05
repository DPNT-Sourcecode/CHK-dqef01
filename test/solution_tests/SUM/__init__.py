import sys

PROJECT_ROOT = "C:/Users/cibele/Documents/Projects/runner-for-python-windows/accelerate_runner/test"
sys.path.append(PROJECT_ROOT)

import solution_tests.SUM.test_sum as st

Test = st.TestSum()

result_equal = Test.test_sum_positive_equal()

result_diff = Test.test_sum_positive_diff()

result_negative = Test.test_sum_negative()





