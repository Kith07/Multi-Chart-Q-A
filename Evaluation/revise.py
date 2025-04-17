import os
from dotenv import load_dotenv
import openai

load_dotenv()

with open("Extraction/Extracted_Attributes/output2/image1.txt") as f1:
    attributes1 = f1.read()

with open("Extraction/Extracted_Attributes/output2/image2.txt") as f2:
    attributes2 = f2.read()

with open("Extraction/Questions/Combo2") as q:
    QUESTION = q.read()

with open("Evaluation/revised_prompt.txt") as p:
    prompt = p.read()

prompt = prompt.format(
    QUESTION=QUESTION,
    ATTRIBUTES1=attributes1,
    ATTRIBUTES2=attributes2
)

# print(prompt)

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

with open("Evaluation/Revised_Questions/Combo2", "w", encoding="utf-8") as f:
    f.write(response["choices"][0]["message"]["content"])