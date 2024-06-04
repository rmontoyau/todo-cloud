from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 
#from  src.lib.db.todo_tables import create_tables
import json
#create_tables()

data = {
    "id": 1,
    "user_name": "user",
    "user" : {
        "name": "rudy",
        "rights" : ["admin", "user"],
        "tasks": [1,2,3]
    },
    "tasks": [
        {
            "id": 1,
            "title": "prueba",
            "completed": False
        },
        {
            "id": 2,
            "title": "prueba2",
            "completed": True
        },
        {
            "id": 3,
            "title": "prueba3",
            "completed": False,
            "list": [
                {
                    "name": "rudy",
                    "age": 19
                },
                {
                    "name": "Alonso",
                    "age": 21
                }
            ]
        }
    ]

}
serialized = {"id": {"N": "1"}, "user_name": {"S": "user"}, 
              "user": {"M": {"name": {"S": "rudy"}, "rights": {"SS": ["admin", "user"]}, "tasks": {"NS": ["1", "2", "3"]}}}, 
              "tasks": {"L": [{"id": {"N": "1"}, "title": {"S": "prueba"}, "completed": {"BOOL": False}}, 
                              {"id": {"N": "2"}, "title": {"S": "prueba2"}, "completed": {"BOOL": True}}, 
                              {"id": {"N": "3"}, "title": {"S": "prueba3"}, "completed": {"BOOL": False}, 
                        "list": {"L": [{"name": {"S": "rudy"}, "age": {"N": "19"}}, {"name": {"S": "Alonso"}, "age": {"N": "21"}}]}}]}}

def serialize(json_data):
    if type(json_data) is dict:
        for item, value in json_data.items():
            if type(value) is dict:
                json_data[item] = {"M" : serialize(value)}
            if type(value) is list:
                if type(value[0]) is dict:
                    json_data[item] = {"L" : serialize(value)}
                elif type(value[0]) is str:
                    json_data[item] = {"SS" : value}
                else:
                    json_data[item] = {"NS" : list(map(lambda x: str(x),value))}
            if type(value) is str:
                json_data[item] = {"S" : value}
            if type(value) is int:
                json_data[item] = {"N" : str(value)}
            if type(value) is bool:
                json_data[item] = {"BOOL" : value}
    if type(json_data) is list:
        for i, item in enumerate(json_data):
            json_data[i] = serialize(item)     
    return json_data

def deserialize(dynamo_data):
    if type(dynamo_data) is dict:
        for item, value in dynamo_data.items():
            if type(value) is dict:
                if "S" in value:
                    dynamo_data[item] = value["S"]
                if "N" in value:
                    dynamo_data[item] = int(value["N"])
                if "BOOL" in value:
                    dynamo_data[item] =  value["BOOL"] 
                if "M" in value:
                    dynamo_data[item] = deserialize(value["M"])
                if "L" in value:
                    dynamo_data[item] = deserialize(value["L"])
                if "SS" in value:
                    dynamo_data[item] = value["SS"]
                if "NS" in value:
                    dynamo_data[item] = list(map(lambda x: int(x), value["NS"]))
           
    if type(dynamo_data) is list:
        for i, item in enumerate(dynamo_data):
            dynamo_data[i] = deserialize(item)
    return dynamo_data

#result = serialize(data)
#print(json.dumps(result))

des = deserialize(serialized)
print(json.dumps(des))
