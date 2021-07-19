import pafy
import os
import CONVRT

def extract(url):
    I=os.listdir("C:/Users/Dhanalakshmi/Desktop/dubber/Input_video")
    J=os.listdir("C:/Users/Dhanalakshmi/Desktop/dubber/Input_audio")
    v="C:/Users/Dhanalakshmi/Desktop/dubber/Input_video/"+"input_video"+str(len(I))+".mp4"
    a="C:/Users/Dhanalakshmi/Desktop/dubber/Input_audio/"+"input_audio"+str(len(J))+".mp3"
    FOLDER=[v,a]
    video=pafy.new(url)
    audios=video.audiostreams
    best_audio=video.getbestaudio()
    best_video=video.getbest()
    best_audio.download(filepath = FOLDER[1])
    best_video.download(filepath=FOLDER[0])
    CONVRT.convrt(FOLDER[1])
    Converted_path="C:/Users/Dhanalakshmi/Desktop/dubber/Input_converted_audio"
    converted_audio_path=Converted_path+"/"+"Input_convert"+str(len(I))+".wav"
    FOLDER[1]=converted_audio_path
    return FOLDER

