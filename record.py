#!/usr/local/bin/python2.7

from pymongo import MongoClient
import mosquitto
import time

#Global Dictionary for ID & time

phones = {}

#
# Mosquitto Callbacks
#

def on_connect(mosq, obj, rc):
	mosq.subscribe("uq/beaconTracker/id/#", 0)
	print("rc: " + str(rc))

def on_message(mosq, obj, msg):
	#parse phone ID from topic
	
	sysTime = time.time()

	if (phones.has_key(id)):
		oldTime = phone.get(id)
		
	else :
		phones['id'] = sysTime
	

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

mqttc.connect("winter.ceit.uq.edu.au", 1883, 60)
mqttc.loop_forever() 
