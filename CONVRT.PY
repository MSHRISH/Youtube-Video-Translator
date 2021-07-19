import soundfile
import wave
from pydub import AudioSegment
from pydub.playback import play
import os
import subprocess

def convrt(source):

	
	Converted_path="#Path where converted audio should be stored"
	I=os.listdir("#Path where converted audio should be stored")
	J=Converted_path+"/"+"Input_convert"+str(len(I))+".wav"
	subprocess.call(['ffmpeg','-i',source,J])
	
	






