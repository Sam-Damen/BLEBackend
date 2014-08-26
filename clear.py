#!/usr/local/bin/python2.7

from pymongo import MongoClient
import time

MAXTIME = 300

phones = {}
locale = {}
client = MongoClient()
db = client.samd
usr = db.users

while True:
	#for every unique phone in db, get time it was entered
	# if sysTime - oldTime > MAXTIME -> haven't seen a beacon in 5min
	# or old majmin |= new majmin -> moved into new room
	#clear out the corresponding database documents
	
	#need to make sure "_id time" correlates with sysTime

	for doc in usr.find():
		print(doc)
