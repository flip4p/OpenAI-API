import openai
from openai import OpenAI
import password


openai=OpenAI(api_key=password.key)


def extract_txt():
    with open("Zadanie_dla_JJunior_AI_Developera_tresc_artykulu.txt", "r", encoding="UTF-8") as file:
        content = file.read()
        return content

    def create_prompt(content: str) -> str:
        prompt_content = f'''I will provide with an article.
        Generate an HTML structure for it. 
        Put it all inside a div.
        Use the following guidelines:
        Headings should use <h1> tags
        Paragraphs should use <p> tags
        Suggest images in text form using <img> tags with: 
        src="image_placeholder.jpg"
        alt="A detailed prompt for generating a relevant image."
        Here is the article {content} ignore comments starting with *
        Generate an HTML structure without any markdown code block formatting.'''

        return prompt_content