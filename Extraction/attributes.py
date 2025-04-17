import os
import openai
import base64
from dotenv import load_dotenv

load_dotenv()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
IMAGE1 = r"Charts-20250226T221112Z-001/Charts/1874.png"
IMAGE2 = r"Charts-20250226T221112Z-001/Charts/2017.png"

im_1 = encode_image(IMAGE1)
im_2 = encode_image(IMAGE2)

DOMAIN2 = "Climate Science, Energy, and Healthcare"

with open("Extraction/Prompts/attribute_prompt.txt", "r") as file:
    prompt = file.read()

prompt = prompt.format(
    DOMAINS=DOMAIN2
)

openai.api_key = os.getenv("OPEN_AI_API_KEY")

response = openai.ChatCompletion.create(
    model = "gpt-4-turbo",
    messages = [{
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{im_2}"}}
        ]
    }]
)

with open("Extraction/Extracted_Attributes/Pair20/im2", "w", encoding="utf-8") as f:
    f.write(response["choices"][0]["message"]["content"])