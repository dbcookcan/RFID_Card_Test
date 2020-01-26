#!/usr/bin/env python
import time
import sys
import serial

card = '6400DBF95412'        # Stored good card number consider using a list or a file.

while True:            # loop until the program encounters an error.
	ser = serial.Serial('/dev/ttyUSB0',9600)
        sys.stdin = open('/dev/ttyUSB0', 'r')
        
	# Read raw input, then strip leading char & CR/NL
	raw_input = ser.readline()
        RFID_input = str(raw_input[1:13])

	#print "Read code from RFID reader:{0}".format(RFID_input)
	#print "Code from card:{0}".format(card)
        #print "Len input: ", len(RFID_input)
        #print "Len card : ", len(card)
        #l1 = []
	#l2 = []
	#for c in RFID_input:
        #		l1.append(c)
	#	l2.append(ord(c))
	#print(l1)
	#print(l2)


	# Check if the card should be granted access            
        if RFID_input == card:      # compare the stored number to the input and if True execute code.
            print "Access Granted" 
            print "Read code from RFID reader:{0}".format(RFID_input)
        else:                    # and if the condition is false excecute this code.
            print "Access Denied"


