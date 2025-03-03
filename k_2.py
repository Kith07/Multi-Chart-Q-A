import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Necessary examples for RL
DOMAIN = "TOPIC"
K = 2
IMAGE_EX1 = "PATH"
IMAGE_EX2 = "PATH"
CAPTION_EX2 = "TEXT"
CAPTION_EX2 = "TEXT"

# Actual images and captions for generation
IMAGE1 = "PATH"
IMAGE2 = "PATH"
CAPTION1 = "TEXT"
CAPTION2 = "TEXT"

#prompt1 = "PATH TO INPUT_PROMPT.txt"
prompt1 = f"Greetings! I am interested in programming and I was wondering if you could help me generate an example of text that illustrates multiple skills in coding structure and syntax. The example should be a block of code with the primary goal of demonstrating the {TOPIC} while also illustrating all of the following skills: {SKILLS}. Please keep the code as concise as possible, and make sure the implementation can be found fully from the produced code. \n\nFor reference, here are the definitions and examples for the concepts: \n{DEFS_EXAMPLES}\n\nPlease start the block of code with 'Solution:' and start the explanation with 'Explanation:'.\n\nThanks very much!"
# TO DO: Add a 2nd prompt to revise it's own answer prior to evaluation/feedback

openai.api_key = os.getenv("OPEN_AI_API_KEY")

response = openai.ChatCompletion.create(
    model = "gpt-4",
    messages = [
        {"role": "user", "content": prompt1}
    ]
)

print(response["choices"][0]["message"]["content"])