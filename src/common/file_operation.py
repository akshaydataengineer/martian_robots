import json


def get_json_object_from_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


def write_json_object_to_file(file_path, data, indent):
    with open(file_path, "w") as write_file:
        json.dump(data, write_file, indent=indent)
