#!/usr/local/bin/python2.7

from pymongo import MongoClient
import mosquitto
import time

#Global Dictionary for ID & time

phones = {}
MINTIME = 5


def checkTime(id, maj, min, tx, rx):
	sysTime = time.time()
#	print(id,maj, min, tx, rx)
#	print(sysTime)

	if(phones.has_key(id)):
		oldTime = phones.get(id)
		doc = {"phone": id, "maj": maj, "min": min, "tx": tx, "rx": rx}
		if((sysTime - oldTime) > MINTIME):
			#add phone to database
			usr.insert(doc)
			print("INSERTED")
	else:
		phones[id] = sysTime
#		print("Dict updated")

#
# Mosquitto Callbacks
#

def on_connect(mosq, obj, rc):
	mosq.subscribe("uq/beaconTracker/id/#", 0)
	print("rc: " + str(rc))

def on_message(mosq, obj, msg):
#	print(msg.topic+ " "+str(msg.qos)+" "+str(msg.payload))
	checkTime(msg.topic[20:], msg.payload[:4], msg.payload[4:8], msg.payload[9:12], msg.payload[12:])

def on_publish(mosq, obj, mid):
	print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, qos):
	print("Subscribed: "+str(mid)+" "+str(qos))

def on_log(mosq, obj, level, string):
	print(string)


mqttc = mosquitto.Mosquitto()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
#mqttc.on_log = on_log

client = MongoClient()
db = client.samd
usr = db.users

mqttc.connect("winter.ceit.uq.edu.au", 1883, 60)
mqttc.loop_forever() 
