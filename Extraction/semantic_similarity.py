import spacy

model = spacy.load("en_core_web_md")

with open("Extraction/Extracted_Attributes/Pair1/im1") as f1:
    file1 = f1.read()

with open("Extraction/Extracted_Attributes/Pair1/im2") as f2:
    file2 = f2.read()

file1 = model(file1)
file2 = model(file2)

print(file1.similarity(file2))