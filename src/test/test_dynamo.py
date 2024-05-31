from unittest import TestCase
from lib.dynamo import dynamo_connect

class test_dynamo(TestCase):
    """
    Test the dynamo connection
    """
    def test_connection(self):
        self.assertTrue(dynamo_connect())
        return 