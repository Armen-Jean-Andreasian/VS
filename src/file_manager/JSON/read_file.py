import json


class ReadJsonFile:
    @staticmethod
    def read(filepath: str) -> dict:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = json.load(file)
        return content
