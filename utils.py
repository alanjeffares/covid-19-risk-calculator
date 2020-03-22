import json

def json_loader(name):
    """Loads json from file path"""
    with open(name) as file:
        json_file = json.load(file)
    return json_file