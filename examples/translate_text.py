from src.translate import translate_to_english

with open("data/sample_spanish.txt", "r") as f:
    text = f.read()

translation = translate_to_english(text)
print(translation)