import fasttext
import os
import sys
from deep_translator import GoogleTranslator

# حل مشكلة الترميز
sys.stdout.reconfigure(encoding='utf-8')

# تحميل الموديل
model_path = os.path.join(os.path.dirname(__file__), "lid.176.bin")
model = fasttext.load_model(model_path)

print("\n" + "="*40)
print("   Language Identifier + Translator")
print("="*40 + "\n")

while True:
    text = input("ادخل النص (exit للخروج): ").strip()

    if text.lower() == "exit":
        break

    if len(text) < 2:
        print("⚠️ النص قصير\n")
        continue

    # تحديد اللغة
    result = model.predict(text, k=1)
    lang = result[0][0].replace("label", "")
    confidence = result[1][0]

    print("\n--- النتيجة ---")
    print(f"🌐 Language: {lang}")
    print(f"📊 Confidence: {round(confidence * 100, 2)}%")

    # ترجمة إذا إنكليزي
    if lang == "en":
        translated = GoogleTranslator(source='en', target='ar').translate(text)
        print("📝 Translation:")
        print("→", translated)

    print("-" * 30 + "\n")

        #  cd "C:\Users\ZEUS\Desktop\language_identifier"

