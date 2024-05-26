import random
import string
import pandas as pd


def f_874(n_rows=1000):
    """
    Generate a histogram of the frequency of the top 30 unique random 3-letter strings.
    The function creates random strings, each consisting of 3 letters from the lowercase English alphabet.
    It then plots a histogram showing the frequencies of the top 30 most common strings among the generated set.

    Parameters:
    - n_rows (int): Number of random 3-letter strings to generate.
    Must be positive. Default is 1000.

    Returns:
    - ax (matplotlib.axes.Axes): A Matplotlib Axes object containing the histogram.
    Each bar represents one of the top 30 most frequent 3-letter strings.

    Raises:
    - ValueError: If `n_rows` is less than or equal to 0.

    Requirements:
    - random
    - string
    - pandas
    
    Example:
    >>> ax = f_874(1000)
    >>> ax.get_title()
    'Top 30 Frequencies of Random 3-Letter Strings'
    """
    # Check if n_rows is positive
    if n_rows <= 0:
        raise ValueError("Number of rows must be greater than 0")

    # Generate random strings
    data = ["".join(random.choices(string.ascii_lowercase, k=3)) for _ in range(n_rows)]
    df = pd.DataFrame(data, columns=["String"])

    # Aggregate and plot the data
    frequency = df["String"].value_counts()
    ax = frequency.head(30).plot(
        kind="bar"
    )  # Limit to the top 30 frequencies for readability
    ax.set_title("Top 30 Frequencies of Random 3-Letter Strings")
    ax.set_xlabel("String")
    ax.set_ylabel("Frequency")

    return ax


import unittest
import random
from matplotlib.axes import Axes
import matplotlib.pyplot as plt


class TestCases(unittest.TestCase):
    """Tests for the function f_874."""

    def test_return_type(self):
        """Test if the function returns a Matplotlib Axes object."""
        random.seed(0)
        result = f_874(100)
        self.assertIsInstance(result, Axes)

    def test_default_parameter(self):
        """Test the function with the default parameter."""
        result = f_874()
        self.assertIsInstance(result, Axes)

    def test_zero_rows(self):
        """Test the function with zero rows."""
        with self.assertRaises(ValueError):
            f_874(0)

    def test_negative_rows(self):
        """Test the function with a negative number of rows."""
        with self.assertRaises(ValueError):
            f_874(-1)

    def test_large_number_of_rows(self):
        """Test the function with a large number of rows."""
        random.seed(2)
        result = f_874(10000)
        self.assertIsInstance(result, Axes)

    def tearDown(self):
        plt.close()

def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
