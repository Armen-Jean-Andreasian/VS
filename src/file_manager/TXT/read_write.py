class ReadWriteTextFile:
    @staticmethod
    def write(filepath: str, content: str) -> None:
        with open(filepath, 'r+', encoding='utf-8') as file:
            old_content = file.read()
            if old_content:
                content += old_content + '\n' + content
            file.write(content)
        return None
