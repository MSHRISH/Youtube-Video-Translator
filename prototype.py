from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import detect_silence
import speech_recognition as sr
from googletrans import Translator, constants
from gtts import gTTS
import os
import playsound

f="converted_test_file_1.wav"
sound = AudioSegment.from_file("#your_audio_file.wav", format="wav")
a=detect_silence(sound,min_silence_len=5000,silence_thresh=-45)

print(a)
recog_text=[]

def recog(audio):
	r=sr.Recognizer()
	a=sr.AudioFile(audio)
	with a as source:
		Audio=r.record(a)
	recognised_text=r.recognize_google(Audio,language="hi-IN")
	trans=Translator()	
	A=trans.translate(recognised_text)
	recog_text.append(A.text)

def spilt_and_recog():
	start=0
	if(len(a)==0):
		recog(f)
	else:
		for i in range(0,len(a)):
			segment=a[i]
			seg_start=segment[0]
			end=segment[1]
			chunk=sound[start:end]
			start=seg_start
			file="chunk"+str(i)+".wav"
			chunk.export(file,format="wav")
			print("exported",file)
			recog(file)
		file="chunk"+str(len(a))+".wav"
		chunk=sound[start:]
		chunk.export(file,format="wav")
		print("exported",file)
		recog(file)

spilt_and_recog()

print(recog_text)

def save():
	for i in range(0,len(a)+1):
		myobj = gTTS(text=recog_text[i],lang="en")
		file_name="Test"+str(i)+".mp3"
		myobj.save(file_name)

def speak():
	duration_list=[]
	for i in a:
		gap=i[1]-i[0]
		duration_list.append(gap)
	duration_list.append(0)

	final_file=AudioSegment.silent(duration=0)
	for i in range(0,len(a)+1):
		file_name="Test"+str(i)+".mp3"
		audio_file=AudioSegment.from_mp3(file_name)
		silence=AudioSegment.silent(duration=duration_list[i])
		final_file+=audio_file+silence
		final="final_output.mp3"
		final_file.export(final,format="mp3")

	speak=AudioSegment.from_mp3("final_output.mp3")
	play(speak)
		

save()
speak()



