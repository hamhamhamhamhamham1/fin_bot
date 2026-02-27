import random
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
def translator(audio_patch):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_patch) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Ты сказал:", text)
        return text
    except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
        print("Не удалось распознать речь.")
    except sr.RequestError as e:             # - если нет интернета или API недоступен
        print(f"Ошибка сервиса: {e}")
    lang = input("Введите код языка для перевода (например, 'en' — английский, 'es' — испанский): ")
    translator = Translator()
    translated = translator.translate(text, dest=lang)  # здесь 'en' — это английский
    print("🌍 Перевод на", translated.text)