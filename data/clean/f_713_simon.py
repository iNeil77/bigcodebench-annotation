import numpy as np
import itertools


def f_713(data_list, file_name):
    """
    This function takes a list of tuples. The first value of each tuple is a string,
    the other values are numeric. E.g. ('test', 2, 12.4, -2)
    It calculates the mean over all tuples of the numerical values for each tuple position excluding the first position, 
    and writes the results into a specified text file.
    The content in the text file is formated as follows:
    'Position 'x': 'mean', where x is the current tuple position and 'mean' denotes the 
    computed mean value. Each Position is written in a new line.
    It returns a list of the calculated mean values.

    Missing values and non numeric values at positions other than the first are filled / replaced with np.nan. 
    If an empty list is handed to the function an empty list is returned and an empty file is created.

    The function utilizes the 'numpy' library for numerical operations and the 'itertools' library 
    to handle the iteration through the data structure.

    Parameters:
    - data_list (list of tuples): A list containing tuples of the form (string, numeric, numeric, ...)
    - file_name (str): The name of the text file to store the mean values.

    Returns:
    - list: A list of mean values calculated from the numerical data in the tuples.

    Requirements:
    - numpy
    - itertools

    Example:
    >>> data = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
    >>> f_713(data, 'mean_values.txt')
    [3.0, 4.0]
    >>> with open('mean_values.txt') as file:
    ...    txt_content = file.readlines()
    >>> print(txt_content)
    ['Position 1: 3.0\\n', 'Position 2: 4.0\\n']
    >>> data_list=[('hi', 'test', -12, 4), ('hallo', 1.2, 'test'), ('hola', -3, 34, 12.1)]
    >>> f_713(data_list, 'test.txt')
    [-0.9, 11.0, 8.05]
    >>> with open('test.txt') as file:
    ...     txt_content = file.readlines()
    >>> print(txt_content)
    ['Position 1: -0.9\\n', 'Position 2: 11.0\\n', 'Position 3: 8.05\\n']
    """
    # Unzipping the data to separate the elements of the tuples
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = []
    # Calculating the mean values excluding the first position (non-numerical)
    for column in unzipped_data[1:]:
        numeric_values = [val for val in column if isinstance(val, (int, float))]
        if numeric_values:
            mean_values.append(np.nanmean(numeric_values))
        else:
            mean_values.append(np.nan)

    # Writing the mean values to the specified file
    with open(file_name, 'w') as f:
        for i, mean_value in enumerate(mean_values, start=1):
            f.write('Position {}: {}\n'.format(i, mean_value))
    
    # Returning the list of mean values for testing purposes
    return mean_values

import unittest
import os
import numpy as np


class TestCases(unittest.TestCase):
    def setUp(self):
        # Variables for the tests
        self.data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        self.file_name = "test_output.txt"

    def tearDown(self) -> None:
        if os.path.isfile(self.file_name):
            os.remove(self.file_name)

    def read_file_content(self, file_path):
        # Read the content of the file and return it as a list of lines
        with open(file_path, 'r') as file:
            return file.readlines()

    def test_mean_values_with_valid_data(self):
        expected_means = [3.0, 4.0]  # Expected mean values
        expected_file_content = ["Position 1: 3.0\n", "Position 2: 4.0\n"]
        result = f_713(self.data_list, self.file_name)

        self.assertEqual(result, expected_means)
        self.assertTrue(os.path.isfile(self.file_name))  # Check file creation

        # Verify the content of the created file
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)

    def test_function_with_empty_data(self):
        result = f_713([], self.file_name)
        self.assertEqual(result, [])  # Should return an empty list
        self.assertTrue(os.path.isfile(self.file_name))  # Check file creation
        expected_file_content = []
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)

    def test_function_with_non_numeric_data(self):
        data_with_non_numeric = [('a', 'x', 'y'), ('b', 'p', 'q')]
        result = f_713(data_with_non_numeric, self.file_name)
        self.assertEqual(result, [np.nan, np.nan])
        self.assertTrue(os.path.isfile(self.file_name))  # Check file creation
        expected_file_content = ["Position 1: nan\n", "Position 2: nan\n"]
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)

    def test_function_with_incomplete_tuples(self):
        inconsistent_data = [('a', 1), ('b',), ('c', 2, 3)]
        expected_means = [1.5, 3.0]  # Expected means
        result = f_713(inconsistent_data, self.file_name)

        self.assertEqual(result, expected_means)
        self.assertTrue(os.path.isfile(self.file_name))  # Check file creation
        expected_file_content = ["Position 1: 1.5\n", "Position 2: 3.0\n"]
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)

    def test_function_with_all_nan_values(self):
        data_all_nan = [('a', np.nan, np.nan) for _ in range(5)]
        expected_means = [np.nan, np.nan]
        result = f_713(data_all_nan, self.file_name)

        # Check if all values are 'nan'
        self.assertTrue(result, expected_means)
        self.assertTrue(os.path.isfile(self.file_name))  # Check file creation
        expected_file_content = ["Position 1: nan\n", "Position 2: nan\n"]
        actual_file_content = self.read_file_content(self.file_name)
        self.assertEqual(actual_file_content, expected_file_content)


# Running the tests
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


# This part is for running the tests if this script is executed.
if __name__ == "__main__":
    run_tests()