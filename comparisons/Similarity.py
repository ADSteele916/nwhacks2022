import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class Similarity:
    def __init__(self) -> None:
        self.engine = "davinci-codex"

    def get_summary(self, code: str) -> str:
        prepend = "Python 3"
        append = "# Explanation of what the code does\n\n #"
        query = prepend + code + append
        response = openai.Completion.create(
            engine=self.engine,
            prompt=query,
            temperature=0,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["#"]
        )

        return response

    def get_similarity_score(self, problem_statement: str, summary_1: str, summary_2: str) -> int:
        """Returns a positive similarity score usually between 0 and 300. Above 200 is good."""
        score = openai.Engine(self.engine).search(
            search_model=self.engine, 
            query=problem_statement, 
            max_rerank=2,
            documents=[summary_1, summary_2]
        )

        return score

