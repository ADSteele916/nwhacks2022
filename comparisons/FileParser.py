from pathlib import Path

class FileParser():
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_str(file: Path):
        with open(file, 'r') as f:
            lines = f.readlines()
        return lines