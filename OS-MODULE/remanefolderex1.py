#remanefolderex1.py
import os 
try:
	os.rename("Bangalore","BAN") 
	print("Folder Renamed---Verify")
except FileNotFoundError:
	print("Old Folder Does not exists")

