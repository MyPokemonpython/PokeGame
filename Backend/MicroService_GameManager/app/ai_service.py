import os
import requests
import random
import openai
from dotenv import load_dotenv

load_dotenv()


class AIService:
    def __init__(self, api_url):
        self.api_url = api_url

        # fetch from env variable.

        openai.api_key = os.getenv("OPENAI_API_KEY")

    def fetch_pokemon_data(self, pokemon_name: str):
        response = requests.get(f"{self.https://pokeapi.co/api/v2}pokemon/{pokemon_name}")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data from pokemon {pokemon_name}")

    def generate_question(self, pokemon_data: dict):
        prompt = (f" answer the question  {pokemon_data['name']} choose the correct answer")

        response = openai.completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )

        question_data = response.choices[0].text.strip()
        return question_data

    def get_ai_generated_question(self, pokemon_name: str):
        pokemon_data = self.fetch_pokemon_data(pokemon_name)
        return self.generate_question(pokemon_data)


print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))
