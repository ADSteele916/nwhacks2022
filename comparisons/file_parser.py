import re
from pathlib import Path
from typing import List

docstring = re.compile(r"(\"\"\"|''')(?:(?=(\\?))\2(.|\n))*?\1")


def strip_comments(text: List[str]) -> str:
    out = ""
    for line in text:
        no_comments = line.split("#")[0]
        out += no_comments
    return out


def file_path_to_code_string(file: Path) -> str:
    with open(file, 'r') as f:
        text = strip_comments(f.readlines())
    return re.sub(docstring, "", text)
