import tkFileDialog,Tkinter,os
#from modules_ocr import *
from file_operations import *
def open_file():
	file = tkFileDialog.askopenfile(mode='rb',title='Choose a file')
	abs_path=os.path.abspath(file.name)
	print(abs_path)
	k=abs_path
	write_file("name.txt",k)
	return
