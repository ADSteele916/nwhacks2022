import re
from pathlib import Path
from typing import List

docstring = re.compile(r"(\"\"\"|''')(?:(?=(\\?))\2(.|\n))*?\1")


def __strip_comments(text: List[str]) -> str:
    out = ""
    for line in text:
        try:
            no_comments = line.split("#")[0]
        except TypeError:
            line = line.decode("utf-8")
            no_comments = line.split("#")[0]
        out += no_comments
    return out


def file_text_to_code_string(text: str) -> str:
    text = __strip_comments(text.readlines())
    return re.sub(docstring, "", text)


def file_path_to_code_string(file: Path) -> str:
    with open(file, "r") as f:
        text = __strip_comments(f.readlines())
    return re.sub(docstring, "", text)
