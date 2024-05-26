import re
from collections import Counter

def f_264(sentence):
    """
    Count the occurrence of each word in a sentence and return the result as a dictionary.
    This function uses a regular expression to find words and a Counter to count their occurrences.

    Parameters:
    sentence (str): The sentence to count the words in.

    Returns:
    dict: A dictionary where the keys are the words and the values are their counts.

    Requirements:
    - re
    - collections.Counter
    
    Example:
    >>> f_264("apple banana apple orange orange orange")
    {'apple': 2, 'banana': 1, 'orange': 3}
    """


    words = re.findall(r'\b\w+\b', sentence)
    return dict(Counter(words))

import unittest
from faker import Faker

fake = Faker()

class TestCases(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(f_264(""), {})

    def test_single_word(self):
        word = fake.word()
        self.assertEqual(f_264(word)[word], 1)

    def test_multiple_words(self):
        sentence = fake.sentence()
        expected_result = {}
        for word in sentence.split():
            expected_result[word] = expected_result.get(word, 0) + 1
        self.assertEqual(len(f_264(sentence)), len(expected_result))

    def test_case_sensitivity(self):
        sentence = 'Apple apple'
        self.assertEqual(f_264(sentence), {"Apple": 1, "apple": 1})

    def test_punctuation_inclusion(self):
        sentence = 'apple, apple; banana!'
        self.assertEqual(f_264(sentence), {"apple": 2, "banana": 1})

    def test_numeric_and_special_characters(self):
        sentence = '123 $%^& 123'
        self.assertEqual(f_264(sentence), {'123': 2})

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    run_tests()
