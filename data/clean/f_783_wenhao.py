import re
from nltk import word_tokenize
from collections import Counter

def f_783(input_str):
    """
    Remove all special characters, punctuation marks and spaces from a string called "input _ str" using regex and then count the frequency of each word.

    Parameters:
    input_str (str): The input string.

    Returns:
    dict: A dictionary with the frequency of each word.

    Requirements:
    - re
    - nltk.word_tokenize
    - collections.Counter

    Example:
    >>> f_783('Special $#! characters   spaces 888323')
    Counter({'Special': 1, 'characters': 1, 'spaces': 1, '888323': 1})
    """
    cleaned_str = re.sub('[^A-Za-z0-9 ]+', '', input_str)
    words = word_tokenize(cleaned_str)
    freq_dict = Counter(words)

    return freq_dict
    

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_783('Special $#! characters   spaces 888323')
        expected = {'Special': 1, 'characters': 1, 'spaces': 1, '888323': 1}
        self.assertEqual(result, expected)

    def test_case_2(self):
        result = f_783('Hello hello world')
        expected = {'Hello': 1, 'hello': 1, 'world': 1}
        self.assertEqual(result, expected)

    def test_case_3(self):
        result = f_783('')
        expected = {}
        self.assertEqual(result, expected)

    def test_case_4(self):
        result = f_783('123 123 456')
        expected = {'123': 2, '456': 1}
        self.assertEqual(result, expected)

    def test_case_5(self):
        result = f_783('Hello123 #$! 123')
        expected = {'Hello123': 1, '123': 1}
        self.assertEqual(result, expected)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()