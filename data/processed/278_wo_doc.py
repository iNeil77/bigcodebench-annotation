import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
import os

def task_func(file_path, onpick):
    """
    Draw the color histogram of an image in 3D and call a function when a data point is selected.

    Parameters:
    file_path (str): The path to the image file.
    onpick (function): The function to be called when a data point is picked.

    Returns:
    matplotlib.axes.Axes: The Axes object of the 3D plot.

    Raises:
    FileNotFoundError: If the image file does not exist.
    
    Requirements:
    - matplotlib
    - mpl_toolkits.mplot3d
    - numpy
    - cv2
    - os
    - tempfile
    
    Example:
    >>> def onpick(event):
    ...     ind = event.ind
    ...     print(f'You picked data point(s) {ind}')
    >>> np.random.seed(42)
    >>> dummy_img_path = 'image.jpg'
    >>> dummy_img = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
    >>> cv2.imwrite(dummy_img_path, dummy_img)
    True
    >>> ax = task_func('image.jpg', onpick)
    >>> os.remove(dummy_img_path)
    """
    if not os.path.exists(str(file_path)):
        raise FileNotFoundError(f"No file found at {str(file_path)}")
    img = cv2.imread(str(file_path))
    color = ('b', 'g', 'r')
    fig = plt.figure()
    ax = Axes3D(fig)
    for i, col in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        ax.plot(np.arange(256), hist, color=col)
    fig.canvas.mpl_connect('pick_event', onpick)
    return ax

import unittest
import numpy as np
import cv2
import os
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a dummy image for testing
        np.random.seed(42)
        self.dummy_img_path = os.path.join(tempfile.mkdtemp(), 'test_image.jpg')
        dummy_img = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
        cv2.imwrite(self.dummy_img_path, dummy_img)
    def tearDown(self):
        # Cleanup the dummy image
        if os.path.exists(self.dummy_img_path):
            os.remove(self.dummy_img_path)
    def test_valid_input(self):
        def dummy_onpick(event):
            pass
        ax = task_func(self.dummy_img_path, dummy_onpick)
        self.assertIsInstance(ax, Axes3D)
    def test_invalid_file_path(self):
        def dummy_onpick(event):
            pass
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent.jpg', dummy_onpick)
    def test_onpick_function(self):
        # This test requires manual verification of onpick functionality
        def dummy_onpick(event):
            print(f"Dummy onpick called with event: {event}")
        ax = task_func(self.dummy_img_path, dummy_onpick)
        self.assertIsInstance(ax, Axes3D)
