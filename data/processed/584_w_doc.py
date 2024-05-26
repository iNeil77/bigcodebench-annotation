import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants defining the range of random integers and the size of the DataFrame
RANGE = 100
SIZE = 1000


def task_func():
    """
    Generates a DataFrame with two columns, 'X' and 'Y', each filled with random integers within a specified range,
    and plots these points using a scatter plot. The visualization is created using Seaborn on top of Matplotlib.

    The function is designed to be parameter-free for simplicity, utilizing constants for configuration.

    Returns:
        pd.DataFrame: A DataFrame with 'X' and 'Y' columns containing the generated random integers.

    Requirements:
        - numpy
        - pandas
        - seaborn
        - matplotlib.pyplot

    No Parameters.

    Example:
        >>> df = task_func()
        >>> isinstance(df, pd.DataFrame)
        True
        >>> 'X' in df.columns and 'Y' in df.columns
        True
        >>> len(df)
        1000
        >>> all(df['X'].between(0, RANGE - 1)) and all(df['Y'].between(0, RANGE - 1))
        True
    """
    df = pd.DataFrame({
        'X': np.random.randint(0, RANGE, SIZE),
        'Y': np.random.randint(0, RANGE, SIZE)
    })
    sns.scatterplot(data=df, x='X', y='Y')
    plt.show()
    return df

import unittest
class TestCases(unittest.TestCase):
    def test_dataframe_shape(self):
        """Test that the DataFrame has the correct shape."""
        df = task_func()
        self.assertEqual(df.shape, (SIZE, 2))
    def test_random_range(self):
        """Test that the random numbers fall within the specified range."""
        df = task_func()
        self.assertTrue(df['X'].between(0, RANGE-1).all())
        self.assertTrue(df['Y'].between(0, RANGE-1).all())
    def test_columns_existence(self):
        """Ensure both 'X' and 'Y' columns exist."""
        df = task_func()
        self.assertIn('X', df.columns)
        self.assertIn('Y', df.columns)
    def test_non_empty_dataframe(self):
        """Check that the DataFrame is not empty."""
        df = task_func()
        self.assertFalse(df.empty)
    def test_columns_type(self):
        """Test that 'X' and 'Y' columns are of integer type."""
        df = task_func()
        self.assertTrue(np.issubdtype(df['X'].dtype, np.integer))
        self.assertTrue(np.issubdtype(df['Y'].dtype, np.integer))
