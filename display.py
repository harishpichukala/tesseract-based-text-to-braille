from open import *
from Tkinter import *
import tkFileDialog,os
from file_operations import *
from modules_ocr import *
import string
from convert_num import *
import speech
def speak(text):
	speech.say(text)
def reload():
	txt.config(state="normal")
	txt.delete(1.0,END)
	print("in reload")
	return
def widget1(l):
	txt.insert(INSERT,l)
	print("in widget")
	s.pack(side=RIGHT,fill=Y)
	txt.config(yscrollcommand=s.set)
	txt.pack(side=LEFT,fill=BOTH)
	txt.config(state="disabled")
	s.config(command=txt.yview)
	return
def choose_file():
	open_file();
	return
def get_text():
	k=read_file("name.txt")
	txt=extract(k)
	reload()
	widget1(txt)
	print(txt)
def say_voice():
	k=read_file("name.txt")
	txt=extract(k)
	print(txt)
	speak(txt)
def get_braile():
	k=read_file("name.txt")
	txt=extract(k)
	#print(txt)
	txt=txt.translate(string.maketrans("\n\t\r", "   "))
	#print(txt)
	txt=convert(txt)
	convert_braille(txt)
	display_txt=read_file("braille.txt")
	reload()
	widget1(display_txt)
	
win=Tk()
win.title("OCR")
win.geometry('600x400')
f=Frame(win)
name=Label(f,text="choose file to perform operation")
name.pack(side=LEFT)
bt=Button(f,text="Browse",command=choose_file)
bt.pack(side=LEFT)
f.pack(fill=BOTH)
f2=Frame(win)
f2.pack()
f1=Frame(win)
frame1=Frame(win)
txt=Text(win)
txt.insert(INSERT,"no results")
s=Scrollbar(win)
bt1=Button(f1,text="EXTRACT TEXT",command=get_text)
bt1.pack(side=LEFT)
bt2=Button(f1,text="voice",command=say_voice)
bt2.pack(side=LEFT)
bt3=Button(f1,text="convert to  Braille",command=get_braile)
bt3.pack(side=LEFT)
bt4=Button(f1,text="quit",command=quit)
bt4.pack(side=LEFT)
f1.pack(fill=BOTH)
win.mainloop()
