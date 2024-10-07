import unittest
import sys
from io import StringIO
from more_data_structures import *


class TestExercise06(unittest.TestCase):

    def test_print_set(self):
        bool_output = None
        captured_output = StringIO()
        sys.stdout = captured_output
        print_set()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        convert_output = eval(output)
        expected_output = {'Siyamthanda', 7, 'Tshepo', 9, 'Respect', 
                           'Simphiwe', 'Khomotso', 'Khensani', 'Nkululeko', 'Ayanda', 23}

        for x in convert_output:
            if x in expected_output:
                bool_output = True
            else:
                bool_output = None
                break

        self.assertTrue(
            bool_output, (f"\n{expected_output} != {convert_output}"))

    def test_remove_yankho(self):
        bool_output = None
        captured_output = StringIO()
        sys.stdout = captured_output
        remove_yankho()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        convert_output = eval(output)
        expected_output = {'Ayanda', 'Tshepo', 'Respect', 'Khensani', 
                           'Simphiwe', 7, 'Siyamthanda', 9, 23, 'Khomotso'}

        for x in convert_output:
            if x in expected_output:
                bool_output = True
            else:
                bool_output = None
                break

        self.assertTrue(
            bool_output, (f"\n{expected_output} != {convert_output}"))

    def test_add_names(self):
        bool_output = None
        captured_output = StringIO()
        sys.stdout = captured_output
        add_names()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        convert_output = eval(output)
        expected_output = {'Respect', 'Simphiwe', 'Khomotso', 7, 9, 
                           'Khensani', 'Ayanda', 'Loveness', 'Tshepo', 23, 'Nkululeko', 'Siyamthanda', 'Onalerona'}

        for x in convert_output:
            if x in expected_output:
                bool_output = True
            else:
                bool_output = None
                break

        self.assertTrue(
            bool_output, (f"\n{expected_output} != {convert_output}"))

    def test_difference(self):
        bool_output = None
        captured_output = StringIO()
        sys.stdout = captured_output
        difference()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        convert_output = eval(output)
        expected_output = {'Respect', 'Nkululeko', 'Siyamthanda', 'Tshepo', 'Khomotso'}

        for x in convert_output:
            if x in expected_output:
                bool_output = True
            else:
                bool_output = None
                break

        self.assertTrue(
            bool_output, (f"\n{expected_output} != {convert_output}"))


if __name__ == "__main__":
    unittest.main()
