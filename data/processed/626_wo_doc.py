import pandas as pd
import time
OUTPUT_DIR = './output'


def task_func(df: pd.DataFrame, filename: str) -> str:
    """
    Write a Pandas DataFrame into a JSON Lines file and save it in a specified directory.

    Parameters:
    - df (pd.DataFrame): A Pandas DataFrame to be saved.
    - filename (str): The filename of the JSON Lines file to be saved.

    Returns:
    - str: The full path where the JSON Lines file was saved.

    Requirements:
    - pandas
    - time

    Example:
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    >>> 'data.jsonl' in task_func(df, 'data.jsonl')
    True
    """
    start_time = time.time()
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    file_path = os.path.join(OUTPUT_DIR, filename)
    with open(file_path, 'w') as file:
        for record in df.to_dict(orient='records'):
            json.dump(record, file)
            file.write('\n')
    end_time = time.time()  # End timing
    cost = f"Operation completed in {end_time - start_time} seconds."
    return os.path.abspath(file_path)

import unittest
import pandas as pd
import os
import json
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        """Create the data directory if it doesn't exist."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    def tearDown(self):
        """Clean up by removing the data directory and its contents after tests."""
        shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    def test_basic_dataframe(self):
        """Ensure basic DataFrame is saved correctly."""
        df = pd.DataFrame({'A': [1, 2], 'B': ['x', 'y']})
        path = task_func(df, 'test_basic.jsonl')
        self.assertTrue(os.path.exists(path))
    def test_empty_dataframe(self):
        """Ensure method handles empty DataFrame correctly."""
        df = pd.DataFrame()
        path = task_func(df, 'test_empty.jsonl')
        self.assertTrue(os.path.exists(path))
    def test_with_nan_values(self):
        """Ensure NaN values are handled correctly."""
        df = pd.DataFrame({'A': [1, None], 'B': [None, 2]})
        path = task_func(df, 'test_nan.jsonl')
        self.assertTrue(os.path.exists(path))
    def test_large_dataframe(self):
        """Test with a large DataFrame."""
        df = pd.DataFrame({'A': range(1000)})
        path = task_func(df, 'test_large.jsonl')
        self.assertTrue(os.path.exists(path))
    def test_special_characters(self):
        """Test DataFrame containing special characters."""
        df = pd.DataFrame({'A': ['Hello, "World"', "It's alright"]})
        path = task_func(df, 'test_special_chars.jsonl')
        self.assertTrue(os.path.exists(path))
