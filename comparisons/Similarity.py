import os
from pathlib import Path

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class Similarity:
    def __init__(self) -> None:
        self.engine = "davinci-codex"

    def get_similarity_score(
        self, problem_statement: str, summary_to_check: str, summary_reference: str
    ) -> int:
        """Returns a positive similarity score usually between 0 and 300. Above 200 is good."""
        score_dict = openai.Engine(self.engine).search(
            search_model=self.engine,
            query=problem_statement,
            max_rerank=2,
            documents=[summary_to_check, summary_reference],
        )

        return score_dict

    def compare_submission_solution(
        self, starter_file: Path, submission_file: Path, solution_file: Path
    ):
        """Returns submission similarity score with starter_file and with solution_file."""
        with open(starter_file) as file:
            starter = file.read()
        with open(submission_file) as file:
            submission = file.read()
        with open(solution_file) as file:
            solution = file.read()

        engine = openai.Engine(self.engine)

        out = engine.search(
            search_model=self.engine, documents=[starter, solution], query=submission
        )

        starter_result = out["data"][0]
        solution_result = out["data"][1]
        return starter_result["score"], solution_result["score"]
