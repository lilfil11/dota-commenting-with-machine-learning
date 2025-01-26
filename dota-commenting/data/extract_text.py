import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile('../../data/2350276298_dota2_paragon_ru.wav')
with harvard as source:
    audio = r.record(source)
    print(type(audio))
