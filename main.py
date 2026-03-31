from detector import detect_language
from utils import tokenize

def main():
    print("=== Language Identifier ===\n")

    text = input("ادخل النص: ")

    words = tokenize(text)

    print("\n📊 النتيجة:\n" + "-"*25)

    for word in words:
        lang = detect_language(word)
        print(f"{word} --> {lang}")

if __name__ == "__main__" : main() 