#!/usr/local/bin/python2.7

import mosquitto
import argparse
import sys


#Input the topic to subscribe to
parser = argparse.ArgumentParser(description='Subscribe to a MQTT Topic on the Winter CIET server')
parser.add_argument('data', type = str, help='The MQTT topic')
args = parser.parse_args()

topic = args.data 

#
# Helper to convert unsigned hex to signed int
#
def hex2sign(num):
	if num > 0x7F:
		num -= 0x100

	return num	


#
# Parse out the mosquitto message for processing
#
def parse(msg):
	col = msg.index(':')
	x = [i for i in msg[col+1:].split()]	#Remove spaces in the message after ID

#Length of data packets
	alen = int(x[0],16)
	adlen = int(x[alen + 1],16)
	
#Find only ibeacon packets??
#Assume proper formating (ie. phone app handles it)

	id = msg[0:col]
	maj = x[-6] + x[-5]
	min = x[-4] + x[-3]
	power = hex2sign(int(x[-2],16))
	rssi = x[-1]
	
#Publish back to 2 different topics for easier sorting
	form = str(maj) + str(min) + " " + str(power) + str(rssi)
	mqttc.publish("uq/beaconTracker/" + id,form, 0)

	form = id + " " + str(power) + str(rssi)
	mqttc.publish("uq/beaconTracker/" + str(maj) + str(min), form, 0) 

#	print(id)
#	print(maj)
#	print(min)
#	print(power)
#	print(rssi)
				

#
# Mosquitto Callbacks below 
#

def on_connect(mosq, obj, rc):
	mosq.subscribe(topic, 0)
	print("rc: " +str(rc))

def on_message(mosq, obj, msg):
     print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
     parse(msg.payload)	

def on_publish(mosq, obj, mid):
    print("mid: "+str(mid))
#	mosq.disconnect()

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)


mqttc = mosquitto.Mosquitto()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
#mqttc.on_log = on_log

mqttc.connect("winter.ceit.uq.edu.au", 1883, 60)


mqttc.loop_forever()
