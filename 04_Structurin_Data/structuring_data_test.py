import unittest
from unittest.mock import patch
import sys
from io import StringIO
from structuring_data import *


class TestExercise04(unittest.TestCase):
    @patch('builtins.input', side_effect=['r', 5])
    def test_element_in_tuple(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        element_in_tuple()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "True\nFalse")

    def test_list_to_tuple(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        list_to_tuple()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "[5, 10, 7, 4, 15, 3]\n(5, 10, 7, 4, 15, 3)")

    def test_length_of_tuple(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        length_of_tuple()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(
            output, "('W', 'e', 'T', 'h', 'i', 'n', 'k', 'C', 'o', 'd', 'e')\n11")

    def test_sum_of_list(self):
        numbers = (1, 5, 43, 2, 23)
        self.assertEqual(sum_of_list(numbers), 74)

    def test_multiply_list(self):
        numbers = (1, 5, 4, -2, 23)
        self.assertEqual(multiply_list(numbers), -920)

    def test_unique_list(self):
        numbers = [1, 1, 5, 5, 4, -2, 23, 7, 7, 7]
        self.assertEqual(unique_list(numbers), [1, 5, 4, -2, 23, 7])

    def test_palindrome(self):
        valid_name = ('anna', 'number', 'madam', 'racecar',
                      'noon', 'level', 'kayak', 'mom', 'civic')
        string = 'jay'
        if (string in valid_name):
            self.assertEqual(palindrome(string), True)
        else:
            self.assertEqual(palindrome(string), False)


if __name__ == "__main__":
    unittest.main()
