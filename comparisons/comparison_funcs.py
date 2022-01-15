import os
from pathlib import Path
from typing import Tuple

import openai

from comparisons.file_parser import file_path_to_code_string

openai.api_key = os.getenv("OPENAI_API_KEY")


def compare_submission_solution(
    starter_file: Path, submission_file: Path, solution_file: Path
) -> Tuple[float, float, float]:
    starter, submission, solution = (
        file_path_to_code_string(starter_file),
        file_path_to_code_string(submission_file),
        file_path_to_code_string(solution_file),
    )

    engine = openai.Engine("davinci-codex")

    out = engine.search(
        search_model="davinci-codex", documents=[starter, solution], query=submission
    )

    starter_similarity = out["data"][0]["score"]
    solution_similarity = out["data"][1]["score"]

    return (
        starter_similarity,
        solution_similarity,
        solution_similarity - starter_similarity,
    )


if __name__ == "__main__":
    starter = Path("examples/starter.py")
    submission_random = Path("examples/submission_random_garbage.py")
    submission_wrong = Path("examples/submission_wrong_function.py")
    submission_recur = Path("examples/submission_recur.py")
    submission_invalid = Path("examples/submission_invalid.py")
    submission_indent_error = Path("examples/submission_indent_error.py")
    solution = Path("examples/solution.py")

    for file in (
        starter,
        submission_random,
        submission_wrong,
        submission_recur,
        submission_invalid,
        submission_indent_error,
        solution,
    ):
        starter_similarity, solution_similarity, score = compare_submission_solution(
            starter, file, solution
        )
        print(f"{starter_similarity}, {solution_similarity}; Score = {score}")
