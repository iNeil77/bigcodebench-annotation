import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def task_func(a, b, columns=['A', 'B']):
    """
    Standardize two lists of numbers using the StandardScaler from sklearn and visualize the standardized values using a bar plot.

    Parameters:
        a (list): A list of numbers.
        b (list): Another list of numbers.
        columns (list, optional): Column names for the resulting DataFrame. Defaults to ['A', 'B'].

    Returns:
        pd.DataFrame: A DataFrame containing the standardized values.
        matplotlib.axes.Axes: Axes object of the displayed bar plot.

    Requirements:
        - numpy
        - pandas
        - sklearn.preprocessing
        - matplotlib.pyplot

    Example:
        >>> df, ax = task_func([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
        >>> isinstance(df, pd.DataFrame) and isinstance(ax, matplotlib.axes.Axes)
        True
    """
    if len(a) == 0 or len(b) == 0:
        fig, ax = plt.subplots()
        plt.close(fig)  # Prevent empty plot from displaying
        return pd.DataFrame(), ax
    scaler = StandardScaler()
    standardized_values = scaler.fit_transform(np.array([a, b]).T)
    df = pd.DataFrame(standardized_values, columns=columns)
    ax = df.plot(kind='bar')
    plt.show()
    return df, ax

import unittest
import matplotlib
class TestCases(unittest.TestCase):
    def test_standard_case(self):
        """Test the function with non-empty lists."""
        df, ax = task_func([1, 2, 3], [4, 5, 6])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (3, 2))
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_empty_lists(self):
        """Test the function with empty lists."""
        df, ax = task_func([], [])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.empty, True)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_unequal_length_lists(self):
        """Test the function with lists of unequal length. Expecting an exception."""
        with self.assertRaises(ValueError):
            task_func([1, 2, 3], [4, 5])
    def test_single_value_lists(self):
        """Test the function with single-value lists."""
        df, ax = task_func([1], [1])
        self.assertEqual(df.shape, (1, 2))
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_large_lists(self):
        """Test the function with large lists."""
        df, ax = task_func(list(range(100)), list(range(100, 200)))
        self.assertEqual(df.shape, (100, 2))
        self.assertIsInstance(ax, matplotlib.axes.Axes)
