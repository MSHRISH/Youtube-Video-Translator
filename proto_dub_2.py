from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import detect_silence
import speech_recognition as sr
from googletrans import Translator, constants
from gtts import gTTS
import os
import playsound
import random

	
def recog(audio,recog_text,lan):
	r=sr.Recognizer()
	a=sr.AudioFile(audio)
	with a as source:
		r.adjust_for_ambient_noise(source)
		Audio=r.record(a)
	try:
		recognised_text=r.recognize_google(Audio,language=lan)
		trans=Translator()	
		A=trans.translate(recognised_text)
		recog_text.append(A.text)
	except sr.UnknownValueError:
		pass

def spilt_and_recog(file_name,silence_list,audio,recog_text,lan):
	start=0
	if(len(silence_list)==0):
		recog(file_name,recog_text,lan)
	else:
		for i in range(0,len(silence_list)):
			segment=silence_list[i]
			seg_start=segment[0]
			end=segment[1]
			chunk=audio[start:end]
			start=seg_start
			file="chunk"+str(i)+".wav"
			chunk.export(file,format="wav")
			recog(file,recog_text,lan)
		file="chunk"+str(len(silence_list))+".wav"
		chunk=audio[start:]
		chunk.export(file,format="wav")
		recog(file,recog_text,lan)


def save(silence_list,recog_text):
	for i in range(0,len(silence_list)+1):
		myobj = gTTS(text=recog_text[i],lang="en")
		file_name="Test"+str(i)+".mp3"
		myobj.save(file_name)

def speak(original_audio,silence_list,final_file_name):
	duration_list=[]
	for i in silence_list:
		gap=(i[1]-i[0])/1000
		duration_list.append(round(gap))
	duration_list.append(0)
	

	len_of_original=len(original_audio)
	len_of_final=0

	for i in range(0,len(silence_list)+1):
		file_name="Test"+str(i)+".mp3"
		audio_file=AudioSegment.from_mp3(file_name)
		len_of_final=len_of_final+len(audio_file)+(duration_list[i]*1000)
	len_of_final=round(len_of_final/1000) * 1000
	len_of_original=round(len_of_original/1000) * 1000
	



	while(len_of_final!=len_of_original):
		diff=len_of_original-len_of_final
		if(diff>0):
			a=len(duration_list)-1
			duration_list[a]=round(diff/1000)
			break
		else:
			B=random.choice(duration_list)
			Index=duration_list.index(B)
			B=B-1
			len_of_final=len_of_final-1000
			duration_list[Index]=B
	final_file=AudioSegment.silent(duration=0)
	for i in range(0,len(silence_list)+1):
		file_name="Test"+str(i)+".mp3"
		audio_file=AudioSegment.from_mp3(file_name)
		silence=AudioSegment.silent(duration=(duration_list[i]*1000))
		final_file+=audio_file+silence
		final=final_file_name+".mp3"
		final_file.export(final,format="mp3")
	F=final_file_name+".mp3"	
	speak=AudioSegment.from_mp3(F)


	X=round(len(speak)/1000) * 1000
	Y=round(len(original_audio)/1000) * 1000

	if X>Y:
		temp=AudioSegment.silent(duration=0)
		diff=X-Y
		X=X-diff
		temp=temp+speak[0:X]
		F=final_file_name+".mp3"
		temp.export(F,format="mp3")
		



def main(name_of_audio,lan,final_name):
	final="#Path where Output audio should be saved"+"/"+final_name
	f=name_of_audio
	sound = AudioSegment.from_file(f, format="wav")
	a=detect_silence(sound,min_silence_len=4000,silence_thresh=-45)
	recog_text=[]
	spilt_and_recog(f,a,sound,recog_text,lan)
	save(a,recog_text)
	speak(sound,a,final)      







