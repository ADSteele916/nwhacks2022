import openai
import os
import file_parser
from pathlib import Path
openai.api_key = os.getenv("OPENAI_API_KEY")

class StudentFunctions():
    def __init__(self) -> None:
        self.engine = "davinci-codex"

    def get_summary(self, code: str) -> str:
        affix = "\"\"\"\nHere's what the above code is doing:\n 1."
        query = code + affix
        response = openai.Completion.create(
            engine=self.engine,
            prompt=query,
            temperature=0,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\"\"\""]
        )

        return response

    def fix_code(self, code: str) -> str:
        prefix = "##### Fix bugs in the below function\n\n### Buggy Python"
        affix = '\n### Fixed Python'
        query = prefix + code + affix
        response = openai.Completion.create(
            engine = self.engine,
            prompt = query,
            temperature = 0,
            max_tokens = 128,
            top_p = 1.0,
            frequency_penalty=0.0,
            presence_penalty = 0.0,
            stop=["###"]
        )

        return response

    def get_time_complexity(self, code: str) -> str:
        affix = "\"\"\"\nThe time complexity of this function is"
        query = code + affix
        response = openai.Completion.create(
            engine=self.engine,
            prompt=query,
            temperature=0,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"]
        )

        return response

    def get_python_docstring(self, code: str) -> str:
        """Only works with Python 3.7"""
        prefix = "# Python 3.7\n\n"
        affix = "\n# An elaborate, high quality docstring for the above function:\n\"\"\""
        query = prefix + code + affix
        response = openai.Completion.create(
            engine=self.engine,
            prompt=query,
            temperature=0,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["#", "\"\"\""]
        )

        return response

    def convert_loop_to_python_stream(self, code: str) -> str:
        # don't know if this will work
        prefix = "##### Convert python loop to functional programming\n\n### Python with loop"
        affix = '\n### Python with functional programming (map, filter, reduce)'
        query = prefix + code + affix
        response = openai.Completion.create(
            engine = self.engine,
            prompt = query,
            temperature = 0,
            max_tokens = 128,
            top_p = 1.0,
            frequency_penalty=0.0,
            presence_penalty = 0.0,
            stop=["###"]
        )

        return response

if __name__ == "__main__":
    sf = StudentFunctions()
    code = file_parser.file_path_to_code_string(Path("examples/wrong_no_doc.py"))
    print(sf.get_python_docstring(code))