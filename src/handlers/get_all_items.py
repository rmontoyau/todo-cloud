from lib.dynamo import get_all_items,dynamo_connect
def getAllItemsHandler(event, context):
    return get_all_items()

def test_connection():
   return dynamo_connect()