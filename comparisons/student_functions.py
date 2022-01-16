import os

# import file_parser
from pathlib import Path

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class StudentFunctions:
    def __init__(self) -> None:
        self.engine = "davinci-codex"

    def get_summary(self, code: str) -> str:
        affix = '"""\nHere\'s what the above code is doing:\n 1.'
        query = code + affix
        response = openai.Completion.create(
            engine=self.engine,
            prompt=query,
            temperature=0,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=['"""'],
        )

        return response["choices"][0]["text"]

    def fix_code(self, code: str) -> str:
        prefix = "##### Fix bugs in the below function\n\n### Buggy Python"
        affix = "\n### Fixed Python"
        query = prefix + code + affix
        response = openai.Completion.create(
            engine=self.engine,
            prompt=query,
            temperature=0,
            max_tokens=128,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["###", "#"],
        )

        return response["choices"][0]["text"]

    def get_time_complexity(self, code: str) -> str:
        affix = '"""\nThe time complexity of this function is'
        query = code + affix
        response = openai.Completion.create(
            engine=self.engine,
            prompt=query,
            temperature=0,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"],
        )

        return response["choices"][0]["text"]

    def get_python_docstring(self, code: str) -> str:
        """Only works with Python 3.7"""
        prefix = "# Python 3.7\n\n"
        affix = '\n# An elaborate, high quality docstring for the above function:\n"""'
        query = prefix + code + affix
        response = openai.Completion.create(
            engine=self.engine,
            prompt=query,
            temperature=0,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["#", '"""'],
        )

        return response["choices"][0]["text"]

    def convert_loop_to_python_stream(self, code: str) -> str:
        # don't know if this will work
        prefix = "##### Convert python loop to functional programming\n\n### Python with loop"
        affix = "\n### Python with functional programming"
        query = prefix + code + affix
        response = openai.Completion.create(
            engine=self.engine,
            prompt=query,
            temperature=0,
            max_tokens=128,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["###", "#"],
        )

        return response["choices"][0]["text"]

    def convert_list_comprehension_to_loop(self, code: str) -> str:
        # don't know if this will work
        prefix = "##### Convert list comprehension to for loop\n\n### Python with list comprehension"
        affix = "\n### Python with for loop"
        query = prefix + code + affix
        response = openai.Completion.create(
            engine=self.engine,
            prompt=query,
            temperature=0,
            max_tokens=128,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["###", "#"],
        )

        return response["choices"][0]["text"]

    def convert_loop_to_list_comprehension(self, code: str) -> str:
        # don't know if this will work
        prefix = (
            "##### Convert for loop to list comprehension\n\n### Python with for loop"
        )
        affix = "\n### Python with list comprehension"
        query = prefix + code + affix
        response = openai.Completion.create(
            engine=self.engine,
            prompt=query,
            temperature=0,
            max_tokens=128,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["###", "#"],
        )

        return response["choices"][0]["text"]


# if __name__ == "__main__":
#     sf = StudentFunctions()
#     code = file_parser.file_path_to_code_string(Path("examples/submission_for_loop_for_list.py"))
#     print(sf.convert_loop_to_list_comprehension(code))
