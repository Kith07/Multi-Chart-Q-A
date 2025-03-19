import spacy

model = spacy.load("en_core_web_md")

with open("Extraction/Extracted_Attributes/output3/image1.txt") as f1:
    file1 = f1.read()

with open("Extraction/Extracted_Attributes/output3/image2.txt") as f2:
    file2 = f2.read()

with open("Extraction/Extracted_Attributes/output3/image3.txt") as f3:
    file3 = f3.read()

file1 = model(file1)
file2 = model(file2)
file3 = model(file3)

print(file1.similarity(file2))
print(file1.similarity(file3))
print(file2.similarity(file3))