import json
from config.config_loader import ConfigLoader
import uuid

print('Loading function')

def lambda_handler(event, context):
    config = ConfigLoader().config()
    uuid_value = uuid.uuid4().hex
    
    return build_json_doc(uuid_value)

def build_json_doc(uuid):
    doc = { "uuid": uuid }
    return json.dumps(doc)

if __name__ == "__main__":
    class Event:
        def get(self, key):
            e = { 
                'key1': 'value1',
                'key2': 'value2',
                'key3': 'value3',
                }
            return e[key]
    context = 'context'
    event = Event()

    print(lambda_handler(event, context))

