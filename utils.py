import re

def tokenize(text):
    # تقسيم النص بشكل أفضل (يشيل الرموز)
    words = re.findall(r'\b\w+\b', text)
    return words