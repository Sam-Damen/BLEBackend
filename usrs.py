#!/usr/local/bin/python2.7

import mosquitto
import random
import time

TOPIC = "uq/beaconTracker/raw"
DATA = ":02 01 06 1A FF 4C 00 02 15 2F 23 44 54 CF 6D 4A 0F AD F2 F4 91 1B A9 FF A6 00 01 00 01 BE -"
NUM = 300

#Mosquitto Set-up

mqttc = mosquitto.Mosquitto()
#mqttc.on_publish = on_publish

mqttc.connect("winter.ceit.uq.edu.au", 1883, 60)


#Create Random Users
usrs = {}

for i in range(0,NUM):
	id = random.getrandbits(64)
	id = format(id,'x')
	rx = random.randint(45,60)
	usrs[id] = rx


#Array of msgs to send
msg = []

for x in usrs:
	msg.append( "ID_" + x + DATA + str(usrs.get(x)) ) 



while True:

#Send out the messages
	
	for m in msg:
		mqttc.publish(TOPIC, m, 0)
		
	
	#Change rx value
	for x in range(len(msg)): 
		rx = str( random.randint(45,60) )
		msg[x] = msg[x][:-2] + rx

#Wait before running again
	time.sleep(random.randint(10,20))	
	


