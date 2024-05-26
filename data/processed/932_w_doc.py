import numpy as np
import matplotlib.pyplot as plt
import string

# Constants
ALPHABET = list(string.ascii_lowercase)

def task_func(word):
    """
    Draws a bar chart representing the positions of each letter in the given word 
    within the English alphabet using numpy and matplotlib.pyplot.
    
    Parameters:
    word (str): The word whose letters' positions will be plotted. 
                Should contain only lowercase alphabetic characters.
                
    Returns:
    Axes: A matplotlib.axes._axes.Axes object representing the generated plot.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    
    Constants:
    - ALPHABET: A list containing all lowercase letters of the English alphabet.
    
    Examples:
    >>> ax = task_func('abc')
    >>> ax = task_func('hello')
    
    Note: 
    The function uses the index of each letter in the English alphabet to represent its position.
    For example, 'a' will be represented by 1, 'b' by 2, and so on.
    """
    if not all(char in ALPHABET for char in word):
        raise ValueError("The word should contain only lowercase alphabetic characters.")
    letter_positions = np.array(list(map(lambda x: ALPHABET.index(x) + 1, word)))
    fig, ax = plt.subplots()
    ax.bar(np.arange(len(letter_positions)), letter_positions)
    ax.set_xlabel('Letter Index')
    ax.set_ylabel('Alphabetical Position')
    ax.set_title('Alphabetical Position of Letters in Word')
    plt.show()
    return ax

import unittest
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        ax = task_func('abc')
        self.assertIsInstance(ax, Axes, "The returned object is not an instance of Axes.")
        self.assertEqual(ax.patches[0].get_height(), 1, "The height of the first bar should be 1.")
        self.assertEqual(ax.patches[1].get_height(), 2, "The height of the second bar should be 2.")
        self.assertEqual(ax.patches[2].get_height(), 3, "The height of the third bar should be 3.")
    
    def test_case_2(self):
        ax = task_func('xyz')
        self.assertIsInstance(ax, Axes, "The returned object is not an instance of Axes.")
        self.assertEqual(ax.patches[0].get_height(), 24, "The height of the first bar should be 24.")
        self.assertEqual(ax.patches[1].get_height(), 25, "The height of the second bar should be 25.")
        self.assertEqual(ax.patches[2].get_height(), 26, "The height of the third bar should be 26.")
        
    def test_case_3(self):
        ax = task_func('ace')
        self.assertIsInstance(ax, Axes, "The returned object is not an instance of Axes.")
        self.assertEqual(ax.patches[0].get_height(), 1, "The height of the first bar should be 1.")
        self.assertEqual(ax.patches[1].get_height(), 3, "The height of the second bar should be 3.")
        self.assertEqual(ax.patches[2].get_height(), 5, "The height of the third bar should be 5.")
        
    def test_case_4(self):
        ax = task_func('bd')
        self.assertIsInstance(ax, Axes, "The returned object is not an instance of Axes.")
        self.assertEqual(ax.patches[0].get_height(), 2, "The height of the first bar should be 2.")
        self.assertEqual(ax.patches[1].get_height(), 4, "The height of the second bar should be 4.")
        
    def test_case_5(self):
        with self.assertRaises(ValueError):
            task_func('a1b')
