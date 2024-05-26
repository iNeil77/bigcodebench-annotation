from django.http import HttpResponse
from django.conf import settings
import random
import time

def task_func(data, min_delay, max_delay):
    """
    After a random delay, generate a Django HttpResponse with JSON data to simulate the latency of the network.
    
    Parameters:
    data (str): The data to be included in the response body.
    min_delay (int): The minimum delay in seconds.
    max_delay (int): The maximum delay in seconds.
    
    Returns:
    HttpResponse: A Django HttpResponse with JSON data.
    
    Requirements:
    - django
    - random
    - time

    Example:
    >>> import json
    >>> random.seed(0)
    >>> response = task_func(json.dumps({"Sample-Key": "Sample-Value"}), 1, 5)
    >>> response.status_code
    200
    >>> json.loads(response.content)
    {"Sample-Key": "Sample-Value"}
    """
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)
    response = HttpResponse(data, content_type='application/json')
    return response

import unittest
import json
import random
if not settings.configured:
    settings.configure(DEBUG=True)
class TestCases(unittest.TestCase):
    def test_case_1(self):
        random.seed(0)
        data = json.dumps({"key": "value"})
        response = task_func(data, 1, 2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"key": "value"})
    def test_case_2(self):
        random.seed(0)
        data = json.dumps({"test": "data", "sample": "value"})
        response = task_func(data, 0, 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"test": "data", "sample": "value"})
    def test_case_3(self):
        random.seed(0)
        data = json.dumps({"hello": "world"})
        response = task_func(data, 1, 3)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"hello": "world"})
    def test_case_4(self):
        random.seed(0)
        data = json.dumps({})
        response = task_func(data, 0, 0)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {})
    def test_case_5(self):
        random.seed(0)
        data = json.dumps({"a": 1, "b": 2, "c": 3})
        response = task_func(data, 2, 4)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"a": 1, "b": 2, "c": 3})
