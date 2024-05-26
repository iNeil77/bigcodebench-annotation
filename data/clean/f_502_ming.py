import os
import re
import pandas as pd


def f_502(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    """
    Searches for files in the specified directory that match a given regex pattern.
    This function walks through the directory, matches filenames against the pattern,
    and saves the matched file paths to a CSV file. It returns a DataFrame of these paths
    with colomn 'File Path'.

    Parameters:
    - pattern (str): Regex pattern to match filenames.
    - directory (str): Directory to search for files.
    - output_csv (str): CSV file path to save matched file paths.

    Returns:
    - pd.DataFrame: DataFrame with a single column 'File Path' of matched paths.

    Requirements:
    - re
    - pandas
    - os

    Example:
    >>> df = f_502(".*\.txt$", "/path/to/search", "matched_files.csv")
    """
    matched_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if re.match(pattern, file):
                matched_paths.append(os.path.join(root, file))

    df = pd.DataFrame(matched_paths, columns=['File Path'])
    df.to_csv(output_csv, index=False)

    return df


import unittest
import shutil

OUTPUT_DIR = './output'


class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = OUTPUT_DIR
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)

        # Create test files
        self.test_file1 = os.path.join(self.test_dir, "test1.txt")
        self.test_file2 = os.path.join(self.test_dir, "ignore.exe")
        with open(self.test_file1, 'w') as f:
            f.write("This is a test file.")
        with open(self.test_file2, 'w') as f:
            f.write("This file should be ignored.")

    def tearDown(self):
        # Remove the test directory and all its contents
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_file_matching(self):
        """Ensure function matches correct files."""
        output_csv = os.path.join(self.test_dir, "matched_files.csv")
        df = f_502(r".*\.txt$", self.test_dir, output_csv)
        self.assertTrue(os.path.exists(output_csv))
        self.assertIn(self.test_file1, df['File Path'].values)

    def test_no_files_matched(self):
        """Test when no files match the pattern."""
        output_csv = os.path.join(self.test_dir, "no_match.csv")
        df = f_502(r".*\.md$", self.test_dir, output_csv)
        self.assertTrue(df.empty)

    def test_output_file_creation(self):
        """Ensure the output file is created."""
        output_csv = os.path.join(self.test_dir, "output_creation.csv")
        _ = f_502(r".*\.txt$", self.test_dir, output_csv)
        self.assertTrue(os.path.exists(output_csv))

    def test_correct_number_of_matches(self):
        """Test the number of files matched is correct."""
        output_csv = os.path.join(self.test_dir, "correct_number.csv")
        df = f_502(r".*\.txt$", self.test_dir, output_csv)
        self.assertEqual(len(df), 1)

    def test_pattern_specificity(self):
        """Ensure the regex pattern correctly distinguishes file types."""
        output_csv = os.path.join(self.test_dir, "pattern_specificity.csv")
        df = f_502(r"test1\.txt$", self.test_dir, output_csv)
        self.assertEqual(len(df), 1)
        self.assertIn("test1.txt", df['File Path'].values[0])


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()