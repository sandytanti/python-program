#mobilenovalid.py
#Write a python program which will evaluate the mobile number 

import re
while True:
	mno=input("Enter Ur Mobile Number:")      #mno--> mobile number
	if (len(mno)==10):
		sres=re.search("\d{10}", mno)         #sres--> search result
		print(sres)
		if sres!=None:
			print("Ur mobile Number Valid:")
			break
		else:
			print("Ur Mobile Number is Invalid-bcoz It should not contain str/ special symbols")
	else:
		print("Mobile Must Contain 10 digits")
	


