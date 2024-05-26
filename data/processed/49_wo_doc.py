from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def task_func(timestamps):
    """
    Convert a list of Unix timestamps to date objects, create a Pandas DataFrame, and draw a histogram.
    - The date format should be as DATE_FORMAT.
    - The DataFrame should have 'Timestamp' and 'Datetime' as column names.
    - If the list of timestamps is empty, raise a ValueError with the message "Input list of timestamps is empty".

    Parameters:
    - timestamps (list): The list of Unix timestamps.

    Returns:
    - pandas.DataFrame: A pandas DataFrame containing the original Unix timestamps and the converted datetime objects.
    - Axes: The Axes object of the histogram plot. The histogram will have 10 bins by default, representing the distribution of the datetime objects.

    Raises:
    - ValueError("Input list of timestamps is empty."): If the list of timestamps is empty.

    Requirements:
    - datetime
    - pandas
    - matplotlib.pyplot

    Examples:
    >>> df, ax = task_func([1347517370, 1475153730, 1602737300])
    >>> print(df)
        Timestamp             Datetime
    0  1347517370  2012-09-13 02:22:50
    1  1475153730  2016-09-29 08:55:30
    2  1602737300  2020-10-15 00:48:20
    """
    if not timestamps:
        raise ValueError("Input list of timestamps is empty.")
    datetimes = [datetime.fromtimestamp(t).strftime(DATE_FORMAT) for t in timestamps]
    df = pd.DataFrame({"Timestamp": timestamps, "Datetime": datetimes})
    ax = plt.hist(pd.to_datetime(df["Datetime"]))
    plt.close()
    return df, ax

import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        self.test_data = [
            [1318935276, 1342905276, 23074268],
            [4235087541, 1234653346, 19862358],
            [],
            [1156829289],
            [1000000000, 2000000000, 3000000000],
        ]
    def test_case_1(self):
        input_timestamps = self.test_data[0]
        self.assert_function_output(input_timestamps)
    def test_case_2(self):
        input_timestamps = self.test_data[1]
        self.assert_function_output(input_timestamps)
    def test_case_3(self):
        input_timestamps = self.test_data[2]
        with self.assertRaises(ValueError) as context:
            task_func(input_timestamps)
        self.assertEqual(
            str(context.exception),
            "Input list of timestamps is empty.",
        )
    def test_case_4(self):
        input_timestamps = self.test_data[3]
        self.assert_function_output(input_timestamps)
    def test_case_5(self):
        input_timestamps = self.test_data[4]
        self.assert_function_output(input_timestamps)
        df, ax = task_func(input_timestamps)
        expected_df = pd.DataFrame(
            {
                "Timestamp": [1000000000, 2000000000, 3000000000],
                "Datetime": [
                    "2001-09-09 01:46:40",
                    "2033-05-18 03:33:20",
                    "2065-01-24 05:20:00",
                ],
            }
        )
        
        pd.testing.assert_frame_equal(df, expected_df)
    def assert_function_output(self, input_timestamps):
        df, ax = task_func(input_timestamps)
        # Assert that the DataFrame contains the correct timestamps
        self.assertEqual(df["Timestamp"].tolist(), input_timestamps)
        # Assert the histogram attributes (e.g., number of bins)
        self.assertEqual(len(ax[0]), 10)  # There should be 10 bars in the histogram
