#!/usr/local/bin/python2.7

from pymongo import MongoClient
import time


client = MongoClient()
db = client.samd
usr = db.users
MAXTIME = 3
		
while True:
	#for every unique phone in db, get time it was entered
	# if sysTime - phoneTime > MAXTIME -> haven't seen a beacon in MAXTIME
	# or old majmin |= new majmin -> moved into new room
	#clear out the corresponding database documents
	
#ensure time formats are the same for comparison
	sysTime = time.mktime(time.gmtime(time.time()))
#print('SysTime: ', sysTime)

	for doc in usr.find():
		usrTime = doc.get('_id').generation_time
		usrTime = time.mktime(usrTime.timetuple())
		if((sysTime - usrTime) > MAXTIME):
			usr.remove({"_id": doc.get('_id')})
			print("Removed")




