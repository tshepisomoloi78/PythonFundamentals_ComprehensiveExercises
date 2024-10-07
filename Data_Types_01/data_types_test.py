import unittest
from unittest.mock import patch
import sys
from io import StringIO
from data_types import *


class TestExercise01(unittest.TestCase):

    def test_boolean(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        boolean()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), 'True')

    @patch('builtins.input', side_effect=[4, 3])
    def test_integer(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        integer()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(),
                         'The product is 12')

    def test_string(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        string()
        sys.stdout = sys.__stdout__
        name = captured_output.getvalue().strip()
        self.assertNotEqual(name, "")

    def test_float(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        convert_to_float()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), '60.0')

    def test_all_data_types(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        all_data_types()
        sentence = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            sentence, "Welcome to the 2023 WeThinkCode_ bootcamp where True learning costs R0.00")


if __name__ == "__main__":
    unittest.main()
