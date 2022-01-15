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

    def get_similarity_score(self, summary_1: str, summary_2: str) -> int:
        openai.Engine("ada").search(
            search_model="ada", 
            query="happy", 
            max_rerank=5,
            file="file-Lwjuy0q2ezi00jdpfCbl28CO"
        )