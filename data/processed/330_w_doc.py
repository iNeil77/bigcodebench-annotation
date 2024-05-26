import collections
from queue import PriorityQueue
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(string_length=100):
    """
    Create a random string of a given length from a predefined list of letters and count the frequency 
    of each letter, returning an ordered dictionary sorted by frequency in descending order.

    Parameters:
    - string_length (int, optional): The length of the random string to be generated. Default is 100.

    Returns:
    - collections.OrderedDict: An ordered dictionary where keys are letters and values are 
      their frequencies in the generated string, sorted in descending order of frequency.

    Requirements:
    - collections
    - queue.PriorityQueue
    - random

    Example:
    >>> random.seed(0)
    >>> freq = task_func(50)
    >>> freq  # Example output: OrderedDict([('e', 15), ('a', 12), ('b', 10), ('d', 8), ('c', 5)])
    OrderedDict(...)
    """
    string = ''.join([LETTERS[random.randint(0, len(LETTERS)-1)] for _ in range(string_length)])
    freq = collections.Counter(string)
    pq = PriorityQueue()
    for letter, count in freq.items():
        pq.put((-count, letter))
    sorted_freq = collections.OrderedDict()
    while not pq.empty():
        count, letter = pq.get()
        sorted_freq[letter] = -count
    return sorted_freq

import unittest
import collections
class TestCases(unittest.TestCase):
    def test_default_length(self):
        random.seed(0)
        freq = task_func()
        self.assertIsInstance(freq, collections.OrderedDict, "Output should be an OrderedDict")
        self.assertEqual(sum(freq.values()), 100, "Total count of letters should be 100 for default length")
        self.assertTrue(all(freq[key] >= freq[key2] for key, key2 in zip(list(freq)[:-1], list(freq)[1:])), "Frequencies should be sorted in descending order")
    def test_specific_length(self):
        random.seed(0)
        freq = task_func(50)
        self.assertIsInstance(freq, collections.OrderedDict, "Output should be an OrderedDict")
        self.assertEqual(sum(freq.values()), 50, "Total count of letters should be 50 for specific length")
        self.assertTrue(all(freq[key] >= freq[key2] for key, key2 in zip(list(freq)[:-1], list(freq)[1:])), "Frequencies should be sorted in descending order")
    def test_minimum_length(self):
        random.seed(0)
        freq = task_func(1)
        self.assertIsInstance(freq, collections.OrderedDict, "Output should be an OrderedDict")
        self.assertEqual(sum(freq.values()), 1, "Total count of letters should be 1 for minimum length")
        self.assertEqual(len(freq), 1, "Only one letter should be present for minimum length")
    def test_large_length(self):
        random.seed(0)
        freq = task_func(1000)
        self.assertIsInstance(freq, collections.OrderedDict, "Output should be an OrderedDict")
        self.assertEqual(sum(freq.values()), 1000, "Total count of letters should be 1000 for large length")
        self.assertTrue(all(freq[key] >= freq[key2] for key, key2 in zip(list(freq)[:-1], list(freq)[1:])), "Frequencies should be sorted in descending order")
    def test_zero_length(self):
        random.seed(0)
        freq = task_func(0)
        self.assertIsInstance(freq, collections.OrderedDict, "Output should be an OrderedDict")
        self.assertEqual(sum(freq.values()), 0, "Total count of letters should be 0 for zero length")
        self.assertEqual(len(freq), 0, "No letters should be present for zero length")
