import json


def write_settings(obj):
    with open('config', 'w') as file:
        file.write(json.dumps(obj))

def read_settings():
    with open('config') as file:
        settings = json.loads(file.read())
    return settings
