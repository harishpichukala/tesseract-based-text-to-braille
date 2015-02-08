def read_file(filename):
	f=open(filename,"r")
	k=f.read()
	f.close()
	return k
def write_file(filename,txt):
	f=open(filename,"w")
	k=f.write(txt)
	f.close()
	