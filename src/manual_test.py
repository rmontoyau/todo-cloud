#files used for do manual test
from lib.db.todo_db import TodoDB
from lib.db.dynamo_db import DynamoDB
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 
#dynamo = DynamoDB()
#dynamo.create_tables()
from lib.account import Account
account = Account()
#account.create("user_1","Rudy", "Alonso", "email@email.com")
#account.create("account_2","account 2", "account2", "email@email.com")
#account.update("account_1", "Rudi", "Alonso", "email")


from lib.task import Task
task = Task("user_1")
#task.add("task_1", "description_1", "05/05/2024 15:00:00")
#task.add("task_2", "description_2", "05/05/2024 15:00:00")
task.update_status("task_1")
#print(account.get("user_1"))
print(task.get("task_1"))
