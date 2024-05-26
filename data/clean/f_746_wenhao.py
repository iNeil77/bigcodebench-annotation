import pandas as pd
import matplotlib.pyplot as plt

def f_746(d, keys=['x', 'y', 'z']):
    """
    Plot values from a list of dictionaries based on specified keys and return the plot as a Matplotlib Axes object.
    
    Parameters:
    d (list): A list of dictionaries containing numerical data.
    keys (list, optional): A list of string keys to plot. Defaults to ['x', 'y', 'z'].

    Returns:
    Matplotlib Axes object: The plot showing the values of specified keys from the input list of dictionaries.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
    >>> ax = f_746(data)
    >>> type(ax)
    <class 'matplotlib.axes._subplots.Axes'>

    >>> ax = f_746(data, keys=['x', 'y'])
    >>> type(ax)
    <class 'matplotlib.axes._subplots.Axes'>
    """
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(d)

    # Initialize a plot
    fig, ax = plt.subplots()
    
    # Plot the values for the specified keys
    plotted_keys = []
    for key in keys:
        if key in df.columns:
            ax.plot(df[key], label=key)
            plotted_keys.append(key)
    
    # Add a legend if there are any lines plotted
    if plotted_keys:
        ax.legend()
    
    # Return the Axes object
    return ax

import unittest
from matplotlib.axes import Axes

class TestCases(unittest.TestCase):
    
    def test_basic_input(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
        ax = f_746(data)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(set([text.get_text() for text in ax.legend_.texts]), {'x', 'y', 'z'})
        self.assertEqual(len(ax.lines), 3)

    def test_missing_keys_in_data(self):
        data = [{'x': 1, 'y': 10}, {'y': 15, 'z': 6}, {'x': 2, 'z': 7}]
        ax = f_746(data)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(set([text.get_text() for text in ax.legend_.texts]), {'x', 'y', 'z'})
        self.assertEqual(len(ax.lines), 3)

    def test_custom_keys(self):
        data = [{'a': 1, 'b': 10}, {'b': 15, 'c': 6}, {'a': 2, 'c': 7}]
        ax = f_746(data, keys=['a', 'b', 'c'])
        self.assertIsInstance(ax, Axes)
        self.assertEqual(set([text.get_text() for text in ax.legend_.texts]), {'a', 'b', 'c'})
        self.assertEqual(len(ax.lines), 3)

    def test_empty_data_list(self):
        data = []
        ax = f_746(data)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(len(ax.lines), 0)
        self.assertIsNone(ax.legend_)

    def test_single_key_data(self):
        data = [{'x': 1}, {'x': 2}, {'x': 3}]
        ax = f_746(data)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(set([text.get_text() for text in ax.legend_.texts]), {'x'})
        self.assertEqual(len(ax.lines), 1)

def run_tests():
    unittest.main(argv=[''], exit=False)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
