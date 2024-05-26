import string
import re


def f_800(text: str) -> tuple:
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
    >>> f_800('Hello, world!')
    (2, 10, 7)
    >>> f_800('Python is  awesome!  ')
    (3, 15, 12)
    """
    words = text.split()
    chars = re.sub("\s", "", re.sub(f"[{string.punctuation}]", "", text))

    return len(words), len(chars), len(set(chars))


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test simple text without any punctuation.
        result = f_800("Hello world")
        self.assertEqual(result, (2, 10, 7))

    def test_case_2(self):
        # Test simple text that includes punctuation.
        result = f_800("Hello, world!")
        self.assertEqual(result, (2, 10, 7))

    def test_case_3(self):
        # Test single word and no punctuation.
        result = f_800("Hello")
        self.assertEqual(result, (1, 5, 4))

    def test_case_4(self):
        # Test single word that includes punctuation.
        result = f_800("Hello!")
        self.assertEqual(result, (1, 5, 4))

    def test_case_5(self):
        # Test empty string.
        result = f_800("")
        self.assertEqual(result, (0, 0, 0))

    def test_case_6(self):
        # Test text with numbers and punctuation.
        result = f_800("There are 4 numbers here: 1, 2, 3, and 4.")
        self.assertEqual(result, (10, 27, 15))

    def test_case_7(self):
        # Test text with only whitespace and punctuation.
        result = f_800("     , , !")
        self.assertEqual(result, (3, 0, 0))

    def test_case_8(self):
        # Test text with multiple spaces between words.
        result = f_800("Multiple    spaces    here")
        self.assertEqual(result, (3, 18, 12))

    def test_case_9(self):
        # Test a long text.
        long_text = "This is a longer text designed to test the function's ability to handle more complex input, including a variety of characters and spaces."
        result = f_800(long_text)
        self.assertEqual(result, (23, 112, 22))


if __name__ == "__main__":
    run_tests()
