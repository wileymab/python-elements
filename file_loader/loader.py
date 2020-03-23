import json
import yaml


class FileLoader:

    @staticmethod
    def load_yaml_file(file_name: str) -> dict:
        with open(file_name, 'r') as data:
            return yaml.full_load(data)

    @staticmethod
    def load_json_file(file_name: str) -> dict:
        with open(file_name, 'r') as data:
            return json.load(data)

    