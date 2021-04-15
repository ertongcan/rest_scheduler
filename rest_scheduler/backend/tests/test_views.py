import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        response = self.client.post('/login/', {'name': 'perdo', 'passwd': 'perdo'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)