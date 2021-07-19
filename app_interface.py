from tkinter import*
from tkinter import ttk
from tkinter import messagebox

import audio_video_extractor as AV
import proto_dub_2 as PD
import Merging as M

class app(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master=master
		self.master.title("Video Translator")
		self.master.geometry("320x200") 
		self.interface()
	def interface(self):
		self.pack(fill=BOTH, expand=1)
		Label(self,text="Enter the location or url:").grid(row=2,column=0)
		self.entry_url=Entry(self)
		self.entry_url.grid(row=2,column=1)
		Label(self,text="Save the output as:").grid(row=3,column=0)
		self.out_name=Entry(self,)
		self.out_name.grid(row=3,column=1)
		self.translate=Button(self,text="Translate",width=10,command=self.Translate).grid(row=9,column=1)
		self.clear_button=Button(self,text="Clear",width=10,command=self.Clear)
		self.clear_button.grid(row=11,column=1)
		self.Language=["Hindi","Tamil","Malayalam","Kannada","Telugu"]
		self.code=["hi-IN","ta-IN","ml-IN","kn-IN","te-IN"]
		self.Lan=StringVar(self)
		self.Lan.set(self.Language[0])
		Lan_op=OptionMenu(self,self.Lan,*self.Language)
		Lan_op.grid(row=8,column=1)
	def Translate(self):
		url_path=self.entry_url.get()
		Output_name=self.out_name.get()
		Language=self.Lan.get()
		index=self.Language.index(Language)
		Lan_code=self.code[index]
		path_list=AV.extract(url_path) #path_list[0] is video #path_list[1] is audio
		PD.main(path_list[1],Lan_code,Output_name)
		Final_audio_path="#path where translated audio should be saved"+"/"+Output_name+".mp3"
		Output_vid_path="#Path where Final video should be saved"+"/"+Output_name+".mp4"
		M.Merge(path_list[0],Final_audio_path,Output_vid_path)
		messagebox.showinfo("Output","Translation success check the Output_video folder")

	def Clear(self):
		self.entry_url.delete(0,"end")
		self.out_name.delete(0,"end")


		
	


a=Tk()
b=app(a)
b.mainloop()
