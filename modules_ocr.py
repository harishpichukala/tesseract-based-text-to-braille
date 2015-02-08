from pytesser import *
from PIL import Image
def extract(src):
	print(src)
	im=Image.open(src)
	text=image_to_string(im)
	#print text
	return text
def convert_braille(text):
	braille = {

        "a" : ["* ","  ","  "],
        "b" : ["* ","* ","  "],
        "c" : ["**","  ","  "],
        "d" : ["**"," *","  "],
        "e" : ["* "," *","  "],
        "f" : ["**","* ","  "],
        "g" : ["**","**","  "],
        "h" : ["* ","**","  "],
        "i" : [" *","* ","  "],
        "j" : [" *","**","  "],
        "k" : ["* ","  ","* "],
        "l" : ["* ","* ","* "],
        "m" : ["**","  ","* "],
        "n" : ["**"," *","* "],
        "o" : ["* "," *","* "],
        "p" : ["**","* ","* "],
        "q" : ["**","**","* "],
        "r" : ["* ","**","* "],
        "s" : [" *","* ","* "],
        "t" : [" *","**","* "],
        "u" : ["* ","  ","**"],
        "v" : ["* ","* ","**"],
        "w" : [" *","**"," *"],
        "x" : ["**","  ","**"],
        "y" : ["**"," *","**"],
        "z" : ["* "," *","**"],
        " " : ["  ","  ","  "],
		"%" : ["  ","  ","  "],
		"-" : ["  ","  ","  "],
		"'" : ["  ","  ","  "],
		"." : ["  ","  ","  "],
		"," : ["  ","  ","  "],
		"@" : [" *"," *","**"]    
		}

	#get the message to convert
	textIn =text.lower()

	#print("");

	#first, print out each character of the text
	#with some gaps in between
	for char in textIn:
		print(char +"  ")
	
	#print("\n")
	f=open("braille.txt","w")
	#for each of the 3 rows of the Braille dots
	for row in range(3):
		textOut = ""
		#for each character in the text
		for char in textIn:
			#add the row of Braille dots to the output
			textOut += braille[char][row] + "  "
		#print the row of braille    
		print(textOut)
		f.write(textOut+"\n")

	
	f.close()
	print("\n\n")