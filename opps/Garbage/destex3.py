#destex3.py 

import time 
class Sample:
	def __init__(self):
		print("Object Initliztion---Constructor:")

	def __del__(self):
		print("Memory Space pointed by object removed--Garbage Collector")


#main program 
s1=Sample()
print("object created and initlized"); 
s2=s1
s3=s2
print("Object s3 is removed") 
s3=None
time.sleep(10)
print("Object s2 is removed") 
s2=None
time.sleep(10)
print("Object s1 memory space is going be removed") 
s1=None
time.sleep(10)
print("End of Application")



