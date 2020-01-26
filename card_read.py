#!/usr/bin/python
# read_card.py
# Read USB/Serial port for RFID carder
#
import os, sys
import serial
import time

# Define USB device
#ser = serial.Serial('/dev/ttyUSB0',9600, timeout = 5)
ser = serial.Serial('/dev/ttyUSB0',9600)

# listen for the input, exit if nothing received in timeout period
while True:
   line = ser.readline()
   if len(line) == 0:
      print("Time out! Exit.\n")
      sys.exit()
   print line,

#
# EOF
#

