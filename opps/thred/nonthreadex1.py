#nonthreadex1.py
import time
def squares(lst):  # lst=[10,20,30]
	for n in lst:
		print("Square of {}={}".format(n,n**2))
		time.sleep(4)

def cubes(lst):  # lst=[10,20,30]
	for n in lst:
		print("cube of {}={}".format(n,n**3))
		time.sleep(4)

bt=time.time()
lst=[10,20,30]
cubes(lst)
print("--------------------------------")
squares(lst)
print("--------------------------------")
et=time.time()
print("Total time taken by this non-threading Programming=",(et-bt))
print("--------------------------------")

