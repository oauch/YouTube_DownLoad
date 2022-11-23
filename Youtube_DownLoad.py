# call lib
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import glob
import os.path

# set
root = Tk()
root.title("유튜브 MP3 다운로드")
root.geometry("500x160")
root.resizable(False, False)

#convert
def convert():
	#유튜브 전용 인스턴스 생성
	par = lnk.get()
	print(par)

	yt = YouTube(par)

	print("start!")
	# mp4 다운로드
	if(Radiovar.get() == 1):
		print("type: mp4")
		yt.streams.filter().all()
		yt.streams.filter(progressive=True, file_extension='mp4').first().download() 
	# mp3 다운로드
	else:
		print("type: mp3")
		yt.streams.filter(only_audio=True).all()
		yt.streams.filter(only_audio=True).first().download() 
		print("@@@ 성공 @@@")

		files = glob.glob("*.mp4")
		for x in files:
			if not os.path.isdir(x):
				filename = os.path.splitext(x)
				try:
					os.rename(x,filename[0] + '.mp3')
				except:
					pass
	messagebox.showinfo("다운여부","성공!") #메시지 박스를 띄운다.


# main
place = Label(root, text="\n")
lbl = Label(root, text="링크 URL")
lnk = Entry(root)

Radiovar = IntVar() 
Radio_button1 = Radiobutton(text="mp4",variable=Radiovar,value=1) 
Radio_button2 = Radiobutton(text="mp3",variable=Radiovar,value=2)

btn = Button(root, text="다운로드",command=convert)

lbl.pack()
lnk.pack(fill="x")
st = StringVar()

Radio_button1.pack()
Radio_button2.pack()

place.pack()


btn.pack()
root.mainloop()