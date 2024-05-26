import itertools
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
SHAPES = [
    "Circle",
    "Square",
    "Triangle",
    "Rectangle",
    "Pentagon",
    "Hexagon",
    "Heptagon",
    "Octagon",
    "Nonagon",
    "Decagon",
]
COLORS = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Black",
    "White",
    "Purple",
    "Orange",
    "Pink",
    "Brown",
]


def f_902(num_pairs=10):
    """
    Generate and display a countplot of predefined shape-color pairs.

    This function creates a visual representation of a specified number of unique shape-color combinations,
    each displayed as a bar in the countplot. The shape-color pairs are selected from a predefined list.

    Parameters:
    - num_pairs (int): The number of unique shape-color pairs to be displayed in the countplot.
                       Default is 10. If the requested number is less than 1 or greater than the total
                       possible unique combinations (100), it is adjusted to the valid range (1 to 100).

    Returns:
    - ax (matplotlib.axes._subplots.AxesSubplot): The Axes object of the countplot, which can be used for
                                                  further customizations or to retrieve information about the plot.

    Requirements:
    - itertools
    - seaborn
    - matplotlib

    Example:
    >>> ax = f_902(10)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    >>> ax = f_902(9)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    >>> ax = f_902(8)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    >>> ax = f_902(7)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    >>> ax = f_902(6)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    """
    max_pairs = len(SHAPES) * len(COLORS)
    num_pairs = min(num_pairs, max_pairs)
    
    pairs = [f"{s}:{c}" for s, c in itertools.product(SHAPES, COLORS)][:num_pairs]
    
    # Drawing the countplot
    ax = sns.countplot(x=pairs, hue=pairs, palette="Set3", legend=False)
    plt.xticks(rotation=90)
    
    return ax


import unittest
import matplotlib.pyplot as plt
import random


class TestCases(unittest.TestCase):
    """Tests for f_902."""

    def tearDown(self):
        plt.clf()

    def test_basic_functionality(self):
        """Test basic functionality with default parameters."""
        random.seed(0)
        ax = f_902()
        self.assertIsInstance(ax, plt.Axes)

    def test_pair_count(self):
        """Test if the number of displayed shape-color pairs matches the input."""
        random.seed(1)
        num_pairs = 7
        ax = f_902(num_pairs)
        displayed_pairs = len(set(tick.get_text() for tick in ax.get_xticklabels()))
        self.assertEqual(displayed_pairs, num_pairs)

    def test_valid_pairs(self):
        """Ensure displayed shape-color pairs are valid combinations."""
        random.seed(2)
        ax = f_902(10)
        displayed_pairs = [tick.get_text() for tick in ax.get_xticklabels()]
        for pair in displayed_pairs:
            shape, color = pair.split(":")
            self.assertIn(shape, SHAPES)
            self.assertIn(color, COLORS)

    def test_max_pairs(self):
        """Test with the maximum number of pairs possible."""
        random.seed(3)
        max_pairs = len(SHAPES) * len(COLORS)
        ax = f_902(max_pairs)
        displayed_pairs = len(set(tick.get_text() for tick in ax.get_xticklabels()))
        self.assertEqual(displayed_pairs, max_pairs)

    def test_min_pairs(self):
        """Test with the minimum number of pairs, which is 1."""
        random.seed(4)
        ax = f_902(1)
        displayed_pairs = len(set(tick.get_text() for tick in ax.get_xticklabels()))
        self.assertEqual(displayed_pairs, 1)


def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
