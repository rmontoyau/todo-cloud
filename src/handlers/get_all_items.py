import json
from lib.dynamo import get_all_items
def getAllItemsHandler(event, context):
    return get_all_items()