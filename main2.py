import openai
from openai import OpenAI
import password


openai=OpenAI(api_key=password.key)


def extract_txt():
    with open("Zadanie_dla_JJunior_AI_Developera_tresc_artykulu.txt", "r", encoding="UTF-8") as file:
        content = file.read()
        return content