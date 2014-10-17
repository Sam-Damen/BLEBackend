#!/usr/local/bin/python2.7

from pymongo import MongoClient
import time
import pymongo

client = MongoClient()
db = client.samd
usr = db.users
MAXTIME = 180 #3min
	
while True:

	#ensure time formats are the same for comparison
	sysTime = time.mktime(time.gmtime(time.time()))


	#Store the users in a list, newest to oldest
	roomList = usr.find().sort("_id",-1)

	seen = set()
	dups = []
	ids = []

	#Remove duplicates
	for x in roomList:
		if x.get('phone') not in seen:
			dups.append(x)
			seen.add(x.get('phone'))

	# remove any old entries 
	for doc in dups:
		usrTime = doc.get('_id').generation_time
		usrTime = time.mktime(usrTime.timetuple())
		if((sysTime - usrTime) > MAXTIME):
			dups.remove(doc)


	#Need list of _id
	for doc in dups:
		ids.append( doc.get('_id') )


	#Remove all docs in the db that do not match
	usr.remove({ "_id": {"$nin": ids }, })





