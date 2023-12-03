class WriteTextFile:
    @staticmethod
    def write(filepath: str, content: str) -> None:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        return None
