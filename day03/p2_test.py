import unittest
from p2 import main
import re

class TestDay03Part2(unittest.TestCase):
    def test_main_mul(self):
        # Test with a single mul operation
        lines = ["mul(2,4)"]
        expected_output = 8
        self.assertEqual(main(lines), expected_output)

    def test_main_do(self):
        # Test with a single do operation
        lines = ["do()"]
        expected_output = 0
        self.assertEqual(main(lines), expected_output)

    def test_main_dont(self):
        # Test with a single don't operation
        lines = ["don't()"]
        expected_output = 0
        self.assertEqual(main(lines), expected_output)

    def test_main_multiple_operations(self):
        # Test with multiple operations
        lines = ["mul(2,4)&do()&mul(3,5)&don't()"]
        expected_output = 23
        self.assertEqual(main(lines), expected_output)

    def test_main_invalid_input(self):
        # Test with invalid input
        lines = [" invalid input "]
        expected_output = 0
        self.assertEqual(main(lines), expected_output)

    def test_main_empty_input(self):
        # Test with empty input
        lines = []
        expected_output = 0
        self.assertEqual(main(lines), expected_output)

    def test_regex_pattern(self):
        # Test the regex pattern
        pattern = r"(mul)\((\d{,3}),(\d{,3})\)|(do)\(\)|(don't)\(\)"
        self.assertTrue(re.match(pattern, "mul(2,4)"))
        self.assertTrue(re.match(pattern, "do()"))
        self.assertTrue(re.match(pattern, "don't()"))

if __name__ == '__main__':
    unittest.main()
