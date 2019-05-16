import json
from config.config_loader import ConfigLoader

print('Loading function')


def lambda_handler(event, context):
    config = ConfigLoader().config()
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + config['NAME'])
    print("value2 = " + event.get('key2'))
    print("value3 = " + event.get('key3'))
    return event.get('key1')  # Echo back the first key value
    #raise Exception('Something went wrong')

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

