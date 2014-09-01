#!/usr/local/bin/python2.7

from pymongo import MongoClient
import time

MAXTIME = 300

client = MongoClient()
db = client.samd
usr = db.users
MAXTIME = 300
		
#while True:
	#for every unique phone in db, get time it was entered
	# if sysTime - oldTime > MAXTIME -> haven't seen a beacon in 5min
	# or old majmin |= new majmin -> moved into new room
	#clear out the corresponding database documents
	
	#need to make sure "_id time" correlates with sysTime

#ensure time formats are the same for comparison

sysTime = time.mktime(time.gmtime(time.time()))
#print('SysTime: ', sysTime)

#doc = usr.find_one()
#usrTime = doc.get('_id').generation_time
#print(time.mktime(usrTime.timetuple()))

for doc in usr.find():
	usrTime = doc.get('_id').generation_time
	usrTime = time.mktime(usrTime.timetuple())
	if((sysTime - usrTime) > 300):
		usr.remove({"_id": doc.get('_id')})
		print("Removed")




