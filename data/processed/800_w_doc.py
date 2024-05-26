import re
from collections import Counter


def task_func(text, stopwords, n=2):
    """
    Remove duplicate and stopwords from a string "text" and a set of stopwords.
    Then, generate a count of n-grams (default is bigrams) in the text.

    Parameters:
    - text (str): The text string to analyze.
    - stopwords (set): A set of stopwords to exclude from the n-grams.
    - n (int): The size of the n-grams.

    Returns:
    - dict: The count of the n-grams in the text.

    Requirements:
    - re
    - collections.Counter

    Example:
    >>> text = "The quick brown fox jumps over the lazy dog and the dog was not that quick to respond."
    >>> ngrams = task_func(text, ['the', 'and', 'to', 'that', 'over', 'was', 'not'], n=2)
    >>> print(ngrams)
    Counter({('quick', 'brown'): 1, ('brown', 'fox'): 1, ('fox', 'jumps'): 1, ('jumps', 'lazy'): 1, ('lazy', 'dog'): 1, ('dog', 'dog'): 1, ('dog', 'quick'): 1, ('quick', 'respond'): 1})
    """
    text = re.sub(r'[^\w\s]', '', text)  # Remove all punctuation
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    words = [word.lower() for word in text.split() if word.lower() not in stopwords]
    ngrams = zip(*[words[i:] for i in range(n)])
    return Counter(ngrams)

import unittest
from collections import Counter
import nltk
import tempfile
temp_dir = tempfile.mkdtemp()
nltk.data.path.append(temp_dir)
nltk.download('stopwords', download_dir=temp_dir)
# Constants
STOPWORDS = set(nltk.corpus.stopwords.words('english'))
class TestCases(unittest.TestCase):
    def test_case_1(self):
        """
        Test Case 1: Simple Text
        - Input: A simple text string with no duplicated words or stopwords
        - Expected Output: A Counter object with the count of each bigram
        """
        text = "The quick brown fox jumps over the lazy dog."
        result = task_func(text, STOPWORDS)
        expected = Counter({('quick', 'brown'): 1, ('brown', 'fox'): 1, ('fox', 'jumps'): 1, ('jumps', 'lazy'): 1, ('lazy', 'dog'): 1})
        self.assertEqual(result, expected)
    def test_case_2(self):
        """
        Test Case 2: Text with Duplicated Words
        - Input: A text string with duplicated consecutive words
        - Expected Output: A Counter object with the count of each bigram, excluding duplicated words
        """
        text = "This is is a simple simple test test."
        result = task_func(text, STOPWORDS)
        expected = Counter({('simple', 'simple'): 1, ('simple', 'test'): 1, ('test', 'test'): 1})
        self.assertEqual(result, expected)
    def test_case_3(self):
        """
        Test Case 3: Text with Stopwords
        - Input: A text string with common English stopwords
        - Expected Output: A Counter object with the count of each bigram, excluding stopwords
        """
        text = "This is a test of the function."
        result = task_func(text, STOPWORDS)
        expected = Counter({('test', 'function'): 1})
        self.assertEqual(result, expected)
    def test_case_4(self):
        # This test involves punctuation; ensure punctuation handling is consistent with function logic
        text = "Hello, world!"
        result = task_func(text, STOPWORDS)
        expected = Counter({
            ('hello', 'world'): 1
        })
        self.assertEqual(result, expected)
    def test_case_5(self):
        """
        Test Case 5: Empty Text
        - Input: An empty text string
        - Expected Output: An empty Counter object
        """
        text = ""
        result = task_func(text, STOPWORDS)
        expected = Counter()
        self.assertEqual(result, expected)
