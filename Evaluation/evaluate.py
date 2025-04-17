import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPEN_AI_API_KEY")

DOMAINS = "Energy, Climate Science, and Healthcare"

PAIR_DIR = "Extraction/Extracted_Attributes"
QUESTION_DIR = "Extraction/Questions"
RUBRIC_PATH = "Evaluation/rubric_prompt.txt"
OUTPUT_DIR = "Evaluation/GPT-4/NewRubric"

with open(RUBRIC_PATH) as p:
    base_prompt = p.read()

for i in range(6, 21):  # Loop over Pair1 to Pair20
    pair = f"Pair{i}"

    im1_path = os.path.join(PAIR_DIR, pair, "im1")
    im2_path = os.path.join(PAIR_DIR, pair, "im2")
    question_path = os.path.join(QUESTION_DIR, f"{pair}.txt")


    with open(im1_path, encoding='utf-8') as f1, open(im2_path, encoding='utf-8') as f2, open(question_path, encoding='utf-8') as q:
        attributes1 = f1.read()
        attributes2 = f2.read()
        questions = q.read().split("QUESTION ")[1:]

    for q_block in questions:
        q_lines = q_block.strip().split("\n")
        q_num = q_lines[0].split(":")[0].strip()
        question_text = ":".join(q_lines[0].split(":")[1:]).strip() + "\n" + "\n".join(q_lines[1:]).strip()

        prompt = base_prompt.format(
            DOMAIN=DOMAINS,
            ATTRIBUTES1=attributes1,
            ATTRIBUTES2=attributes2,
            QUESTION=question_text
        )

        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        output_path = os.path.join(OUTPUT_DIR, f"{pair}-Q{q_num}.txt")
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as out:
            out.write(response["choices"][0]["message"]["content"])

        print(f"Saved response for {pair} - Question {q_num}")