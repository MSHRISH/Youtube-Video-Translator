from tkinter import*
from tkinter import ttk


class app(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master=master
		self.master.title("Video Translator")
		self.master.geometry("320x200") 
		self.interface()
	def interface(self):
		self.pack(fill=BOTH, expand=1)
		Label(self,text="select the video format").grid(row=0,column=0)
		self.A=StringVar(self)
		self.A.set("url")
		B=OptionMenu(self,self.A,"url","mp4")
		B.config(width=5)
		B.grid(row=0,column=1)
		Label(self,text="Enter the location or url:").grid(row=2,column=0)
		self.entry_box=Entry(self)
		self.entry_box.grid(row=2,column=1)
		Label(self,text="Save the output as:").grid(row=3,column=0)
		self.out_name=Entry(self,)
		self.out_name.grid(row=3,column=1)
		Button(self,text="Translate",width=10).grid(row=9,column=1)
		self.clear_button=Button(self,text="Clear",width=10)
		self.clear_button.grid(row=11,column=1)
		self.Language=["Hindi","Tamil","Malayalam","Kannada","Telugu"]
		self.code=["hi-IN","ta-IN","ml-IN","kn-IN","te-IN"]
		self.Lan=StringVar(self)
		self.Lan.set(self.Language[0])
		Lan_op=OptionMenu(self,self.Lan,*self.Language)
		Lan_op.grid(row=8,column=1)
	
		





a=Tk()
b=app(a)
b.mainloop()
