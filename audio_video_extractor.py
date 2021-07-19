import pafy
import os
import CONVRT

def extract(url):
    I=os.listdir("#Path where downloaded video should be saved")
    J=os.listdir("#Path where extracted audio should be saved")
    v="#Path where downloaded video should be saved"+"input_video"+str(len(I))+".mp4"
    a="#Path where extracted audio should be saved"+"input_audio"+str(len(J))+".mp3"
    FOLDER=[v,a]
    video=pafy.new(url)
    audios=video.audiostreams
    best_audio=video.getbestaudio()
    best_video=video.getbest()
    best_audio.download(filepath = FOLDER[1])
    best_video.download(filepath=FOLDER[0])
    
    CONVRT.convrt(FOLDER[1])
    Converted_path="#Path where Mp3 to wav converted audio should be saved"
    converted_audio_path=Converted_path+"/"+"Input_convert"+str(len(I))+".wav"
    FOLDER[1]=converted_audio_path
    return FOLDER

