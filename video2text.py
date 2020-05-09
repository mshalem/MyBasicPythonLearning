import os

import speech_recognition as sr

command2mp3 = "ffmpeg -i Bolna.mp4 Bolna.mp3"
command2wav = "ffmpeg -i Bolna.mp3 Bolna.wav"
os.system(command2mp3)
os.system(command2wav)
r = sr.Recognizer()
audio = sr.AudioFile('Bolna.wav')
audio = r.record(source, duration=100)
print(r.recognize_google(audio))

