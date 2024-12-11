import unittest
from p2 import isSafe

class TestIsSafe(unittest.TestCase):
    def test_no_errors(self):
        report = [1, 2, 3, 4, 5]
        self.assertTrue(isSafe(report))

    def test_one_error_at_end(self):
        report = [1, 2, 3, 4, 10]
        self.assertTrue(isSafe(report))

    def test_one_error_at_start(self):
        report = [10, 2, 3, 4, 5]
        self.assertTrue(isSafe(report))

    def test_two_errors_at_start(self):
        report = [1, 7, 5, 7, 9]
        self.assertFalse(isSafe(report))

    def test_one_error_in_middle(self):
        report = [1, 2, 10, 4, 5]
        self.assertTrue(isSafe(report))

    def test_multiple_errors(self):
        report = [1, 10, 3, 10, 5]
        self.assertFalse(isSafe(report))

    def test_all_errors(self):
        report = [10, 10, 10, 10, 10]
        self.assertFalse(isSafe(report))

    def test_empty_report(self):
        report = []
        self.assertFalse(isSafe(report))

    def test_single_element_report(self):
        report = [1]
        self.assertFalse(isSafe(report))

    def test_report_with_zero_diff(self):
        report = [1, 1, 1, 1, 1]
        self.assertFalse(isSafe(report))

if __name__ == '__main__':
    unittest.main()
