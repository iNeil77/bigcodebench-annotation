import re
import tempfile
import nltk
from textblob import TextBlob

temp_dir = tempfile.mkdtemp()
nltk.data.path.append(temp_dir)
nltk.download('stopwords')

from nltk.corpus import stopwords


# Constants
STOPWORDS = set(stopwords.words('english'))

def f_677(text):
    """
    Remove duplicate and stopwords from a string "text."
    Then, analyze the sentiment of the text using TextBlob.
    Use nltk.corpus.stopwords to remove stopwords from the text
    by downloading the stopwords list to a temporary directory.

    Parameters:
    - text (str): The text string to analyze.

    Returns:
    - Sentiment: The sentiment of the text.

    Requirements:
    - re
    - tempfile
    - nltk.corpus.stopwords
    - textblob.TextBlob

    Example:
    >>> text = "The quick brown fox jumps over the lazy dog and the dog was not that quick to respond."
    >>> sentiment = f_677(text)
    >>> print(sentiment)
    Sentiment(polarity=0.13888888888888887, subjectivity=0.6666666666666666)
    """
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
    words = [word for word in re.findall(r'\b\w+\b', text.lower()) if word not in STOPWORDS]
    text = ' '.join(words)
    blob = TextBlob(text)
    
    return blob.sentiment

import unittest

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test Case 1: Regular Sentence
        # Description: This test case checks the function's behavior with a regular sentence containing duplicate words
        # and stopwords. The function should remove the duplicate words and stopwords, and return the sentiment analysis
        # result as a tuple of two float values.
        text = "The quick brown fox jumps over the lazy dog and the dog was not quick."
        sentiment = f_677(text)
        self.assertIsInstance(sentiment, tuple, "The function should return a tuple")
        self.assertEqual(len(sentiment), 2, "The tuple should contain two elements")
        self.assertIsInstance(sentiment[0], float, "The polarity should be a float")
        self.assertIsInstance(sentiment[1], float, "The subjectivity should be a float")

    def test_case_2(self):
        # Test Case 2: Empty String
        # Description: This test case checks the function's behavior with an empty string. The function should return
        # (0.0, 0.0) as the sentiment of an empty string is neutral.
        text = ""
        sentiment = f_677(text)
        self.assertEqual(sentiment, (0.0, 0.0), "The sentiment of an empty string should be (0.0, 0.0)")

    def test_case_3(self):
        # Test Case 3: Positive Sentiment
        # Description: This test case checks the function's behavior with a sentence that has a positive sentiment.
        # The function should return a positive polarity value.
        text = "I absolutely love this! It's amazing."
        sentiment = f_677(text)
        self.assertGreater(sentiment[0], 0, "The polarity of a positive sentiment sentence should be greater than 0")

    def test_case_4(self):
        # Test Case 4: Negative Sentiment
        # Description: This test case checks the function's behavior with a sentence that has a negative sentiment.
        # The function should return a negative polarity value.
        text = "This is really bad. I hate it."
        sentiment = f_677(text)
        self.assertLess(sentiment[0], 0, "The polarity of a negative sentiment sentence should be less than 0")

    def test_case_5(self):
        # Test Case 5: Neutral Sentiment
        # Description: This test case checks the function's behavior with a sentence that has a neutral sentiment.
        # The function should return a zero polarity value.
        text = "This is a pen."
        sentiment = f_677(text)
        self.assertEqual(sentiment[0], 0, "The polarity of a neutral sentiment sentence should be 0")

# Running the tests
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()