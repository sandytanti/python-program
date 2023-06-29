#FileEX1.py
try:
	rp=open("stud.data")
	print("type of rp=",type(rp))  #TextIOWrapper
except FileNotFoundError:
	print("Files does not exits:")
else:
	print("File opened in read mode successfully:")
	print("---------------------------------------")
	print("File Opening Mode=",rp.mode)   #r
	print("is it readable?=",rp.readable())  #True
	print("is it writable?=",rp.writable()) #False
	print("is files closed?=",rp.closed)    #False
	print("---------------------------------------")
finally:
	if rp!=None:
		print("File closed successfully:")
		rp.closed()
		print("Line-19--->is files closed?=",rp.closed) #True




