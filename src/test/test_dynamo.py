from moto import mock_dynamodb
from unittest import TestCase
from lib.db.todo_db import TodoDB
import os
@mock_dynamodb
class TestDynamoDB(TestCase):
    def setUp(self) -> None:
        os.environ["ENVIRONMENT"] = "test"
        self.todo = TodoDB()
   
    def test_add_todo(self):
        data = {
            "id" : "1",
            "user_name": "user 1",
            "is_active": True
        }
        todo = self.todo.add(data)
        assert todo["ResponseMetadata"]["HTTPStatusCode"] == 200
    
    def test_get_todo(self):
        data = {
            "id" : "1",
            "user_name": "user 1",
            "is_active": True
        }
        todo = self.todo.add(data)
        data = {
            "id": "1",
            "user_name": "user 1",
        }
        todo = self.todo.get(data)
        assert todo["user_name"] == "user 1"