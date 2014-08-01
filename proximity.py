#!/usr/local/bin/python2.7

import argparse
import sys

parser = argparse.ArgumentParser(description='Calculate the proximity to a beacon')
parser.add_argument('data', metavar = 'N', type = int, nargs='+', help='The rssi & output tX power of a beacon')
args = parser.parse_args()

rssi = float( args.data[0] )
tx =  float( args.data[1] )

ratio = rssi * 1.0 / tx 

if (ratio < 1.0):
	prox = ratio ** 10.0
else:
	prox = 0.89976 * (ratio ** 7.7095) + 0.111


print prox

 
