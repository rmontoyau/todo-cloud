from unittest import TestCase
from lib.db.todo_db import TodoDB
from dotenv import load_dotenv

load_dotenv() 

class TestTodoDB(TestCase):
    def test_init(self):
        db = TodoDB()
    
    def test_add_todo(self):
        db = TodoDB()
        data = {
            "id" : "1",
            "user_name": "user 1",
            "is_active": True
        }
        todo = db.add(data)
        assert todo["ResponseMetadata"]["HTTPStatusCode"] == 200

        data = {
            "id": "1",
            "user_name": "user 1",
        }
        item = db.get(data)
        print(item)