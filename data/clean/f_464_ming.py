import numpy as np
import pandas as pd

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'


def f_464(file_path, output_dir=OUTPUT_DIR):
    """
    Create a CSV file containing a 2D matrix populated exclusively with random lowercase letters.
    
    Parameters:
    - file_path (str): The path of the CSV file to be created.
    - output_dir (str, optional): The dir of the CSV file to be created.
    
    Returns:
    None: Writes a CSV file to the specified path.
    
    Requirements:
    - pandas
    - numpy

    Example:
    >>> f_464(os.path.join(OUTPUT_DIR, 'random_matrix.csv'))
    """
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    matrix = pd.DataFrame(np.random.choice(LETTERS, (10, 10)))
    matrix.to_csv(file_path, sep='\t', header=False, index=False)

    return None


import unittest
import shutil
import os


class TestCases(unittest.TestCase):

    def setUp(self):
        if not os.path.exists(OUTPUT_DIR):
            os.mkdir(OUTPUT_DIR)

    def tearDown(self):
        """Clean up any files created during the tests."""
        # Check and remove the expected file if it exists
        # if os.path.exists(FILE_PATH):
        #     os.remove(FILE_PATH)
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)

    def test_case_1(self):
        # Testing with a sample file path
        file_path = os.path.join(OUTPUT_DIR, 'test_output_1.csv')
        f_464(file_path)
        df = pd.read_csv(file_path, sep='\t', header=None)
        self.assertEqual(df.shape, (10, 10), "Matrix shape should be 10x10")

    def test_case_2(self):
        # Testing if the generated matrix contains only lowercase letters
        file_path = os.path.join(OUTPUT_DIR, 'test_output_2.csv')
        f_464(file_path)
        df = pd.read_csv(file_path, sep='\t', header=None)
        all_lower = df.applymap(str.islower).all().all()
        self.assertTrue(all_lower, "All elements should be lowercase letters")

    def test_case_3(self):
        # Testing if the generated matrix contains only letters from the alphabet
        file_path = os.path.join(OUTPUT_DIR, 'test_output_3.csv')
        f_464(file_path)
        df = pd.read_csv(file_path, sep='\t', header=None)
        all_alpha = df.applymap(str.isalpha).all().all()
        self.assertTrue(all_alpha, "All elements should be alphabetic")

    def test_case_4(self):
        # Testing if the generated matrix contains different letters
        file_path = os.path.join(OUTPUT_DIR, 'test_output_4.csv')
        f_464(file_path)
        df = pd.read_csv(file_path, sep='\t', header=None)
        unique_elements = df.nunique().sum()
        self.assertTrue(unique_elements > 10, "Matrix should have more than 10 unique elements")

    def test_case_5(self):
        # Testing if the function overwrites existing files
        file_path = os.path.join(OUTPUT_DIR, 'test_output_5.csv')
        with open(file_path, 'w') as f:
            f.write("test")
        f_464(file_path)
        with open(file_path, 'r') as f:
            content = f.read()
        self.assertNotEqual(content, "test", "Function should overwrite existing content")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()