import unittest
from unittest.mock import patch
import sys
from io import StringIO
from combining_instructions import *


class TestExercise03(unittest.TestCase):
    @patch('builtins.input', side_effect=[3, 30, 56])
    def test_max_three(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        max_three()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "The max of the three numbers is: 56")

    def test_between_3_and_9(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        user_input = 2
        between_3_and_9(user_input)
        output = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__
        if user_input in range(3, 9):
            self.assertEqual(output, (f"{user_input} is in the range"))
        else:
            self.assertEqual(output, "The number is outside the given range.")


if __name__ == "__main__":
    unittest.main()
