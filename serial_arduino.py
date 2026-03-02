#saves values from serial to file and print to terminal
# python serial_arduino.py COM3
from serial import Serial
import time
import sys

filename = "arduino.txt"

def adddata(data):#a function to add the data to the text file
	date=time.time()
	h=str(data)+','+str(date)+'\n'
	fh = open(filename, 'a')
	fh.write(h) 
	fh.close 

if len(sys.argv) < 2:
	portname = 'COM3'
else:
	portname = sys.argv[1]
	
ser =Serial(
	port=portname,
	baudrate = 9600,
	timeout=None)
	
while 1:
	while(ser.inWaiting()==0):#wait for the data from serial		
		time.sleep(0.2)
		#print(".")

	#read and decode the data
	line=ser.readline().decode('utf-8')
	line=line.rstrip() #remove trainling chars
	print(line)	
	adddata(line) #add the data to the txt file
	