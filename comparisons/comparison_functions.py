import os
from pathlib import Path
from typing import Tuple

import openai

from comparisons.file_parser import file_path_to_code_string

openai.api_key = os.getenv("OPENAI_API_KEY")


def compare_submission_solution(
    starter: str, submission: str, solution: str
) -> Tuple[float, float, float]:

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


def is_passing(comparison_output: Tuple[float, float, float]) -> bool:
    starter_similarity, solution_similarity, score = comparison_output
    return score > 0


if __name__ == "__main__":
    starter = Path("examples/fibonacci/starter.py")
    submission_random = Path("examples/fibonacci/submission_random_garbage.py")
    submission_wrong = Path("examples/fibonacci/submission_wrong_function.py")
    submission_recur = Path("examples/fibonacci/submission_recur.py")
    submission_invalid = Path("examples/fibonacci/submission_invalid.py")
    submission_indent_error = Path("examples/fibonacci/submission_indent_error.py")
    solution = Path("examples/fibonacci/solution.py")
    bintree_starter = Path("examples/bintree/starter.py")
    bintree_submission_iterative = Path("examples/bintree/submission_iterative.py")
    bintree_submission_alternative = Path("examples/bintree/submission_alternative.py")
    bintree_solution = Path("examples/bintree/solution.py")

    for file in (
        starter,
        submission_random,
        submission_wrong,
        submission_recur,
        submission_invalid,
        submission_indent_error,
        solution,
        bintree_starter,
        bintree_submission_iterative,
        bintree_submission_alternative,
        bintree_solution,
    ):
        output = compare_submission_solution(
            file_path_to_code_string(starter),
            file_path_to_code_string(file),
            file_path_to_code_string(solution),
        )
        print(
            f"{file.parent.name}/{file.name}: {output}; Passing = {is_passing(output)}"
        )
