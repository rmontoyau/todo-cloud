from moto import mock_dynamodb
from unittest import TestCase
from lib.account import Account
from lib.db.dynamo_db import DynamoDB
import os
@mock_dynamodb
class TestUser(TestCase):
    def setUp(self) -> None:
        os.environ["ENVIRONMENT"] = "test"
        DynamoDB().create_tables()
        self.account = Account()
        self.account.create("user_1", "user1", "lastname 1", "user1@example.com")
        self.account.create("user_2", "user2", "lastname 2", "user2@example.com")
        self.account.create("user_3", "user3", "lastname 3", "user3@example.com")
    
    def test_createUser(self):
        _account = self.account.create("user_4", "user4", "lastname 4", "user4@example.com")
        assert _account != None
        #must return None if user already exists
        _account = self.account.create("user_4", "user5", "lastname 5", "user5@example.com")
        assert _account == None

    def test_getUser(self):
        _account = self.account.get("user_1")
        assert _account != None
        assert _account["user_name"] == "user_1"
        assert _account["account"]["name"] == "user1"
        assert _account["account"]["last_name"] == "lastname 1"
        assert _account["account"]["email"] == "user1@example.com"
    
    def test_updateUser(self):
        _account = self.account.update("user_1", "user1_updated", "lastname 1_updated", "user1_updated@example.com")
        _account = self.account.get("user_1")
        print(f" getting account: {_account}")
        assert _account != None
        assert _account["user_name"] == "user_1"
        assert _account["account"]["name"] == "user1_updated"
        assert _account["account"]["last_name"] == "lastname 1_updated"
        assert _account["account"]["email"] == "user1_updated@example.com"

    def test_deleteUser(self):
        self.account.delete("user_1")
        _account = self.account.get("user_1")
        assert _account == None
        _account = self.account.get("user_2")
        assert _account != None
        _account = self.account.get("user_3")
        assert _account != None
        