from collections import Counter
import re

def f_774(word: str) -> list:
    """
    Finds the most common two-letter combination in a given, cleaned word (lowercased and alphabetic characters only) 
    and returns its frequency. The search is case-insensitive and ignores non-alphabetic characters.
    
    Requirements:
    - collections.Counter
    - re
    
    Parameters:
    - word (str): The input string containing the word to analyze. The word should have a length of at least 2 to form pairs.
    
    Returns:
    - list: A list containing a single tuple. The tuple consists of the most frequent two-letter combination (str) 
      and its frequency (int). Returns an empty list if the word has fewer than 2 letters, or after cleaning, 
      the word has fewer than 2 alphabetic characters.
    
    Examples:
    >>> f_774("aaBBcc")
    [('aa', 1)]
    >>> f_774("abc!abc")
    [('ab', 2)]
    >>> f_774("a")
    []
    >>> f_774("abcd")
    [('ab', 1)]
    >>> f_774("a1b2c3")
    [('ab', 1)]
    """
    # Clean the word: lowercase and keep alphabetic characters only
    clean_word = re.sub('[^a-z]', '', word.lower())
    
    if len(clean_word) < 2:
        return []
    
    pairs = [clean_word[i:i+2] for i in range(len(clean_word) - 1)]
    pair_counter = Counter(pairs)
    most_common = pair_counter.most_common(1)
    
    # This check ensures we return the result directly from most_common without additional filtering
    return most_common

import unittest
class TestCases(unittest.TestCase):

    def test_repeating_pairs(self):
        self.assertEqual(f_774("aabbcc"), [('aa', 1)], "Should identify single repeating pair")
        
    def test_mixed_repeating_pairs(self):
        self.assertEqual(f_774("abcabc"), [('ab', 2)], "Should identify most frequent pair in mixed sequence")
        
    def test_single_character(self):
        self.assertEqual(f_774("a"), [], "Should return empty list for single character")
        
    def test_unique_pairs(self):
        self.assertEqual(f_774("abcdef"), [('ab', 1)], "Should handle all unique pairs")
        
    def test_empty_string(self):
        self.assertEqual(f_774(""), [], "Should return empty list for empty string")

    def test_case_insensitive(self):
        # Corrected the expected count to match the correct behavior of the function
        self.assertEqual(f_774("aAaAbbBB"), [('aa', 3)], "Should be case-insensitive")

    def test_ignore_non_alphabetic(self):
        self.assertEqual(f_774("abc123abc!"), [('ab', 2)], "Should ignore non-alphabetic characters")

def run_tests():
    unittest.main(argv=[''], exit=False)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
