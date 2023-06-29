#roman.py
def normaltoroman(n):
	if(n<=0):
		print("{} invalid input:".format(n))
	else:     #n=2900
		while(n>=1000):
			print("M",end="")
			n=n-1000
		if(n>=900):
			print("CM",end="")
			n=n-900
		if(n>=500):
			print("D",end="")
			n=n-500
		if(n>=400):
			print("CD",end="")
			n=n-400
		if(n>=100):
			print("C",end="")
			n=n-100
		if(n>=90):
			print("XC",end="")
			n=n-90
		if(n>=50):
			print("L",end="")
			n=n-50
		if(n>=40):
			print("XL",end="")
			n=n-40
		if(n>=10):
			print("IX",end="")
			n=n-10
		if(n>=9):
			print("X",end="")
			n=n-9
		if(n>=5):
			print("V",end="")
			n=n-5
		if(n>=4):
			print("IV",end="")
			n=n-4
		while(n>=1):
			print("I",end="")
			n=n-1
	print()

#main program

n=int(input("Enter a number:"))
print("------------------------")
normaltoroman(n)
print("-------------------------")




	 
