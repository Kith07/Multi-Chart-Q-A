import os
import openai
from dotenv import load_dotenv

load_dotenv()

with open("Extraction/Extracted_Attributes/Pair9/im1") as f1:
    file1 = f1.read()

with open("Extraction/Extracted_Attributes/Pair9/im2") as f2:
    file2 = f2.read()

with open("Extraction/Prompts/similarity_prompt.txt") as p:
    prompt = p.read()

DOMAINS = "Climate Science, Energy, and Healthcare"

prompt = prompt.format(
    DOMAIN=DOMAINS
)
prompt += f"File 1: \n {file1} \n File 2: \n {file2}"

openai.api_key = os.getenv("OPEN_AI_API_KEY")

response = openai.ChatCompletion.create(
    model = "gpt-4-turbo",
    messages = [{
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
        ]
    }]
)

with open("Extraction/Similarity_Scores/GPT-4-Turbo/Pair9.txt", "w", encoding="utf-8") as f:
    f.write(response["choices"][0]["message"]["content"])