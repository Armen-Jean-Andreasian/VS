class ReadTextFile:
    @staticmethod
    def read(filepath: str) -> str:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
