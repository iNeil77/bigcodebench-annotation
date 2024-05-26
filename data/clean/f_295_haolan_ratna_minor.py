import numpy as np
import matplotlib.pyplot as plt

# Constants
COLORS = ['r', 'g', 'b']

def f_295(df, group_col, value_col):
    """
    Create a bar chart of data in multiple groups with error bars.

    Parameters:
    - df (DataFrame): The input DataFrame containing the data.
    - group_col (str): The name of the column to group the data by.
    - value_col (str): The name of the column containing the values to plot.

    Returns:
    - AxesSubplot: A matplotlib axes object with the bar chart.

    Requirements:
    - matplotlib.pyplot
    - numpy

    Example:
    >>> import matplotlib.pyplot as plt
    >>> import pandas as pd
    >>> df = pd.DataFrame({'Group': ['A', 'B', 'A', 'B', 'A', 'B'], 'Value': [1, 2, 3, 4, 5, 6]})
    >>> ax = f_295(df, 'Group', 'Value')
    >>> len(ax.patches)
    2
    >>> plt.close()

    Note:
    - The function uses a predefined set of colors for the bars. If there are more groups than colors,
      the colors will repeat from the beginning of the COLORS list.
    - This function use "Bar chart of {value_col} by {group_col}" for the plot title.
    - This function use value of variables group_col and value_col as the xlabel and ylabel respectively.

    Raises:
    -This function will raise TypeError if the 'Value' has non-numeric values.
    """

    group_mean = df.groupby(group_col)[value_col].mean()
    group_std = df.groupby(group_col)[value_col].std()

    # Get the number of groups and generate x locations for the bars
    num_groups = len(group_mean)
    index = np.arange(num_groups)

    # Create the bar chart with error bars
    for i, (mean, std) in enumerate(zip(group_mean, group_std)):
        plt.bar(index[i], mean, yerr=std, color=COLORS[i % len(COLORS)], capsize=4, label=f'Group {i+1}')

    # Set labels and title
    plt.xlabel(group_col)
    plt.ylabel(value_col)
    plt.title(f'Bar chart of {value_col} by {group_col}')
    plt.xticks(index, group_mean.index)  # Set x-axis labels to group names
    plt.legend()
    # Return the axes object
    return plt.gca()

import unittest
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from faker import Faker
faker = Faker()

# Constants
COLORS = ['r', 'g', 'b']

class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({'Group': ['A', 'B', 'C'], 'Value': [10, 20, 30]})
        self.ax = f_295(self.df, 'Group', 'Value')
        plt.close()

    def test_bar_chart(self):
        # Create a figure and render the plot
        fig = plt.figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        canvas = FigureCanvas(fig)
        self.ax.set_title('Bar chart of Value by Group')
        self.ax.set_xlabel('Group')
        self.ax.set_ylabel('Value')
        self.ax.legend(['Group 1', 'Group 2', 'Group 3'])

        canvas.draw()
        
        # Get the RGBA buffer and convert to RGB
        buf = canvas.buffer_rgba()
        rgb = np.asarray(buf)

        # Check that bars are present in the plot
        self.assertTrue(np.any(rgb[:, :, 3] != 0), msg="No bars found in the plot")
        plt.close()

    def test_single_group(self):
        # Test for a single group with a single value
        df_single_group = pd.DataFrame({
            'Group': ['A'] * 4,
            'Value': [1, 2, 3, 4]
        })
        ax = f_295(df_single_group, 'Group', 'Value')
        self.assertIsNotNone(ax, "The axes object should not be None")
        plt.close()

    def test_multiple_groups(self):
        # Test for multiple groups
        df_multiple_groups = pd.DataFrame({
            'Group': ['A', 'B', 'C', 'D'] * 4,
            'Value': [1, 2, 3, 4] * 4
        })
        ax = f_295(df_multiple_groups, 'Group', 'Value')
        self.assertIsNotNone(ax, "The axes object should not be None")
        plt.close()

    def test_with_nan(self):
        # Test handling of NaN values
        df_with_nan = pd.DataFrame({
            'Group': ['A', 'B', 'C', 'D', None],
            'Value': [1, 2, 3, 4, None]
        })
        ax = f_295(df_with_nan, 'Group', 'Value')
        self.assertIsNotNone(ax, "The axes object should not be None")
        plt.close()

    def test_non_numeric_values(self):
        # Test with non-numeric values to ensure TypeError is raised
        df_non_numeric = pd.DataFrame({
            'Group': ['A', 'B', 'C', 'D'],
            'Value': [1, 'two', 3, 4]
        })
        with self.assertRaises(TypeError):
            f_295(df_non_numeric, 'Group', 'Value')
        plt.close()

    def test_large_numbers(self):
        # Test with a large range of numbers
        df_large_numbers = pd.DataFrame({
            'Group': ['A'] * 100,
            'Value': range(1, 101)
        })
        ax = f_295(df_large_numbers, 'Group', 'Value')
        self.assertIsNotNone(ax, "The axes object should not be None")
        plt.close()


    def test_complex_data(self):
        # Test with complex data generated by Faker
        df_complex = generate_complex_test_data(num_rows=100)
        ax = f_295(df_complex, 'Group', 'Value')
        self.assertIsNotNone(ax, "The axes object should not be None for complex data")
        plt.close()

def generate_complex_test_data(num_rows=100):
    """Generate a DataFrame with a mix of numeric and text data, including some potential outliers."""
    data = {
        'Group': [faker.random_element(elements=('A', 'B', 'C', 'D')) for _ in range(num_rows)],
        'Value': [faker.random_int(min=0, max=1000) for _ in range(num_rows)]
    }
    complex_df = pd.DataFrame(data)
    return complex_df


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
