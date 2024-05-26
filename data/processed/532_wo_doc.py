import sqlite3
import pandas as pd


def task_func(db_name, table_name):
    """
    Plot the relationship between the first and second numerical columns of an SQLite3 table, after excluding 'id' column.

    Parameters:
    - db_name (str): The absolute path to the SQLite3 database.
    - table_name (str): The name of the table to plot from.

    Returns:
    - matplotlib.axes._axes.Axes: Scatterplot with column name labeled on their respective axes.

    Raises:
    - ValueError: If the table has less than two numerical columns.
    
    Requirements:
    - sqlite3
    - pandas

    Example:
    >>> ax = task_func('/path/to/database/test.db', 'People')
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(0.9400000000000001, 0, '0.94'), ... ]
    """
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f"SELECT * from {table_name}", conn)
    numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    if "id" in numerical_columns:
        numerical_columns.remove("id")
    if len(numerical_columns) < 2:
        raise ValueError("The table must have at least two numerical columns to plot.")
    ax = df.plot.scatter(x=numerical_columns[0], y=numerical_columns[1])
    return ax

import unittest
import sqlite3
import os
import matplotlib.pyplot as plt
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_db_path = os.path.join(self.temp_dir.name, "test.db")
        self.another_test_db_path = os.path.join(self.temp_dir.name, "another_test.db")
        self.nonexistent_db_path = os.path.join(self.temp_dir.name, "nonexistent.db")
        # Setup for 'test.db'
        with sqlite3.connect(self.test_db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE People (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, height REAL)"
            )
            self.data = [
                ("Alice", 25, 5.5),
                ("Bob", 30, 6.0),
                ("Charlie", 35, 5.8),
                ("David", 40, 6.2),
                ("Eve", 45, 5.9),
                ("Frank", 50, 5.6),
            ]
            cur.executemany(
                "INSERT INTO People (name, age, height) VALUES (?, ?, ?)", self.data
            )
        # Setup for 'another_test.db'
        with sqlite3.connect(self.another_test_db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE Animals (id INTEGER PRIMARY KEY, name TEXT, lifespan INTEGER, weight REAL)"
            )
            animal_data = [
                ("Dog", 13, 30.0),
                ("Cat", 15, 4.5),
                ("Elephant", 70, 6000.0),
                ("Dolphin", 20, 150.0),
            ]
            cur.executemany(
                "INSERT INTO Animals (name, lifespan, weight) VALUES (?, ?, ?)",
                animal_data,
            )
    def tearDown(self):
        self.temp_dir.cleanup()
        plt.close("all")
    def test_case_1(self):
        # Test basic functionality
        ax = task_func(self.test_db_path, "People")
        self.assertEqual(ax.get_xlabel(), "age")
        self.assertEqual(ax.get_ylabel(), "height")
        self.assertEqual(len(ax.collections[0].get_offsets()), 6)
    def test_case_2(self):
        # Test handling non-existent table
        with self.assertRaises(Exception):
            task_func(self.test_db_path, "NonExistentTable")
    def test_case_3(self):
        # Test handling non-existent db
        with self.assertRaises(Exception):
            task_func(self.nonexistent_db_path, "People")
    def test_case_4(self):
        # Table with removed numerical column should raise error
        with sqlite3.connect(self.test_db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                f"CREATE TABLE temp AS SELECT id, name, age FROM People WHERE name IN ('Alice', 'Bob')"
            )
            cur.execute(f"DROP TABLE People")
            cur.execute(f"ALTER TABLE temp RENAME TO People")
        with self.assertRaises(Exception):
            task_func(self.test_db_path, "People")
        # Revert changes
        with sqlite3.connect(self.test_db_path) as conn:
            cur = conn.cursor()
            cur.execute(f"CREATE TABLE temp AS SELECT * FROM People")
            cur.execute(f"DROP TABLE People")
            cur.execute(
                f"CREATE TABLE People (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, height REAL)"
            )
            cur.executemany(
                f"INSERT INTO People (name, age, height) VALUES (?, ?, ?)", self.data
            )
    def test_case_5(self):
        # Test another set of data/db
        ax = task_func(self.another_test_db_path, "Animals")
        self.assertEqual(ax.get_xlabel(), "lifespan")
        self.assertEqual(ax.get_ylabel(), "weight")
        self.assertEqual(len(ax.collections[0].get_offsets()), 4)
    def test_case_6(self):
        # Test handling of a table with only one numerical column
        with sqlite3.connect(self.test_db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE SingleNumCol (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
            )
        with self.assertRaises(Exception):
            task_func(self.test_db_path, "SingleNumCol")
    def test_case_7(self):
        # Test handling of a table with no numerical columns
        with sqlite3.connect(self.test_db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE NoNumCols (id INTEGER PRIMARY KEY, name TEXT, description TEXT)"
            )
        with self.assertRaises(Exception):
            task_func(self.test_db_path, "NoNumCols")
    def test_case_8(self):
        # Test a table where 'id' is the only numerical column
        with sqlite3.connect(self.test_db_path) as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE OnlyIDNum (id INTEGER PRIMARY KEY, name TEXT)")
        with self.assertRaises(Exception):
            task_func(self.test_db_path, "OnlyIDNum")
    def test_case_9(self):
        # Test plotting when the first two numerical columns are not 'id', 'age', or 'height'
        with sqlite3.connect(self.another_test_db_path) as conn:
            cur = conn.cursor()
            custom_data = [("Lion", 15, 190.5), ("Tiger", 20, 220.0)]
            cur.executemany(
                "INSERT INTO Animals (name, lifespan, weight) VALUES (?, ?, ?)",
                custom_data,
            )
        ax = task_func(self.another_test_db_path, "Animals")
        self.assertEqual(ax.get_xlabel(), "lifespan")
        self.assertEqual(ax.get_ylabel(), "weight")
        self.assertGreaterEqual(len(ax.collections[0].get_offsets()), 2)
