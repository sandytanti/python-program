#FileWriteEx3.py
with open("hyd.data","a") as wp:
	print("Enter Multiple Lines of Text (To stop press stop)") 
	while(True):
		std=input()
		if (std!="stop"):
			wp.write(std+"\n")
		else:
			print("\n data written to the file sucessfully--verify") 
			break

