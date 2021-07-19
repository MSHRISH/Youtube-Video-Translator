import soundfile
import wave
from pydub import AudioSegment
from pydub.playback import play
import os
import subprocess

def convrt(source):

	
	Converted_path="C:/Users/Dhanalakshmi/Desktop/dubber/Input_converted_audio"
	I=os.listdir("C:/Users/Dhanalakshmi/Desktop/dubber/Input_converted_audio")
	J=Converted_path+"/"+"Input_convert"+str(len(I))+".wav"
	subprocess.call(['ffmpeg','-i',source,J])
	
	






