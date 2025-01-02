from vosk import Model, KaldiRecognizer
import pyaudio
import json
import pyttsx4
import datetime

engine = pyttsx4.init()
def say_it(speech):
    engine.say(speech)
    engine.runAndWait()

model = Model("model")
recognizer = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("Говорите...")
while True:
    data = stream.read(4000, exception_on_overflow=False)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        text = result['text'].lower()
        print(text)
        if text == "time":
            now = datetime.datetime.now()
            str_date = f"Сейчас {str(now.hour)}:{str(now.minute)}"
            print(str_date)
            say_it(str_date)