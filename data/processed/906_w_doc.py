import numpy as np
import matplotlib.pyplot as plt

def task_func(letters, repetitions, colors):
    """
    Create a bar chart to visualize the frequency of each letter in a flattened list 
    formed by multiple repetitions of the original list. Each repetition of the list 
    is associated with a different color in the chart.
    
    Note:
    - Generate a bar chart for the frequency of letters, where each letter's frequency
      is determined by its number of repetitions.
    - Each letter's bar in the chart is colored according to the specified color.
    - The length of the list `colors` should match the number of repetitions of `letters`.
    - The lists 'letters' and 'colors' cannot be empty.
    
    Parameters:
    - letters (list of str): A list of unique letters to be visualized.
    - repetitions (list of int): A list of the number of times each letter is repeated.
      Must be the same length as `letters`.
    - colors (list of str): A list of colors for the bars corresponding to each letter.
      Must be the same length as `letters`.
    
    Returns:
    - Returns the Matplotlib Axes object representing the created bar chart, with the x-axis labeled 'Letters', y-axis labeled 'Frequency', and title 'Frequency of Letters'.
    
    Raises:
    - ValueError: If the lengths of the input lists do not match or if any list is empty.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    
    Example:
    >>> ax = task_func(['A', 'B', 'C'], [3, 5, 2], ['red', 'green', 'blue'])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    if len(letters) != len(repetitions) or len(letters) != len(colors) or len(letters) == 0:
        raise ValueError("All lists must be the same length and non-empty.")
    counts = np.array(repetitions)
    fig, ax = plt.subplots()
    ax.bar(letters, counts, color=colors)
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Letters')
    return ax

import unittest
class TestCases(unittest.TestCase):
    
    def test_basic_input(self):
        ax = task_func(['A', 'B', 'C'], [3, 5, 2], ['red', 'green', 'blue'])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Frequency of Letters")
        self.assertEqual(ax.get_xlabel(), "Letters")
        self.assertEqual(ax.get_ylabel(), "Frequency")
        expected_colors = ['red', 'green', 'blue']
        for patch, expected_color in zip(ax.patches, expected_colors):
            self.assertEqual(patch.get_facecolor(), plt.cm.colors.to_rgba(expected_color))
        expected_counts = [3, 5, 2]
        for patch, expected_count in zip(ax.patches, expected_counts):
            self.assertEqual(patch.get_height(), expected_count)
    
    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            task_func(['A', 'B'], [3], ['red', 'green'])
    
    def test_empty_lists(self):
        with self.assertRaises(ValueError):
            task_func([], [], [])
    
    def test_single_letter(self):
        ax = task_func(['Z'], [1], ['purple'])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Frequency of Letters")
        self.assertEqual(ax.get_xlabel(), "Letters")
        self.assertEqual(ax.get_ylabel(), "Frequency")
        self.assertEqual(ax.patches[0].get_facecolor(), plt.cm.colors.to_rgba('purple'))
        self.assertEqual(ax.patches[0].get_height(), 1)
    
    def test_multiple_repetitions(self):
        ax = task_func(['D', 'E', 'F'], [10, 20, 15], ['cyan', 'magenta', 'yellow'])
        self.assertIsInstance(ax, plt.Axes)
        expected_counts = [10, 20, 15]
        for patch, expected_count in zip(ax.patches, expected_counts):
            self.assertEqual(patch.get_height(), expected_count)
