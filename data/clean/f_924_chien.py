import pandas as pd
from sklearn.linear_model import LinearRegression

DATA = {
    "Area_String": ["1,000", "2,000", "3,000", "4,000", "5,000"],
    "Price": [100, 200, 300, 400, 500],
}


def f_924(area_string, data=DATA):
    """
    Predicts the price based on a given area after training a linear regression model.

    Parameters:
    - area_string (str): A string representing the area (in square units) for
    which the price needs to be predicted. The string may contain commas.
    - data (dict): Optional. A dictionary with keys 'Area_String' and 'Price'
    representing area values (as strings) and their corresponding prices. Defaults to a predefined dataset.

    Returns:
    - float: The predicted price for the given area.

    Requirements:
    - pandas
    - sklearn.linear_model

    Example:
    >>> f_924('6,000')
    600.0
    """
    # Convert area strings to float and prepare data for the model
    df = pd.DataFrame(data)
    df["Area_Float"] = df["Area_String"].str.replace(",", "").astype(float)

    # Train the linear regression model
    X = df[["Area_Float"]]
    Y = df["Price"]
    model = LinearRegression()
    model.fit(X, Y)

    # Predict the price for the given area string
    area_float = float(area_string.replace(",", ""))
    prediction_data = pd.DataFrame([area_float], columns=["Area_Float"])
    price_predicted = model.predict(prediction_data)

    return price_predicted[0]


import unittest


class TestCases(unittest.TestCase):
    """Test cases for f_924"""

    def test_correctness(self):
        """Test correctness."""
        self.assertAlmostEqual(f_924("6,000"), 600, delta=10)
        self.assertAlmostEqual(f_924("7,000"), 700, delta=10)

    def test_input_formats(self):
        """Test input formats."""
        self.assertAlmostEqual(f_924("6,500"), 650, delta=10)
        self.assertAlmostEqual(f_924("6500"), 650, delta=10)

    def test_custom_data(self):
        """Test custom data."""
        custom_data = {
            "Area_String": ["10", "20", "30", "40", "50"],
            "Price": [1, 2, 3, 4, 5],
        }
        self.assertAlmostEqual(f_924("60", data=custom_data), 6, delta=0.1)

    def test_existing_area(self):
        """Test existing area."""
        self.assertAlmostEqual(f_924("5,000"), 500, delta=5)

    def test_large_area(self):
        """Test large area."""
        self.assertAlmostEqual(f_924("100,000"), 10000, delta=100)


# Running the test cases
def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
