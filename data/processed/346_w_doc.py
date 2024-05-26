import pandas as pd
import random


def task_func(product_list, categories, min_value = 10, max_value = 100):
    """
    Create a sales report for a list of products in different categories.
    The report includes the quantity sold and revenue generated for each product.
    
    Parameters:
    product_list (list): The list of products.
    categories (list): A list of categories for the products.
    min_value (int): The minimum value for quantity sold and revenue.
    max_value (int): The maximum value for quantity sold and revenue.
    
    Returns:
    DataFrame: A pandas DataFrame with sales data for the products.
    
    Note:
    - The column names uses are 'Product', 'Category', 'Quantity Sold', and 'Revenue'.

    Requirements:
    - pandas
    - random
    
    Example:
    >>> random.seed(0)
    >>> report = task_func(['Product 1'], ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports'], 100, 100)
    >>> report.iloc[0]['Category'] in ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
    True
    >>> report.iloc[0]['Quantity Sold']
    100
    >>> report.iloc[0]['Revenue']
    10000
    """
    report_data = []
    for product in product_list:
        category = categories[random.randint(0, len(categories)-1)]
        quantity_sold = random.randint(min_value, max_value)
        revenue = quantity_sold * random.randint(min_value, max_value)
        report_data.append([product, category, quantity_sold, revenue])
    report_df = pd.DataFrame(report_data, columns=['Product', 'Category', 'Quantity Sold', 'Revenue'])
    return report_df

import unittest
import pandas as pd
import random
class TestCases(unittest.TestCase):
    
    categories = ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
    products = ['Product ' + str(i) for i in range(1, 101)]
    
    def test_case_1(self):
        random.seed(0)
        report = task_func(self.products[:5], self.categories)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 5)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)
        
    def test_case_2(self):
        random.seed(0)
        report = task_func(self.products[5:10], self.categories)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 5)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)
        
    def test_case_3(self):
        random.seed(0)
        report = task_func([self.products[10]], self.categories)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 1)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)
        
    def test_case_4(self):
        random.seed(0)
        report = task_func(self.products[10:20], self.categories)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 10)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)
        
    def test_case_5(self):
        random.seed(0)
        report = task_func(self.products[20:40], self.categories)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 20)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)
    
    def test_case_6(self):
        random.seed(0)
        report = task_func([self.products[0]], self.categories, 10, 10)
        self.assertTrue(isinstance(report, pd.DataFrame))
        self.assertEqual(len(report), 1)
        self.assertEqual(set(report['Category'].unique()).issubset(self.categories), True)
        self.assertEqual(report.iloc[0]['Quantity Sold'], 10)
        self.assertEqual(report.iloc[0]['Revenue'], 100)
