#lambdaex1.py
#program for finding sum , sub and mul operations on two numbers

def sumop(a,b):          #normal Function Def
	c=a+b
	return c

addop=lambda x,y:x+y     #anonymous fuction
subop=lambda a,b:a-b     #anonymous fuction
mulop=lambda k,v:k*v     #anonymous fuction

#main program
result1=sumop(10,20)
print("sum of two numbers with normal function={}".format(result1))
result2=addop(100,200)
print("sum of two numbers with anonymous function={}".format(result2))
print("sum of two numbers with anonymous function={}".format(addop(-10,-20)))
print("-"*50)
print("sub of two numbers with anonymous function={}".format(subop(10,20)))
print("mul of two numbers with anonymous function={}".format(mulop(6,7)))



