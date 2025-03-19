import os
import openai
import base64
from dotenv import load_dotenv

load_dotenv()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
IMAGE1 = r"Charts-20250226T221112Z-001/Charts/300.png" #276
IMAGE2 = r"Charts-20250226T221112Z-001/Charts/302.png" #297
IMAGE3 = r"Charts-20250226T221112Z-001/Charts/304.png" #297

im_1 = encode_image(IMAGE1)
im_2 = encode_image(IMAGE2)
im_3 = encode_image(IMAGE3)

DOMAIN1 = "Energy"
DOMAIN2 = "Climate Science"
#DOMAINS = f"{DOMAIN1} and {DOMAIN2}"

with open("Extraction/Prompts/answers_prompt.txt", "r") as file:
    prompt = file.read()

prompt = prompt.format(
    DOMAIN=DOMAIN2
)

with open("Extraction/Questions/Combo3") as q1:
    question = q1.read()

prompt += question

openai.api_key = os.getenv("OPEN_AI_API_KEY")

response = openai.ChatCompletion.create(
    model = "gpt-4-turbo",
    messages = [{
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{im_1}"}},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{im_2}"}},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{im_3}"}}
        ]
    }]
)

with open("Extraction/Answers/Combo3", "w", encoding="utf-8") as f:
    f.write(response["choices"][0]["message"]["content"])