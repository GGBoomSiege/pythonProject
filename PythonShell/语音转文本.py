import speech_recognition as sr
 
r = sr.Recognizer()
 
test = sr.AudioFile('F:/123.wav')
 
with test as source:
    audio = r.record(source)
 
type (audio)
 
r.recognize_google(audio, language='zh-CN', show_all= True)