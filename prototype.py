#modules to be impoerted
from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import detect_silence
import speech_recognition as sr
from googletrans import Translator, constants
from gtts import gTTS
import os
import playsound

f="#YOUR_AUDIO_FILE.wav"


sound = AudioSegment.from_file("#your_audio_file.wav", format="wav")

#Silent parts in the audio.The thresh and min_silence_len can be tweaked according to the audio
a=detect_silence(sound,min_silence_len=5000,silence_thresh=-45)
recog_text=[]#List of recognised and translated text from audio chunks


def recog(audio):
	"""audio is a AudioSegment object.It is the audio which is to be recognized.
	The function recognises and translates the audio and append in the above lis(recog_text)."""
	r=sr.Recognizer()
	a=sr.AudioFile(audio)
	with a as source:
		Audio=r.record(a)
	recognised_text=r.recognize_google(Audio,language="hi-IN")
	trans=Translator()
	A=trans.translate(recognised_text)
	recog_text.append(A.text)

def spilt_and_recog():
	"""This function spilts the audio into chunks and calls the recog() function and passes each chunk"""
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

		
def save():
	"""This function converts the text in recog_text to speech and save it as an mp3 file"""
	for i in range(0,len(a)+1):
		myobj = gTTS(text=recog_text[i],lang="en")
		file_name="Test"+str(i)+".mp3"
		myobj.save(file_name)

def speak():
	"""This function merges all audio files converted by save() into a single audio file
	with all the necessary pauses and gaps"""
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
		
spilt_and_recog()
save()
speak()



