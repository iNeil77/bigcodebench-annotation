from collections import defaultdict
import re

def f_773(word: str) -> dict:
    """
    Find the occurrences of each two-letter combination in the sanitized word,
    where only alphabetic characters are considered.

    Requirements:
    - collections.defaultdict
    - re
    
    Parameters:
    word (str): The input string.

    Returns:
    collections.defaultdict: A dictionary with keys as two-letter combinations and values as their counts in the sanitized word.

    Example:
    >>> f_773('abcdef')
    defaultdict(<class 'int'>, {'ab': 1, 'bc': 1, 'cd': 1, 'de': 1, 'ef': 1})
    >>> f_773('aabbcc')
    defaultdict(<class 'int'>, {'aa': 1, 'ab': 1, 'bb': 1, 'bc': 1, 'cc': 1})
    >>> f_773('a1!b@c#d$')
    defaultdict(<class 'int'>, {'ab': 1, 'bc': 1, 'cd': 1})
    """
    # Sanitize the word to include only alphabetic characters
    sanitized_word = re.sub('[^A-Za-z]', '', word)
    occurrences = defaultdict(int)
    pairs = [''.join(x) for x in zip(sanitized_word, sanitized_word[1:])]

    for pair in pairs:
        occurrences[pair] += 1

    return occurrences

import unittest
class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = f_773('abcdef')
        expected = {'ab': 1, 'bc': 1, 'cd': 1, 'de': 1, 'ef': 1}
        self.assertEqual(result, expected)

    def test_case_2(self):
        result = f_773('aabbcc')
        expected = {'aa': 1, 'ab': 1, 'bb': 1, 'bc': 1, 'cc': 1}
        self.assertEqual(result, expected)

    def test_case_3(self):
        result = f_773('a')
        expected = {}
        self.assertEqual(result, expected)

    def test_case_4(self):
        result = f_773('')
        expected = {}
        self.assertEqual(result, expected)

    def test_case_5(self):
        result = f_773('AbCd')
        expected = {'Ab': 1, 'bC': 1, 'Cd': 1}
        self.assertEqual(result, expected)

    def test_case_6(self):
        # Test with non-alphabetic characters in the word
        result = f_773('a1!b@c#d$')
        expected = {'ab': 1, 'bc': 1, 'cd': 1}
        self.assertEqual(result, expected)

    def test_case_7(self):
        # Test with mixed case and non-alphabetic characters
        result = f_773('AaBb!!Cc123')
        expected = {'Aa': 1, 'aB': 1, 'Bb': 1, 'bC': 1, 'Cc': 1}
        self.assertEqual(result, expected)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
