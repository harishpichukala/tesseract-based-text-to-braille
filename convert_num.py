def convert(text):
	temp=text
	out=[]
	for i in temp:
		if '1'==i:
			j="@a"
			out.append(j)
		elif '2'==i:
			j="@b"
			out.append(j)
		elif '3'==i:
			j="@c"
			out.append(j)
		elif '4'==i:
			j="@d"
			out.append(j)
		elif '5'==i:
			j="@e"
			out.append(j)
		elif '6'==i:
			j="@f"
			out.append(j)
		elif '7'==i:
			j="@g"
			out.append(j)
		elif '8'==i:
			j="@h"
			out.append(j)
		elif '9'==i:
			j="@i"
			out.append(j)
		elif '0'==i:
			j="@j"
			out.append(j)
		else:
			j=i
			out.append(j)
		#print i
		#print out
	out=''.join(out)
	return out



		