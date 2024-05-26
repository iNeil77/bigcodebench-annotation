import pandas as pd
import time


def task_func(df, letter):
    """
    The function filters rows in a dict of list in which the values of the 'Word' column begin with a specified letter.
    It first convert the dict to Datafrome, then calculates the length of the words in the filtered column and returns
    a dictionary of word lengths and their respective counts.

    Parameters:
    df (dict of list): A dictionary where the key 'Word' maps to a list of strings.
    letter (str): The letter to filter the 'Word' column by. 

    Returns:
    dict: A dictionary of word lengths and their counts.
    
    Requirements:
    - pandas
    - time

    Example:
    >>> df = {'Word': ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']}
    >>> task_func(df, 'a')
    {5: 1}
    """
    start_time = time.time()
    df = pd.DataFrame(df)
    regex = '^' + letter
    filtered_df = df[df['Word'].str.contains(regex, regex=True)]
    word_lengths = filtered_df['Word'].str.len()
    count_dict = word_lengths.value_counts().to_dict()
    end_time = time.time()  # End timing
    cost = f"Operation completed in {end_time - start_time} seconds."
    return count_dict

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = {'Word': ['apple', 'banana', 'cherry', 'date', 'elephant', 'fig', 'grape', 'kiwi']}
        result = task_func(df, 'a')
        expected_result = {5: 1}
        self.assertDictEqual(result, expected_result)
    def test_case_2(self):
        df = {'Word': ['cat', 'dog', 'elephant', 'fish', 'goose']}
        result = task_func(df, 'e')
        expected_result = {8: 1}
        self.assertDictEqual(result, expected_result)
    def test_case_3(self):
        df = {'Word': ['kiwi', 'lemon', 'mango', 'nectarine', 'orange']}
        result = task_func(df, 'm')
        expected_result = {5: 1}
        self.assertDictEqual(result, expected_result)
    def test_case_4(self):
        df = {'Word': ['apple', 'banana', 'cherry', 'date', 'elephant', 'fig', 'grape', 'kiwi']}
        result = task_func(df, 'z')
        expected_result = {}
        self.assertDictEqual(result, expected_result)
    def test_case_5(self):
        df = {'Word': ['zebra', 'zoo', 'zucchini']}
        result = task_func(df, 'z')
        expected_result = {5: 1, 3: 1, 8: 1}
        self.assertDictEqual(result, expected_result)
