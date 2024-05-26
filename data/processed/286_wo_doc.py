import os
import tempfile
import nltk
from collections import Counter


def task_func(directory_path):
    """
    Count the number of unique non-stop words across all '.txt' files in a specified directory. Download the 
    NLTK stopwords corpus to a temporary directory to access the stopwords.

    Parameters:
    directory_path (str): The path to the directory containing '.txt' files.

    Returns:
    int: The total count of unique non-stop words across all files.

    Requirements:
    - collections.Counter
    - os
    - tempfile
    - nltk.corpus.stopwords

    Example:
    >>> task_func('./yourdictfiles/')
    1500
    """
    temp_dir = tempfile.mkdtemp()
    nltk.data.path.append(temp_dir)
    nltk.download('stopwords', download_dir=temp_dir)
    STOPWORDS = set(nltk.corpus.stopwords.words('english'))
    word_counts = Counter()
    for file_name in os.listdir(directory_path):
        if not file_name.endswith('.txt'):
            continue
        with open(os.path.join(directory_path, file_name), 'r') as file:
            words = [word for word in file.read().split() if word.lower() not in STOPWORDS]
            word_counts.update(words)
    return len(word_counts)

import unittest
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_data'
        os.makedirs(self.test_dir, exist_ok=True)
    def tearDown(self):
        for f in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, f))
        os.rmdir(self.test_dir)
    def test_no_text_files(self):
        self.assertEqual(task_func(self.test_dir), 0)
    def test_empty_text_files(self):
        with open(os.path.join(self.test_dir, 'empty.txt'), 'w') as f:
            pass
        self.assertEqual(task_func(self.test_dir), 0)
    def test_files_with_only_stopwords(self):
        with open(os.path.join(self.test_dir, 'stopwords.txt'), 'w') as f:
            f.write('the and or but')
        self.assertEqual(task_func(self.test_dir), 0)
    def test_non_empty_text_files(self):
        with open(os.path.join(self.test_dir, 'sample.txt'), 'w') as f:
            f.write('Hello world! This is a test.')
        self.assertEqual(task_func(self.test_dir), 3)  # 'Hello', 'world', 'This', 'test'
    def test_case_insensitivity(self):
        with open(os.path.join(self.test_dir, 'mixed_case.txt'), 'w') as f:
            f.write('Word word WoRd WORD')
        self.assertEqual(task_func(self.test_dir), 4)  # 'Word' in different cases
