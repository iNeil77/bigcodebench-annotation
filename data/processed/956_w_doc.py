import string
import random


def task_func(text, seed=None):
    """
    Generates a password that mirrors the structure of the given text by replacing alphabetic
    characters with random ascii lowercase letters, digits with random single-digit numbers,
    spaces wth either a random digit or random lowercase letter at equal probabilities, and
    leaving other characters unchanged.

    Parameters:
    - text (str): The text to be mirrored in the generated password. Must not be empty.
    - seed (int, optional): Seed for the random number generator. Defaults to None (not set).

    Returns:
    - str: The generated password.

    Raises:
    - ValueError: If the input text is empty.

    Requirements:
    - random
    - string

    Note:
    - This function does not handle high Unicode characters and focuses only on ASCII values.

    Examples:
    >>> task_func("hello world! 123", 0)
    'mbqmp3jytre!v553'
    >>> task_func("apple321#", seed=42)
    'uahev901#'
    """
    if seed is not None:
        random.seed(seed)
    if not text:
        raise ValueError("text cannot be empty.")
    password = ""
    for char in text:
        random_lowercase = random.choice(string.ascii_lowercase)
        random_digit = random.choice(string.digits)
        if char.isalpha():
            password += random_lowercase
        elif char.isdigit():
            password += random_digit
        elif char == " ":
            if random.random() < 0.5:
                password += random_lowercase
            else:
                password += random_digit
        else:
            password += char
    return password

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case
        result = task_func("Hello123", seed=1)
        self.assertEqual(len(result), 8)
        for i, char in enumerate("Hello123"):
            if char.isalpha():
                self.assertTrue(result[i].isalpha())
            elif char.isdigit():
                self.assertTrue(result[i].isdigit())
    def test_case_2(self):
        # Test basic case with alphabet only
        result = task_func("ABC", seed=2)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(char.isalpha() for char in result))
    def test_case_3(self):
        # Test basic case with digit only
        result = task_func("123", seed=3)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(char.isdigit() for char in result))
    def test_case_4(self):
        # Test basic case with whitespace, alphabet, number, special char
        text = "Hello, world!"
        result = task_func(text, seed=4)
        self.assertEqual(len(result), 13)
        for i, char in enumerate(text):
            result_char = result[i]
            if char.isalpha():
                self.assertTrue(result_char.isalpha())
            elif char.isdigit():
                self.assertTrue(result_char.isdigit())
            elif char == " ":
                self.assertTrue(result_char.isalnum())
            else:
                self.assertEqual(result[i], char)
    def test_case_5(self):
        # Test handling empty string
        with self.assertRaises(Exception):
            task_func("", seed=5)
