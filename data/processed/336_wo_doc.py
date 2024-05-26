import json
import urllib.parse
import hmac
import hashlib

def task_func(req_data, secret_key):
    """
    Signs the specified request data with a secret key using HMAC SHA256, then URL encodes the signature and replace spaces with '+'.

    Parameters:
        req_data (dict): The request data to be signed. It should be a dictionary.
        secret_key (str): The secret key used for signing the request data.

    Returns:
        str: The URL encoded HMAC signature of the request data.

    Raises:
        TypeError: If `req_data` is not a dictionary.

    Requirements:
    - json
    - urllib.parse
    - hmac
    - hashlib

    Examples:
    >>> secret_key = 'my_secret_key'
    >>> isinstance(task_func({'test': 'just a test'}, secret_key), str)
    True
    >>> isinstance(task_func({'another': 'data', 'key': 123}, secret_key), str)
    True
    """
    if not isinstance(req_data, dict):
        raise TypeError("req_data must be a dictionary")
    json_req_data = json.dumps(req_data)
    hmac_obj = hmac.new(secret_key.encode(), json_req_data.encode(), hashlib.sha256)
    hmac_signature = hmac_obj.hexdigest()  # Use hexdigest for a hexadecimal representation
    url_encoded_signature = urllib.parse.quote_plus(hmac_signature)
    return url_encoded_signature

import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        """Set up common test data and secret key."""
        self.secret_key = 'test_secret_key'
    
    def compute_expected_signature(self, req_data):
        """Compute the expected HMAC signature for comparison in tests."""
        json_req_data = json.dumps(req_data)
        hmac_obj = hmac.new(self.secret_key.encode(), json_req_data.encode(), hashlib.sha256)
        hmac_hex = hmac_obj.hexdigest()
        url_encoded_signature = urllib.parse.quote_plus(hmac_hex)
        
        return url_encoded_signature
    def test_return_type(self):
        """Ensure the function returns a string."""
        result = task_func({'key': 'value'}, self.secret_key)
        self.assertIsInstance(result, str)
    def test_known_data_signature(self):
        """Validate the HMAC signature against a known output for specific data."""
        known_data = {'known': 'data'}
        expected_signature = self.compute_expected_signature(known_data)
        result = task_func(known_data, self.secret_key)
        self.assertEqual(result, expected_signature)
    def test_empty_data(self):
        """Verify the function behaves correctly with empty input data."""
        result = task_func({}, self.secret_key)
        expected_signature_for_empty_data = self.compute_expected_signature({})
        self.assertEqual(result, expected_signature_for_empty_data)
    def test_complex_data_structure(self):
        """Check the function's behavior with complex nested data structures."""
        complex_data = {'list': [1, 2, 3], 'nested': {'key': 'value'}}
        result = task_func(complex_data, self.secret_key)
        expected_signature = self.compute_expected_signature(complex_data)
        self.assertEqual(result, expected_signature)
    def test_non_dict_input(self):
        """Ensure non-dictionary inputs raise the appropriate error."""
        with self.assertRaises(TypeError):
            task_func('not a dict', self.secret_key)
    def test_different_data_different_signatures(self):
        """Test that different data results in different HMAC signatures."""
        data1 = {'data': 'test1'}
        data2 = {'data': 'test2'}
        result1 = task_func(data1, self.secret_key)
        result2 = task_func(data2, self.secret_key)
        expected_signature1 = self.compute_expected_signature(data1)
        expected_signature2 = self.compute_expected_signature(data2)
        self.assertEqual(result1, expected_signature1)
        self.assertEqual(result2, expected_signature2)
        self.assertNotEqual(result1, result2)
    def test_consistent_hash_with_same_input(self):
        """Test that hashing the same data multiple times results in the same hashes."""
        data = {'consistent': 'data'}
        result1 = task_func(data, self.secret_key)
        result2 = task_func(data, self.secret_key)
        expected_signature = self.compute_expected_signature(data)
        self.assertEqual(result1, expected_signature)
        self.assertEqual(result2, expected_signature)
        self.assertEqual(result1, result2)
