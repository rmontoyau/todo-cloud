from unittest import TestCase
from handlers.get_all_items import test_connection

class TestGetAllItems(TestCase):
    def test_dynamo_connection(self):
        self.assertTrue(test_connection())
        print("test passed")