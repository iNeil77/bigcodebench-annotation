import pandas as pd
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    """
    Reads data from an Excel spreadsheet, converts it to a CSV file, then calculates the sum of each column in the CSV file.

    Parameters:
    - sheet_name (str): The name of the sheet to load data from.
    - excel_file_location (str): The path to the Excel file. Default is 'test.xlsx'.
    - csv_file_location (str): The path where the CSV file will be saved. Default is 'test.csv'.

    Returns:
    - dict: A dictionary with the sum of each column.

    Raises:
    - FileNotFoundError: If the Excel file does not exist at the specified path.
    - ValueError: If the specified sheet name is not found in the Excel file.

    Requirements:
    - pandas
    - logging

    Example:
    >>> test_excel_file = 'dummy_test.xlsx'
    >>> test_csv_file = 'dummy_test.csv'
    >>> test_sheet_name = 'TestSheet'
    >>> data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
    >>> df = pd.DataFrame(data)
    >>> df.to_excel(test_excel_file, sheet_name=test_sheet_name, index=False)
    >>> task_func(sheet_name='TestSheet', excel_file_location=test_excel_file, csv_file_location=test_csv_file) # {'Column1': sum_value1, 'Column2': sum_value2, ...}
    {'A': 60, 'B': 150}
    >>> os.remove(test_excel_file)
    >>> os.remove(test_csv_file)
    
    Note:
    - Ensure the Excel file contains only numerical data for accurate sum calculations.
    """
    try:
        logging.info('Reading the Excel file.')
        df = pd.read_excel(excel_file_location, sheet_name=sheet_name)
        logging.info('Converting to CSV.')
        df.to_csv(csv_file_location, index=False)
        column_sum = df.sum(numeric_only=True)
    except FileNotFoundError:
        logging.error(f"Excel file not found at {excel_file_location}")
        raise FileNotFoundError(f"Excel file not found at {excel_file_location}")
    except ValueError as e:
        logging.error(f"Error in processing Excel file: {e}")
        raise ValueError(f"Error in processing Excel file: {e}")
    return column_sum.to_dict()

import unittest
import pandas as pd
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        # Creating a dummy Excel file for testing
        self.test_excel_file = 'dummy_test.xlsx'
        self.test_csv_file = 'dummy_test.csv'
        self.test_sheet_name = 'TestSheet'
        data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
        df = pd.DataFrame(data)
        df.to_excel(self.test_excel_file, sheet_name=self.test_sheet_name, index=False)
    def tearDown(self):
        os.remove(self.test_excel_file)
        if os.path.exists(self.test_csv_file):
            os.remove(self.test_csv_file)
    def test_normal_functionality(self):
        result = task_func(self.test_sheet_name, self.test_excel_file, self.test_csv_file)
        self.assertEqual(result, {'A': 60, 'B': 150})
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func(self.test_sheet_name, 'nonexistent.xlsx', self.test_csv_file)
    def test_sheet_not_found(self):
        with self.assertRaises(ValueError):
            task_func('NonexistentSheet', self.test_excel_file, self.test_csv_file)
    def test_empty_excel_file(self):
        empty_excel_file = 'empty_test.xlsx'
        pd.DataFrame().to_excel(empty_excel_file, index=False)
        with self.assertRaises(ValueError):
            task_func(self.test_sheet_name, empty_excel_file, self.test_csv_file)
        os.remove(empty_excel_file)
    def test_overwrite_existing_csv(self):
        with open(self.test_csv_file, 'w') as file:
            file.write('Old Data')
        task_func(self.test_sheet_name, self.test_excel_file, self.test_csv_file)
        with open(self.test_csv_file, 'r') as file:
            self.assertNotIn('Old Data', file.read())
