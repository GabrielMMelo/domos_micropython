import json
import os


def write_settings(obj):
    with open('config', 'w') as file:
        file.write(json.dumps(obj))

def read_settings():
    if 'config' not in os.listdir():
        return {}
    with open('config') as file:
        settings = json.loads(file.read())
    return settings
