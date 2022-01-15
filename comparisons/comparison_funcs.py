import os
from pathlib import Path

import openai

from comparisons.file_parser import file_path_to_code_string

openai.api_key = os.getenv("OPENAI_API_KEY")


def compare_submission_solution(
    starter_file: Path, submission_file: Path, solution_file: Path
):
    starter, submission, solution = (
        file_path_to_code_string(starter_file),
        file_path_to_code_string(submission_file),
        file_path_to_code_string(solution_file),
    )

    engine = openai.Engine("davinci-codex")

    out = engine.search(
        search_model="davinci-codex", documents=[starter, solution], query=submission
    )
    return out["data"][0]["score"], out["data"][1]["score"]


if __name__ == "__main__":
    starter = Path("examples/starter.py")
    submission_recur = Path("examples/submission_recur.py")
    submission_invalid = Path("examples/submission_invalid.py")
    submission_wrong = Path("examples/submission_wrong_function.py")
    solution = Path("examples/solution.py")

    for file in (submission_recur, submission_invalid, submission_wrong):
        print(compare_submission_solution(starter, file, solution))
