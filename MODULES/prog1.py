#prog1.py----->main program

from icici import addr as a,callntrest as ca
print("Address of ICICI: {}".format(a))
print("---------------------------------------")
p=float(input("Enter Principle Amount:")) 
t=float(input("Enter Time:")) 
r=float(input("Enter Rate of intrest:")) 
ca(p,t,r)


 
