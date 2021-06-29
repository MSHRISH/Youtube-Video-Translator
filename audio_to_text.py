import speech_recognition as sr
r = sr.Recognizer()

def startConvertion():
    audio_file = sr.AudioFile('file_name.wav')#specify the file name
    with audio_file as s:
        r.adjust_for_ambient_noise(s)
        audio = r.record(s)
        try:
            print(r.recognize_google(audio,language="hi-IN"))
        except sr.UnknownValueError:
            print("FAiled")
startConvertion()
