import sys
import unittest
from io import StringIO
from file_input_and_output import *


class TestExercise05(unittest.TestCase):

    def test_open_file(self):
        filename = "food.txt"
        file = open_file(filename)
        self.assertEqual(file.name, "food.txt")
        file.close()

    def test_append_to_file(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        with open_file("food.txt") as file:
            append_to_file(file, "Rice")
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        expected_output = "Line appended successfully."

        self.assertEqual(output, expected_output)

    def test_print_foods(self):
        filename = "wethinkcode.txt"
        with open_file(filename) as file:
            append_to_file(
                file, "Welcome\nto\nWe\nThink\nCode,\nBootcamp\n2023\n!Welcome\nto\nWe\nThink\nCode,\nBootcamp\n2023\n!Welcome\nto\nWe\nThink\nCode,\nBootcamp\n2023\n!")

        captured_output = StringIO()
        sys.stdout = captured_output
        print_foods(filename)
        output = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__

        self.assertEqual(output, "Code,\nBootcamp\n2023\n!")


if __name__ == "__main__":
    unittest.main()
