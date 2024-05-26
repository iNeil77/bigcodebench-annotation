import re
from collections import Counter

def f_780(input_str):
    """
    Count the frequency of each alphanumeric character in a given string after removing all non-alphanumeric characters,
    treating uppercase and lowercase letters as the same.

    Requirements:
    - re
    - collections.Counter

    Parameters:
    - input_str (str): The input string containing alphanumeric characters mixed with special characters and/or spaces.

    Returns:
    - dict: A dictionary with characters as keys (all lowercase) and their frequencies in the input string as values.
    
    Examples:
    >>> f_780("Hello, World!")
    Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})
    """
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str).lower()
    freq_dict = Counter(cleaned_str)
    return freq_dict

import unittest
class TestCases(unittest.TestCase):

    def test_only_letters(self):
        # Expected output adjusted for lowercase
        self.assertEqual(f_780("Hello, World!"), {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})

    def test_empty_string(self):
        self.assertEqual(f_780(""), {})

    def test_repeated_numbers(self):
        self.assertEqual(f_780("12345 12345"), {'1': 2, '2': 2, '3': 2, '4': 2, '5': 2})

    def test_mixed_case_letters(self):
        # Expecting all lowercase after adjustment for case insensitivity
        self.assertEqual(f_780("AAaaBBbbCCcc"), {'a': 4, 'b': 4, 'c': 4})

    def test_numbers_only(self):
        self.assertEqual(f_780("111222333444555"), {'1': 3, '2': 3, '3': 3, '4': 3, '5': 3})

    def test_uppercase_only(self):
        # Expecting all lowercase after adjustment for case insensitivity
        self.assertEqual(f_780("AAAABBBBCCCC"), {'a': 4, 'b': 4, 'c': 4})

    def test_no_alphanumeric(self):
        self.assertEqual(f_780("!!!@@@###$$$%%%^^^&&&"), {})

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
