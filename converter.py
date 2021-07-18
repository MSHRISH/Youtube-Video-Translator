import subprocess

try:
	subprocess.call(['ffmpeg','-i','#file_to_be_converted.extension','#file_expected_as_output.extension'])
	print("pass")
except:
	print("fail")
