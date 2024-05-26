from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(l):
    """
    Scale the input field to the range [0, 1] and display it as a DataFrame.

    Parameters:
    l (numpy array): The input array.

    Returns:
    DataFrame: A pandas DataFrame of the scaled array.

    Requirements:
    - numpy
    - sklearn.preprocessing
    - pandas

    Note:
    - The return DataFrame use 'Scaled Values' as the column name.

    Example:
    >>> import numpy as np
    >>> l = np.array([10, 20, 30, 40, 50])
    >>> df = task_func(l)
    >>> print(int(df.iloc[0]['Scaled Values']))
    0
    """
    scaler = MinMaxScaler()
    l_scaled = scaler.fit_transform(l.reshape(-1, 1))
    df = pd.DataFrame(l_scaled, columns=['Scaled Values'])
    return df

import unittest
import numpy as np
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        l1 = np.array([10, 20, 30, 40, 50])
        expected_df1 = pd.DataFrame({'Scaled Values': [0.0, 0.25, 0.5, 0.75, 1.0]})
        self.assertTrue(task_func(l1).equals(expected_df1))
    
    def test_case_2(self):
        l2 = np.array([-10, 0, 10])
        expected_df2 = pd.DataFrame({'Scaled Values': [0.0, 0.5, 1.0]})
        self.assertTrue(task_func(l2).equals(expected_df2))
    
    def test_case_3(self):
        l3 = np.array([5, 5, 5])
        expected_df3 = pd.DataFrame({'Scaled Values': [0.0, 0.0, 0.0]})
        self.assertTrue(task_func(l3).equals(expected_df3))
        
    def test_case_4(self):
        l4 = np.array([100])
        expected_df4 = pd.DataFrame({'Scaled Values': [0.0]})
        self.assertTrue(task_func(l4).equals(expected_df4))
    
    def test_case_5(self):
        l5 = np.array([10, 50, 30, 40, 20])
        expected_df5 = pd.DataFrame({'Scaled Values': [0.0, 1.0, 0.5, 0.75, 0.25]})
        self.assertTrue(task_func(l5).equals(expected_df5))
