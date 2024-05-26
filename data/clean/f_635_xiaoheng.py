import re
import string

def f_635(content):
    """Count the non-stop words in a sentence without the last word.

    Parameters:
    - content (str): The sentence to count non-stopwords from.

    Returns:
    - count (int): The count of non-stopwords.

    Requirements:
    - re
    - string

    Example:
    >>> f_635('this is an example content')
    1
    """
    STOPWORDS = set([
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
        "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", 
        "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", 
        "theirs", "themselves", "what", "which", "who", "whom", "this", "that", 
        "these", "those", "is", "are", "was", "were", "be", "been", "being", "have", 
        "has", "had", "having", "do", "does", "did", "doing", "an", "the", "and", 
        "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", 
        "for", "with", "about", "against", "between", "into", "through", "during", 
        "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", 
        "on", "off", "over", "under", "again", "further", "then", "once"
    ])

    content = content.split(' ')
    if len(content) > 1:
        content = content[:-1]
    else:
        content = []
    words = [word.strip(string.punctuation).lower() for word in re.split(r'\W+', ' '.join(content)) if word]
    non_stopwords = [word for word in words if word not in STOPWORDS]
    count = len(non_stopwords)

    return count

import unittest

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a mix of stopwords and non-stopwords
        self.assertEqual(f_635('this is an example content'), 1)

    def test_case_2(self):
        # Test with all stopwords except the last word
        self.assertEqual(f_635('this is an the of'), 0)

    def test_case_3(self):
        # Test with no stopwords
        self.assertEqual(f_635('example content programming'), 2)

    def test_case_4(self):
        # Test with punctuation
        self.assertEqual(f_635('example, content; programming, python.'), 3)

    def test_case_5(self):
        # Test with an empty string
        self.assertEqual(f_635(''), 0)

    def test_case_6(self):
        # Test with a single non-stopword
        self.assertEqual(f_635('content'), 0)

    def test_case_7(self):
        # Test with a single stopword
        self.assertEqual(f_635('the'), 0)

    def test_case_8(self):
        # Test with a mix and uppercase letters
        self.assertEqual(f_635('This IS an Example Content'), 1)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()