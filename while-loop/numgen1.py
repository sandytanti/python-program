#numgen1.py
n=int(input("Enter a number:"))
if(n<=0):
	print("{} is invaild input:".format(n))
else:
	print("-"*40)
	print("Number within :{}".format(n))
	print("-"*40)
	i=1  #initlization part
	while(i<=n): #condition
		print("\t{}".format(i))
		i=i+1  #updation(incr)
	else:
		print("-"*40)






     




