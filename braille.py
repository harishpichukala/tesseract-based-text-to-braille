#--------------------------
# Text to Braille converter
#--------------------------

#a dictionary of text and the Braille equivalent
#the Braille is 3 rows of dots, so is stored as
#a list of 3 bits of text
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
        " " : ["  ","  ","  "]

    }

#get the message to convert
textIn =raw_input("\n\nEnter some text: ").lower()

print("");

#first, print out each character of the text
#with some gaps in between
for char in textIn:
	print(char +"  ")

print("\n")
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