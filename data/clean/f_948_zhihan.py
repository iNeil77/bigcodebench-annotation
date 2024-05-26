import subprocess
import os
import threading

def f_948(script_path: str, timeout: int = 60) -> str:
    """
    Execute a specified python code with a given timeout. If the script execution exceeds the timeout, it is terminated.

    Parameters:
    - script_path (str): The path to the Python code to be executed.
    - timeout (int): The maximum allowed time (in seconds) for the script execution. Default is 60 seconds.

    Returns:
    - str: A message indicating if the code was terminated due to timeout or executed successfully. The message is either "Script executed successfully." or "Terminating process due to timeout."

    Requirements:
    - subprocess
    - os
    - threading

    Examples:
    >>> f_948('/pathto/MyrScript.py')
    'Script executed successfully.'
    
    >>> f_948('/pathto/LongRunningScript.py', 30)
    'Terminating process due to timeout.'

    Note:
    - If the script was terminated due to timeout it will return "Script executed successfully.", otherwise "Terminating process due to timeout."

    Raise:
    - The code will raise FileNotFoundError if the file is not exist.
    """
    def target():
        subprocess.call(['python', script_path])

    thread = threading.Thread(target=target)
    thread.start()

    thread.join(timeout)

    if thread.is_alive():
        os.system(f'pkill -f "{script_path}"')
        thread.join()
        return 'Terminating process due to timeout.'
    else:
        return 'Script executed successfully.'

import unittest
from unittest.mock import patch
import time
import shutil

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'testdir_f_948'
        os.makedirs(self.test_dir, exist_ok=True)
        f = open(self.test_dir+"/script4.py","w")
        f.write("print('Hello from script4')")
        f.close()
        f = open(self.test_dir+"/script1.py","w")
        f.write("import time\ntime.sleep(10)\nprint('waiting')")
        f.close()
        f = open(self.test_dir+"/script2.py","w")
        f.close()
        f = open(self.test_dir+"/script3.py","w")
        f.write("import time\ntime.sleep(62)\nprint('waiting')")
        f.close()
        
        self.temp_dir = 'testdir_f_947/temp_dir'
        os.makedirs(self.temp_dir, exist_ok=True)
        

    def tearDown(self):
        # Clean up the test directory
        shutil.rmtree(self.test_dir)
        shutil.rmtree(self.temp_dir)
    
    @patch('subprocess.call', return_value=None)
    def test_case_1(self, mock_subprocess):
        # Test with a short-running script
        result = f_948('/path/to/short_script.py', 10)
        self.assertEqual(result, 'Script executed successfully.')

    
    def test_case_2(self):
        # Test with a long-running script and short timeout
        result = f_948(self.test_dir+"/script1.py", 3)
        self.assertEqual(result, 'Terminating process due to timeout.')

    @patch('subprocess.call', return_value=None)
    def test_case_3(self, mock_subprocess):
        # Test default timeout behavior
        result = f_948('/path/to/short_script.py')
        self.assertEqual(result, 'Script executed successfully.')

    def test_case_4(self):
        # Test with a long-running script and long timeout
        result = f_948(self.test_dir+"/script1.py", 20)
        self.assertEqual(result, 'Script executed successfully.')

    def test_case_5(self):
        # Test with a long-running script and default timeout
        result = f_948(self.test_dir+"/script3.py")
        self.assertEqual(result, 'Terminating process due to timeout.')



if __name__ == "__main__":
    run_tests()