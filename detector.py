from langdetect import detect

def detect_language(word):
    try:
        return detect(word)
    except:
        return "unknown"