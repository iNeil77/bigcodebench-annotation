import string
import random



def task_func(length, random_seed=None):
    """
    Generate a random string of a given length, with each character being either
    a parenthesis (from the set "(){}[]") 
    or a lowercase English character.
    For function uses a optional random_seed when sampling characters.

    Parameters:
    length (int): The length of the string to generate.
    random_seed (int): Random seed for rng. Used in picking random characters.
                       Defaults to None.

    Returns:
    str: The generated string.

    Requirements:
    - string
    - random

    Note: The function uses the internal string constant BRACKETS for 
          definition of the bracket set.

    Example:
    >>> string = task_func(10, random_seed=1)
    >>> print(string)
    ieqh]{[yng
    
    >>> string = task_func(34, random_seed=42)
    >>> print(string)
    hbrpoigf)cbfnobm(o{rak)vrjnvgfygww

    >>> string = task_func(23, random_seed=1)
    >>> print(string)
    ieqh]{[yng]by)a{rogubbb
    """
    random.seed(random_seed)
    BRACKETS = "(){}[]"
    return ''.join(random.choice(string.ascii_lowercase + BRACKETS) for _ in range(length))

import unittest
import string
class TestCases(unittest.TestCase):
    def setUp(self):
        self.BRACKETS = "(){}[]"
        return 
    def test_rng(self):
        # rng reproducability
        res1 = task_func(100, random_seed=42)
        res2 = task_func(100, random_seed=42)
        self.assertEqual(res1, res2)
    def test_case_1(self):
        # Testing with length = 5
        result = task_func(5, random_seed=1)
        self.assertEqual(len(result), 5)
        for char in result:
            self.assertIn(char, string.ascii_lowercase + self.BRACKETS)
    def test_case_2(self):
        # Testing with length = 0 (edge case)
        result = task_func(0, random_seed=2)
        self.assertEqual(len(result), 0)
    def test_case_3(self):
        # Testing with length = 10
        result = task_func(10, random_seed=3)
        self.assertEqual(len(result), 10)
        for char in result:
            self.assertIn(char, string.ascii_lowercase + self.BRACKETS)
    def test_case_4(self):
        # Testing with length = 1 (edge case)
        result = task_func(1, random_seed=34)
        self.assertEqual(len(result), 1)
        self.assertIn(result, string.ascii_lowercase + self.BRACKETS)
    def test_case_5(self):
        # Testing with length = 50
        result = task_func(50, random_seed=777)
        self.assertEqual(len(result), 50)
        for char in result:
            self.assertIn(char, string.ascii_lowercase + self.BRACKETS)
