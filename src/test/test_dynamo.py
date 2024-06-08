from moto import mock_dynamodb
from unittest import TestCase
from lib.db.todo_db import TodoDB
from lib.db.dynamo_db import DynamoDB
import os
@mock_dynamodb
class TestDynamoDB(TestCase):
    def setUp(self) -> None:
        pass
    

