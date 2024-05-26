import sys
import sqlite3

# Constants
PATH_TO_APPEND = "path/to/whatever"
DATABASE = "path/to/database.db"


def f_835(path_to_append=PATH_TO_APPEND, database=DATABASE):
    """
    This function appends a given path to sys.path and updates an SQLite database with the path, 
    creating the table if needed and avoiding duplicates.

    Parameters:
    - path_to_append (str): A file system path to be appended to sys.path and inserted
      into the SQLite database. Defaults to 'path/to/whatever' if not specified.
    - database (str): The file system path to the SQLite database file. Defaults to
      'path/to/database.db' if not provided. The function interacts with this database
      to store the path.

    Returns:
    - str: The path that was appended to sys.path and inserted into the database.

    Requirements:
    - sys
    - sqlite3


    Examples:
    >>> f_835('path/to/new_directory', 'path/to/new_database.db')
    'path/to/new_directory'
    >>> f_835()
    'path/to/whatever'
    """
    sys.path.append(path_to_append)

    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS paths (path TEXT UNIQUE)")
    cur.execute("INSERT OR IGNORE INTO paths (path) VALUES (?)", (path_to_append,))
    conn.commit()
    conn.close()

    return path_to_append


import unittest
import sqlite3
import os
import shutil


class TestCases(unittest.TestCase):
    """Test cases for f_835"""

    def setUp(self):
        path_to_create = os.path.dirname(PATH_TO_APPEND)
        os.makedirs(path_to_create, exist_ok=True)
        self.test_db = DATABASE

    def test_basic_path_insertion(self):
        """Test the function when a path is provided."""
        test_path = "path/to/test/path"
        result = f_835(test_path, self.test_db)
        self.assertEqual(result, test_path)

        # Check the database to ensure the path was saved
        conn = sqlite3.connect(self.test_db)
        cur = conn.cursor()
        cur.execute("SELECT * FROM paths WHERE path=?", (test_path,))
        fetched_path = cur.fetchone()
        conn.close()

        self.assertIsNotNone(fetched_path)
        self.assertEqual(fetched_path[0], test_path)

    def test_existing_path(self):
        """Test the function when an existing path is provided."""
        # Insert an existing path
        existing_path = "existing/path"
        f_835(existing_path, self.test_db)

        # Attempt to insert the same path again
        result = f_835(existing_path, self.test_db)
        self.assertEqual(result, existing_path)

        # Check the database to ensure there's only one entry for the existing path
        conn = sqlite3.connect(self.test_db)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM paths WHERE path=?", (existing_path,))
        count = cur.fetchone()[0]
        conn.close()

        self.assertEqual(count, 1)

    def test_multiple_paths(self):
        """Test the function when multiple paths are provided."""
        paths = ["path1", "path2", "path3"]
        for path in paths:
            result = f_835(path, self.test_db)
            self.assertEqual(result, path)

        # Check the database to ensure all paths are saved
        conn = sqlite3.connect(self.test_db)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM paths")
        count = cur.fetchone()[0]
        conn.close()

        self.assertEqual(count, len(paths))

    def test_database_creation(self):
        """Test the function when the database doesn't exist."""
        new_db = "path/to/new_test_database.db"
        test_path = "path/to/new"
        os.makedirs(os.path.dirname(test_path), exist_ok=True)
        result = f_835(test_path, new_db)
        self.assertEqual(result, test_path)

        # Check the new database to ensure the path was saved
        conn = sqlite3.connect(new_db)
        cur = conn.cursor()
        cur.execute("SELECT * FROM paths WHERE path=?", (test_path,))
        fetched_path = cur.fetchone()
        conn.close()

        self.assertIsNotNone(fetched_path)
        self.assertEqual(fetched_path[0], test_path)

    def test_invalid_database(self):
        """Test the function when an invalid database is provided."""
        invalid_db = "invalid/path/database.db"
        test_path = "test/path"
        with self.assertRaises(sqlite3.OperationalError):
            f_835(test_path, invalid_db)

    def tearDown(self):
        # Cleanup the test databases
        dbs_to_remove = ["path/to/database.db", "path/to/new_test_database.db"]
        for db in dbs_to_remove:
            if os.path.exists(db):
                os.remove(db)

        # Cleanup the test directories
        dirs_to_remove = ["path/to/whatever", "path/to", "path"]
        for dir_path in dirs_to_remove:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)


def run_tests():
    """Run all testscases"""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
