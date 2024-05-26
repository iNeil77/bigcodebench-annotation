import pickle
import os
import matplotlib.pyplot as plt


def task_func(numbers, file_path="save.pkl"):
    """
    Save a Matplotlib image generated from the provided "numbers" list in a pickle file.
    The function then reads the image back from the file for validation and deletes the pickle file afterward.

    Parameters:
    - numbers  (list): List of int/float values used to generate the matplotlib figure.
    - file_path (str): Path to temporary pickle file. Defaults to 'save.pkl'.

    Returns:
    - loaded_fig (matplotlib.figure.Figure): The loaded matplotlib figure from file_path.

    Requirements:
    - pickle
    - os
    - matplotlib.pyplot

    Raises:
    - TypeError: If the input is not a list of numbers.
    
    Example:
    >>> numbers = [random.random() for _ in range(100)]
    >>> loaded_fig = task_func(numbers)
    >>> type(loaded_fig)
    <class 'matplotlib.figure.Figure'>
    """
    if not isinstance(numbers, list) or not all(
        isinstance(item, (int, float)) for item in numbers
    ):
        raise TypeError("Expect list of numbers.")
    fig = plt.figure()
    plt.plot(numbers)
    with open(file_path, "wb") as file:
        pickle.dump(fig, file)
    with open(file_path, "rb") as file:
        loaded_fig = pickle.load(file)
    os.remove(file_path)
    return loaded_fig

import unittest
import matplotlib.pyplot as plt
import tempfile
import os
import random
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        random.seed(0)
    def test_case_1(self):
        # Test default case - correct file was generated & correct removal
        numbers = list(range(10))
        loaded_fig = task_func(numbers)
        self.assertIsInstance(
            loaded_fig,
            type(plt.figure()),
            "Returned object is not a Matplotlib figure.",
        )
        self.assertFalse(os.path.exists("save.pkl"), "Pickle file was not deleted.")
    def test_case_2(self):
        # Test when saving intermediate file to specified location
        numbers = list(range(10))
        path = os.path.join(self.temp_dir.name, "default.pkl")
        loaded_fig = task_func(numbers, path)
        self.assertIsInstance(
            loaded_fig,
            type(plt.figure()),
            "Returned object is not a Matplotlib figure.",
        )
        self.assertFalse(os.path.exists(path), "Pickle file was not deleted.")
    def test_case_3(self):
        # Test with floats
        numbers = [random.random() for _ in range(10)]
        loaded_fig = task_func(numbers)
        self.assertIsInstance(
            loaded_fig,
            type(plt.figure()),
            "Returned object is not a Matplotlib figure.",
        )
        self.assertFalse(os.path.exists("save.pkl"), "Pickle file was not deleted.")
    def test_case_4(self):
        # Test with a mix of positive, negative, integer, and floating numbers
        numbers = [1, -1, 2.5, -2.5, 3, -3, 4.5, -4.5]
        loaded_fig = task_func(numbers)
        self.assertIsInstance(
            loaded_fig,
            type(plt.figure()),
            "Returned object is not a Matplotlib figure.",
        )
        self.assertFalse(os.path.exists("save.pkl"), "Pickle file was not deleted.")
    def test_case_5(self):
        # Test with an empty list
        numbers = []
        loaded_fig = task_func(numbers)
        self.assertIsInstance(
            loaded_fig,
            type(plt.figure()),
            "Returned object is not a Matplotlib figure.",
        )
        self.assertFalse(os.path.exists("save.pkl"), "Pickle file was not deleted.")
    def test_case_6(self):
        # Function should fail when there's invalid input
        with self.assertRaises(TypeError):
            task_func("123")
        with self.assertRaises(TypeError):
            task_func(["1", "2", "3"])
        with self.assertRaises(TypeError):
            task_func([None, None, None])
    def tearDown(self):
        plt.close("all")
        self.temp_dir.cleanup()
