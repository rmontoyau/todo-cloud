from moto import mock_dynamodb
from unittest import TestCase
from lib.db.config_db import configDB
from lib.db.dynamo_db import DynamoDB
import os
@mock_dynamodb
class TestDynamoDB(TestCase):
    def setUp(self) -> None:
        os.environ["ENVIRONMENT"] = "test"
        DynamoDB().create_tables()
        self.config = configDB()

    def test_insert(self):
        assert self.config.set("val", "1") == True
        assert self.config.set("val1", "2") == True
        assert self.config.set("count", "3") == True
        assert self.config.set("count", "5") == True
        assert self.config.set("index", "1") == True
        assert self.config.get("val") == "1"
        assert self.config.get("val1") == "2"
        assert self.config.get("count") == "5"
        assert self.config.get("index") == "1"
