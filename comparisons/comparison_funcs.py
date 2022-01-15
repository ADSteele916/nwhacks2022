import os
from pathlib import Path

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def compare_submission_solution(starter_file: Path, submission_file: Path, solution_file: Path):
    with open(starter_file) as file:
        starter = file.read()
    with open(submission_file) as file:
        submission = file.read()
    with open(solution_file) as file:
        solution = file.read()

    engine = openai.Engine("davinci-codex")

    out = engine.search(search_model="davinci-codex", documents=[starter, solution], query=submission)
    print(out)


if __name__ == "__main__":
    compare_submission_solution(Path("examples/starter.py"),
                                Path("examples/submission_invalid.py"),
                                Path("examples/solution.py"))
