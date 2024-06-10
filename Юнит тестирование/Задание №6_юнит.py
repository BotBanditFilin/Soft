import re

def strip_punctuation_ru(data):
    data = re.sub(r'[^\w\s]', ' ', data)
    data = re.sub(r'\s+', ' ', data)
    return data.strip()

text = "Привет, мир! Как дела?"
cleaned_text = strip_punctuation_ru(text)
print(cleaned_text)
