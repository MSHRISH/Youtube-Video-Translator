
import moviepy.editor as mpe

def Merge(input_vid,input_audio,final_name):
	my_clip = mpe.VideoFileClip(input_vid)
	audio_background = mpe.AudioFileClip(input_audio)
	final_audio = mpe.CompositeAudioClip([my_clip.audio, audio_background])
	final_clip = my_clip.set_audio(final_audio)
	final_clip.write_videofile(final_name)
	final_clip.ipython_display(maxduration=1000)


