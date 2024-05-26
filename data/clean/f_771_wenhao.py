import numpy as np
from scipy import stats
def f_771(word: str) -> np.ndarray:
    """
    Calculate the difference between the ASCII values of each pair of adjacent letters in the input word.
    After calculating the difference, calculate the entropy of the differences.
    
    Requirements:
    - numpy
    - scipy.stats
    
    Parameters:
    - word (str): The input word as a string.
    
    Returns:
    - np.ndarray: A numpy array containing the difference between the ASCII values of each pair of adjacent letters in the word.
    - float: The entropy of the differences.
    
    Examples:
    >>> f_771('abcdef')
    (array([1, 1, 1, 1, 1]), 1.6094379124341005)
    >>> f_771('hello')
    (array([-3,  7,  0,  3]), -inf)
    """
    if not word:  # Handling the case for empty string
        return np.array([])
    word_ascii_values = np.array([ord(x) for x in word])
    difference = np.diff(word_ascii_values)
    entropy = stats.entropy(difference)
    
    return difference, entropy

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_771('abcdef')
        expected_diff = np.array([1, 1, 1, 1, 1])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], 1.6094379124341005)
        
    def test_case_2(self):
        result = f_771('hell')
        expected_diff = np.array([-3, 7, 0])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], -np.inf)
        
    def test_case_3(self):
        result = f_771('az')
        expected_diff = np.array([25])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], 0.0)
        
    def test_case_4(self):
        result = f_771('a')
        expected_diff = np.array([])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], 0.0)
        
    def test_case_5(self):
        result = f_771('i love Python')
        expected_diff = np.array([-73,  76,   3,   7, -17, -69,  48,  41,  -5, -12,   7,  -1])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], -np.inf)
        
    def test_case_6(self):
        result = f_771('Za')
        expected_diff = np.array([7])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], 0.0)

    def test_case_7(self):
        result = f_771('racecar')
        expected_diff = np.array([-17, 2, 2, -2, -2, 17])
        np.testing.assert_array_equal(result[0], expected_diff)
        self.assertEqual(result[1], -np.inf)

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
