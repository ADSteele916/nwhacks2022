import difflib
import os
import re
from pathlib import Path
from typing import Tuple, List

import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

docstring = re.compile(r"(\"\"\"|''')(?:(?=(\\?))\2(.|\n))*?\1")


def strip_comments(text: List[str]) -> str:
    out = ""
    for line in text:
        no_comments = line.split("#")[0]
        out += no_comments
    return out


def open_and_preprocess_files(
    starter_file: Path, submission_file: Path, solution_file: Path
) -> Tuple[str, str, str]:
    with open(starter_file) as file:
        starter = strip_comments(file.readlines())
    with open(submission_file) as file:
        submission = strip_comments(file.readlines())
    with open(solution_file) as file:
        solution = strip_comments(file.readlines())

    starter = re.sub(docstring, "", starter)
    submission = re.sub(docstring, "", submission)
    solution = re.sub(docstring, "", solution)

    return starter, submission, solution


def compare_submission_solution(
    starter_file: Path, submission_file: Path, solution_file: Path
):
    starter, submission, solution = open_and_preprocess_files(
        starter_file, submission_file, solution_file
    )

    engine = openai.Engine("davinci-codex")

    out = engine.search(
        search_model="davinci-codex", documents=[starter, solution], query=submission
    )
    return out


def compare_submission_solution_diff(
    starter_file: Path, submission_file: Path, solution_file: Path
):
    starter, submission, solution = open_and_preprocess_files(
        starter_file, submission_file, solution_file
    )

    engine = openai.Engine("davinci-codex")

    starter_submission_diff = "".join(difflib.context_diff(starter, submission))
    starter_solution_diff = "".join(difflib.context_diff(starter, solution))

    out = engine.search(
        search_model="davinci-codex",
        documents=[starter_solution_diff],
        query=starter_submission_diff,
    )
    return out


if __name__ == "__main__":
    starter = Path("examples/starter.py")
    submission_recur = Path("examples/submission_recur.py")
    submission_invalid = Path("examples/submission_invalid.py")
    solution = Path("examples/solution.py")
    print(
        compare_submission_solution(
            starter, submission_recur, solution
        )
    )
    print(
        compare_submission_solution(
            starter, submission_invalid, solution
        )
    )
