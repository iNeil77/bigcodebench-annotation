import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt


def task_func(a, b):
    """
    Calculate the Euclidean distance between two lists, create a Pandas DataFrame from these lists
    with indices 'A' and 'B', and then draw the values with a line displaying the Euclidean distance.

    Parameters:
    a (list): A list of numbers.
    b (list): Another list of numbers.

    Returns:
    float: The computed Euclidean distance between the two lists.
    pd.DataFrame: A DataFrame containing the two lists as columns.
    matplotlib.axes.Axes: The generated plot's Axes object.

    Requirements:
    - pandas
    - scipy.spatial
    - matplotlib.pyplot

    Example:
    >>> euclidean_distance, df, ax = task_func([1, 2, 3], [2, 3, 4])
    >>> print(euclidean_distance)
    1.7320508075688772
    """
    euclidean_distance = distance.euclidean(a, b)
    df = pd.DataFrame({'A': a, 'B': b})
    fig, ax = plt.subplots()
    ax.plot(df['A'], df['B'])
    ax.plot([df['A'].iloc[0], df['B'].iloc[0]], [df['A'].iloc[-1], df['B'].iloc[-1]], 'ro-')
    return euclidean_distance, df, ax

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        a = [1, 2, 3]
        b = [2, 3, 4]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertAlmostEqual(euclidean_distance, 1.732, places=3)
        self.assertTrue('A' in df.columns)
        self.assertTrue('B' in df.columns)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)
    def test_case_2(self):
        a = [1, 1, 1]
        b = [1, 1, 1]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertEqual(euclidean_distance, 0)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)
    def test_case_3(self):
        a = [0, 5, 10]
        b = [10, 5, 0]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertAlmostEqual(euclidean_distance, 14.142, places=3)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)
    def test_case_4(self):
        a = [3, 3, 3, 3]
        b = [4, 4, 4, 4]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertAlmostEqual(euclidean_distance, 2.0, places=3)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)
    def test_case_5(self):
        a = [1, 2, 3, 4, 5]
        b = [5, 4, 3, 2, 1]
        euclidean_distance, df, ax = task_func(a, b)
        self.assertAlmostEqual(euclidean_distance, 6.325, places=3)
        self.assertListEqual(df['A'].tolist(), a)
        self.assertListEqual(df['B'].tolist(), b)
        lines = ax.get_lines()
        self.assertTrue(len(lines) > 0)
