import pandas as pd
from collections import Counter

def task_func(df):
    """
    Calculate the frequency of combinations of elements in a DataFrame.
    The function adds a 'combination' column to the DataFrame, which is the combination of items in each row.
    It then calculates the frequency of each combination.
    
    Parameters:
    - df (pandas.DataFrame): The input DataFrame with columns 'item1', 'item2', 'item3', 'item4', 'item5'.
    
    Returns:
    - dict: A dictionary containing the frequency of all combination.

    Requirements:
    - pandas
    - collections

    Example:
    >>> df = pd.DataFrame({'item1': ['a', 'b', 'a'], 'item2': ['b', 'c', 'b'], 'item3': ['c', 'd', 'c'], 'item4': ['d', 'e', 'd'], 'item5': ['e', 'f', 'e']})
    >>> task_func(df)
    {('a', 'b', 'c', 'd', 'e'): 2, ('b', 'c', 'd', 'e', 'f'): 1}
    """
    df['combination'] = pd.Series(df.apply(lambda row: tuple(sorted(row)), axis=1))
    combination_freq = Counter(df['combination'])
    return dict(combination_freq)

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame({'item1': ['a', 'b', 'a'], 'item2': ['b', 'c', 'b'], 'item3': ['c', 'd', 'c'], 'item4': ['d', 'e', 'd'], 'item5': ['e', 'f', 'e']})
        freq = task_func(df)
        self.assertEqual(freq[('a', 'b', 'c', 'd', 'e')], 2)
        self.assertEqual(freq[('b', 'c', 'd', 'e', 'f')], 1)
    def test_case_2(self):
        df = pd.DataFrame({'item1': ['c', 'b', 'a'], 'item2': ['b', 'c', 'b'], 'item3': ['c', 'd', 'c'], 'item4': ['d', 'e', 'd'], 'item5': ['e', 'f', 'e']})
        freq = task_func(df)
        print(freq)
        self.assertEqual(freq[('a', 'b', 'c', 'd', 'e')], 1)
        self.assertEqual(freq[('b', 'c', 'd', 'e', 'f')], 1)
        if ('b', 'c', 'c', 'd', 'e') in freq:
            self.assertEqual(freq[('b', 'c', 'c', 'd', 'e')], 1)
        elif ('c', 'b', 'c', 'd', 'e') in freq:
            self.assertEqual(freq[('c', 'b', 'c', 'd', 'e')], 1)
    def test_case_3(self):
        df = pd.DataFrame({'item1': ['a'], 'item2': ['a'], 'item3': ['a'], 'item4': ['a'], 'item5': ['a']})
        freq = task_func(df)
        self.assertEqual(freq[('a', 'a', 'a', 'a', 'a')], 1)
    def test_case_4(self):
        df = pd.DataFrame({'item1': ['a', 'b', 'c'], 'item2': ['b', 'c', 'd'], 'item3': ['c', 'd', 'e'], 'item4': ['d', 'e', 'f'], 'item5': ['e', 'f', 'g']})
        freq = task_func(df)
        self.assertEqual(freq[('a', 'b', 'c', 'd', 'e')], 1)
        self.assertEqual(freq[('b', 'c', 'd', 'e', 'f')], 1)
        self.assertEqual(freq[('c', 'd', 'e', 'f', 'g')], 1)
    def test_case_5(self):
        df = pd.DataFrame({'item1': ['a', 'a', 'a'], 'item2': ['b', 'b', 'b'], 'item3': ['c', 'c', 'c'], 'item4': ['d', 'd', 'd'], 'item5': ['e', 'e', 'e']})
        freq = task_func(df)
        self.assertEqual(freq[('a', 'b', 'c', 'd', 'e')], 3)
