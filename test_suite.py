#!/usr/bin/python

import sys
from unittest.mock import patch
from io import StringIO
import unittest

import word_count

class TestUM(unittest.TestCase):
    """Test class for word_count.word_counter
    """

    def setUp(self):
        """Runs before each test below.
        """
        pass

    def test_numbers(self):
        """Simple test of four words in small input file, all are 
           common, none are filtered.

        File "test_case_one.txt" is required for input.

        Expected output:
            one - 1
            two - 2
            three - 3                                
            four - 4

        Raises:
            AttributeError:
                FAIL: If assertEqual statements are unequal.
        """

        list_process = test_get_out(json_flag=False,
                                    filename="test_files//test_case_one.txt")


        self.assertEqual(list_process[0], 'one - 1')        
        self.assertEqual(list_process[1], 'two - 2')
        self.assertEqual(list_process[2], 'three - 3')
        self.assertEqual(list_process[3], 'four - 4')

    def test_numbers_json(self):
        """Simple test of four words in small input file with -json
           option.

        File "test_case_one.txt" is required for input.

        Expected output:
            {"one": 1, "two": 2, "three": 3, "four": 4}

        Raises:
            AttributeError:
                FAIL: If assertEqual statements are unequal.
        """

        list_process = test_get_out(json_flag=True,
                                    filename="test_files//test_case_one.txt")

        self.assertEqual(list_process[0],
                         '{"one": 1, "two": 2, "three": 3, "four": 4}')

    def test_apostrophe(self):
        """Simple test of four words with an apostrophe.

        File "test_three_app.txt" is required for input.

        Expected output:
            liu'd - 9

        Raises:
            AttributeError:
                FAIL: If assertEqual statements are unequal.
        """

        list_process = test_get_out(json_flag=False,
                                    filename="test_files//test_three_app.txt")

        self.assertEqual(list_process[0], "liu'd - 9")        


    def test_apostrophe_json(self):
        """Simple test of four words with an apostrophe.

        File "test_three_app.txt" is required for input.

        Expected output:
            {"liu'd": 9}

        Raises:
            AttributeError:
                FAIL: If assertEqual statements are unequal.
        """

        list_process = test_get_out(json_flag=True,
                                    filename="test_files//test_three_app.txt")

        self.assertEqual(list_process[0], "{\"liu'd\": 9}")        

    def test_500_numbers(self):
        """Test of 500ish words. None should be filtered.

        File "test_case_one.txt" is required for input.

        Expected output:
            got - 1
            oneone - 507

        Raises:
            AttributeError:
                FAIL: If assertEqual statements are unequal.
        """

        list_process = test_get_out(json_flag=False,
                                    filename="test_files//test_one_in_500ish.txt")

        self.assertEqual(list_process[0], 'got - 1')
        self.assertEqual(list_process[1], 'oneone - 507')

    def test_500_numbers_json(self):
        """Test of 500ish words. None should be filtered

        File "test_case_one.txt" is required for input.

        Expected output:
            {"got": 1, "oneone": 507}

        Raises:
            AttributeError:
                FAIL: If assertEqual statements are unequal.
        """

        list_process = test_get_out(json_flag=True,
                                    filename="test_files//test_one_in_500ish.txt")

        self.assertEqual(list_process[0],
                         '{"got": 1, "oneone": 507}')

    def test_1k_numbers(self):
        """Test of 1kish words. The word "ignore" should be filtered.

        File "test_one_in_1kish.txt" is required for input.

        Expected output:
            oneone - 1014

        Raises:
            AttributeError:
                FAIL: If assertEqual statements are unequal.
        """

        list_process = test_get_out(json_flag=False,
                                    filename="test_files//test_one_in_1kish.txt")

        self.assertEqual(list_process[0], 'oneone - 1014')

    def test_1k_numbers_json(self):
        """Test of 1kish words. None should be filtered.

        File "test_one_in_1kish.txt" is required for input.

        Expected output:
            {"ignore": 1, "oneone": 1014}

        Raises:
            AttributeError:
                FAIL: If assertEqual statements are unequal.
        """

        list_process = test_get_out(json_flag=True,
                                    filename="test_files//test_one_in_1kish.txt")

        self.assertEqual(list_process[0], '{"ignore": 1, "oneone": 1014}')

    def test_500_numbers_json(self):
        """Test of 500ish words. None should be filtered

        File "test_case_one.txt" is required for input.

        Expected output:
            {"got": 1, "oneone": 507}

        Raises:
            AttributeError:
                FAIL: If assertEqual statements are unequal.
        """

        list_process = test_get_out(json_flag=True,
                                    filename="test_files//test_one_in_500ish.txt")
        self.assertEqual(list_process[0],
                         '{"got": 1, "oneone": 507}')

    def test_empty(self):
        """Simple test of empty file.

        File "test_case_empty.txt" is required for input.

        Expected output:

        Raises:
            AttributeError:
                FAIL: If assertEqual statements are unequal.
        """

        list_process = test_get_out(json_flag=False,
                                    filename="test_files//test_case_empty.txt")

        self.assertEqual(len(list_process), 1)

    def test_json(self):
        self.assertEqual(12, 12)


def test_get_out(json_flag, filename):
    """Returns list of stdout lines of call of word_count.word_counter.

    Expected output:
        List of stdout lines of call to word_count.word_counter.

    Args:
        json_flag (string): If the first argument is "-json" then the
        output will be a single string of a json list of the words and
        their frequency. If "-json" is NOT set then the otuput will be
        repeated lines of, e.g.,  "bleed - 1".

        filename (string): The name of the UTF-8 encoded text file to
            parse.

    Returns:
        list_process (list of strings): List of stdout lines of
            word_count.word_counter
    """

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    out = word_count.word_counter(json_flag=json_flag, filename=filename)

    sys.stdout = old_stdout

    process = mystdout.getvalue()

    list_process = process.split('\n')

    return list_process

if __name__ == '__main__':
    unittest.main()
