import pandas as pd
import numpy as np


def task_func(column, data):
    """
    Analyze a list of sales data, calculate the sum, the mean, the minimum, the maximum of a given column,
    and return the bar chart plot for the given column without displaying it.

    Parameters:
    column (str): The column to analyze. Expected values are ['Product', 'Quantity Sold', 'Total Sales'].
    data (list): The sales data. Expected format: [['Product Name', Quantity Sold (int), Total Sales (int)], ...]
                 The function checks for data validity in the quantity columns (must not be negative).

    Returns:
    tuple: A tuple containing:
        - dict: A dictionary with the sum, mean, min, max of the column.
        - matplotlib.axes.Axes: The Axes object of the plotted bar chart. The bar chart will have Product in its
                                x-axis and the title Bar Chart of (column).

    Requirements:
    - pandas
    - numpy

    Raises:
    - ValueError: If the quantity sold or total sales is negative.
    
    Example:
    >>> data = [['Product A', 100, 10000], ['Product B', 150, 15000], ['Product C', 200, 20000]]
    >>> stats, plot = task_func('Total Sales', data)
    >>> stats
    {'sum': 45000, 'mean': 15000.0, 'min': 10000, 'max': 20000}
    >>> plot
    <Axes: title={'center': 'Bar Chart of Total Sales'}, xlabel='Product'>
    """
    COLUMNS = ["Product", "Quantity Sold", "Total Sales"]
    df = pd.DataFrame(data, columns=COLUMNS)
    if (df["Quantity Sold"] < 0).any() or (df["Total Sales"] < 0).any():
        raise ValueError("Value must not be negative")
    column_data = df[column]
    result = {
        "sum": np.sum(column_data),
        "mean": np.mean(column_data),
        "min": np.min(column_data),
        "max": np.max(column_data),
    }
    ax = df.plot.bar(x="Product", y=column, title=f"Bar Chart of {column}")
    return result, ax

import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test total sales
        scenarios = [
            (
                [
                    ["Product A", 100, 10000],
                    ["Product B", 150, 15000],
                    ["Product C", 200, 20000],
                ],
                {"sum": 45000, "mean": 15000.0, "min": 10000, "max": 20000},
            ),
            (
                [
                    ["Product A", 10, 1000],
                    ["Product B", 20, 2000],
                    ["Product C", 30, 3000],
                    ["Product D", 40, 4000],
                ],
                {"sum": 10000, "mean": 2500.0, "min": 1000, "max": 4000},
            ),
            (
                [["Product A", 5, 500]],
                {"sum": 500, "mean": 500.0, "min": 500, "max": 500},
            ),
        ]
        for data, expected in scenarios:
            with self.subTest(data=data):
                stats, ax = task_func("Total Sales", data)
                self.assertDictEqual(stats, expected)
                self.assertEqual(ax.get_title(), "Bar Chart of Total Sales")
                plt.close("all")
    def test_case_2(self):
        # Test quantity sold
        scenarios = [
            (
                [
                    ["Product A", 100, 5000],
                    ["Product B", 200, 6000],
                    ["Product C", 300, 7000],
                ],
                {"sum": 600, "mean": 200.0, "min": 100, "max": 300},
            ),
            (
                [
                    ["Product A", 5, 500],
                    ["Product B", 10, 1000],
                    ["Product C", 15, 1500],
                    ["Product D", 20, 2000],
                    ["Product E", 25, 2500],
                ],
                {"sum": 75, "mean": 15.0, "min": 5, "max": 25},
            ),
        ]
        for data, expected in scenarios:
            with self.subTest(data=data):
                stats, ax = task_func("Quantity Sold", data)
                self.assertDictEqual(stats, expected)
                self.assertEqual(ax.get_title(), "Bar Chart of Quantity Sold")
                plt.close("all")
    def test_case_3(self):
        # Test error handling - invalid column
        with self.assertRaises(KeyError):
            task_func("Invalid Column", [["Product A", 100, 10000]])
    def test_case_4(self):
        # Test error handling - empty data and negative values
        with self.assertRaises(Exception):
            task_func("Total Sales", [])
        with self.assertRaises(Exception):
            task_func("Total Sales", [["Product A", -100, -10000]])
    def test_case_5(self):
        # Test plot data integrity
        data = [["Product A", 100, 5000], ["Product B", 200, 10000]]
        _, ax = task_func("Quantity Sold", data)
        bars = [rect.get_height() for rect in ax.patches]
        expected_bars = [100, 200]
        self.assertEqual(bars, expected_bars)
        plt.close("all")
    def tearDown(self):
        plt.close("all")
