import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
def startConvertion():
    mic=sr.Microphone(device_index=1)
    print("listening")
    with mic as s:
        print("Yes")
        r.adjust_for_ambient_noise(s)
        audio=r.listen(s,timeout=10)
        try:
            print(r.recognize_google(audio,language="hi-IN"))
        except sr.UnknownValueError:
            print("FAiled")
startConvertion()
