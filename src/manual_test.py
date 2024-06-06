#files used for do manual test
from lib.db.todo_db import TodoDB
from lib.db.dynamo_db import DynamoDB
from lib.db.config_db import configDB
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 
#dynamo = DynamoDB()
#dynamo.create_tables()
configDB.set("init","0")
configDB.set("init","1")
print(configDB.get("init"))