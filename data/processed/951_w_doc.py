import string
import re


def task_func(text: str) -> tuple:
    """
    Counts the number of words, characters, and unique characters in a given text.

    Parameters:
    - text (str): The input text to be analyzed.

    Returns:
    - tuple: A tuple containing three integers: the number of words,
                                                the number of characters,
                                                the number of unique characters.

    Requirements:
    - string
    - re

    Note:
    - This function considers whitespace-separated substrings as words.
    - When counting characters, this function excludes whitespace and special
      characters (i.e. string.punctuation).

    Example:
    >>> task_func('Hello, world!')
    (2, 10, 7)
    >>> task_func('Python is  awesome!  ')
    (3, 15, 12)
    """
    words = text.split()
    chars = re.sub("\s", "", re.sub(f"[{string.punctuation}]", "", text))
    return len(words), len(chars), len(set(chars))

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test simple text without any punctuation.
        result = task_func("Hello world")
        self.assertEqual(result, (2, 10, 7))
    def test_case_2(self):
        # Test simple text that includes punctuation.
        result = task_func("Hello, world!")
        self.assertEqual(result, (2, 10, 7))
    def test_case_3(self):
        # Test single word and no punctuation.
        result = task_func("Hello")
        self.assertEqual(result, (1, 5, 4))
    def test_case_4(self):
        # Test single word that includes punctuation.
        result = task_func("Hello!")
        self.assertEqual(result, (1, 5, 4))
    def test_case_5(self):
        # Test empty string.
        result = task_func("")
        self.assertEqual(result, (0, 0, 0))
    def test_case_6(self):
        # Test text with numbers and punctuation.
        result = task_func("There are 4 numbers here: 1, 2, 3, and 4.")
        self.assertEqual(result, (10, 27, 15))
    def test_case_7(self):
        # Test text with only whitespace and punctuation.
        result = task_func("     , , !")
        self.assertEqual(result, (3, 0, 0))
    def test_case_8(self):
        # Test text with multiple spaces between words.
        result = task_func("Multiple    spaces    here")
        self.assertEqual(result, (3, 18, 12))
    def test_case_9(self):
        # Test a long text.
        long_text = "This is a longer text designed to test the function's ability to handle more complex input, including a variety of characters and spaces."
        result = task_func(long_text)
        self.assertEqual(result, (23, 112, 22))
