import json


class WriteJsonFile:
    @staticmethod
    def write(filepath: str, content: dict) -> None:
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(content, file)
        return None
