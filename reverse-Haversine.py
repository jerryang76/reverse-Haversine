#!/usr/bin/env python
# coding: utf8
# http://www.movable-type.co.uk/scripts/latlong.html
import math
import sys


# Earth's radius, sphere
#R = 6371.01
R = 6378.1370
username = ("Username1","Username2")
password = "password"

cmd = "python runserver.py -ns -l '{lat} {lon}' --port {port} -u {username} -st 10 -p {password} -ld 20 &"
#cmd_final = "python runserver.py -l '{lat} {lon}' -u {username} -st 10 -p {password} -st 10 -ld 20&"

# starting point
#sham = (24.1395777166, 120.673547)
#sham = sys.argv
#lat = sham[0]
#lon = sham[1]
#get lat from 1st argument, lon from 2nd argument
#example python matirx.py 24.1395777166 120.673547
if len(sys.argv) != 2:
	print 'example: python matirx.py 24.1395777166 120.673547'
	sys.exit(0)

lat = float(sys.argv[1])
lon = float(sys.argv[2])


# offsets in km
#d = 2.85
d = 2.00
brng = math.radians (90.00)

# scan initial location
port = 6000
index = -1

for h in range(2):
	if h == 0:
		hlat2 = lat
		hlat = lat
	else:
		hd = 2.00
		hbrng = math.radians (180.00)
		hlat1 = math.radians(hlat)  # Current lat point converted to radians
		hlat2 = math.asin(math.sin(hlat1) * math.cos(hd / R) + 
						 math.cos(hlat1) * math.sin(hd / R) * math.cos(hbrng))
		hlat2 = math.degrees(hlat2)
		hlat = hlat2

	for i in range(6):
		if i == 0:
			lat = hlat2
			lon = float(sys.argv[2])
			index = index + 1
			port = port + 1
			#print cmd.format(lat=lat, lon=lon, port=port, username=username[index], password=password)
		else:
		
			port = port + 1
			# // Coordinate offsets in radians
			#print hlat2
			lat1 = math.radians(hlat2)  # Current lat point converted to radians
			lon1 = math.radians(lon)  # Current long point converted to radians

			lat2 = math.asin(math.sin(lat1) * math.cos(d / R) + 
							 math.cos(lat1) * math.sin(d / R) * math.cos(brng))

			lon2 = lon1 + math.atan2(math.sin(brng) * math.sin(d / R) * math.cos(lat1), 
									 math.cos(d / R) - math.sin(lat1) * math.sin(lat2))

			lat2 = math.degrees(lat2)
			lon2 = math.degrees(lon2)
			index = index + 1
						
			print cmd.format(lat=lat2, lon=lon2, port=port, username=username[index], password=password)

			lat = lat2
			lon = lon2