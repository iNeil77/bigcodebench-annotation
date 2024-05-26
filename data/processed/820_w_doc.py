import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    """
    Count the number of words and punctuation marks in a string.

    Parameters:
    - text (str): The input string.

    Returns:
    - tuple: A tuple containing the number of words and punctuation marks.

    Requirements:
    - re
    - string

    Example:
    >>> task_func("Hello, world! This is a test.")
    (6, 3)
    """
    words = re.findall(r'\b\w+\b', text)
    punctuation_marks = [char for char in text if char in PUNCTUATION]
    return len(words), len(punctuation_marks)

import unittest
class TestCases(unittest.TestCase):
    def test_basic_input(self):
        """Test with basic input string"""
        result = task_func("Hello, world! This is a test.")
        self.assertEqual(result, (6, 3))
    def test_no_punctuation(self):
        """Test with a string that has words but no punctuation"""
        result = task_func("No punctuation here just words")
        self.assertEqual(result, (5, 0))
    
    def test_with_empty_string(self):
        """Test with an empty string"""
        result = task_func("")
        self.assertEqual(result, (0, 0))
    def test_with_multiple_spaces(self):
        """Test with a string that has multiple spaces between words"""
        result = task_func("This  is   a    test     with      multiple       spaces")
        self.assertEqual(result, (7, 0))
    def test_with_only_punctuation(self):
        """Test with a string that consists only of punctuation marks"""
        result = task_func("!!!")
        self.assertEqual(result, (0, 3))
    
    def test_with_single_punctuation(self):
        """Test with a string that is a single punctuation mark"""
        result = task_func("!")
        self.assertEqual(result, (0, 1))
