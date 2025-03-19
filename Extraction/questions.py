import os
import openai
from dotenv import load_dotenv

load_dotenv()

DOMAINS = "Energy and Climate Science"

with open("Extraction/Extracted_Attributes/output3/image1.txt") as f1:
    file1 = f1.read()

with open("Extraction/Extracted_Attributes/output3/image2.txt") as f2:
    file2 = f2.read()

with open("Extraction/Extracted_Attributes/output3/image3.txt") as f3:
    file3 = f3.read()

with open("Extraction/Prompts/inference_prompt.txt") as p:
    prompt = p.read()

prompt = prompt.format(
    DOMAIN=DOMAINS
)

prompt += f"File 1: \n {file1} \n File 2: \n {file2} \n File 3: \n {file3}"

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

with open("Extraction/Questions/Combo3", "w", encoding="utf-8") as f:
    f.write(response["choices"][0]["message"]["content"])