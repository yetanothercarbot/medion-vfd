#!/usr/bin/python3

# This script will enable and disable each of the graphical
# segments below the text elements. The command for each individual
# segment can be found in PROTOCOL.md

import argparse, serial, time, sys

parser = argparse.ArgumentParser(description="Show built-in animations")
parser.add_argument("-p", "--port", default="/dev/ttyUSB0")

args = parser.parse_args()

try:
  ser = serial.Serial(args.port)
except serial.serialutil.SerialException:
  print("Unable to open serial port. Try using -p to specify a custom port.")
  sys.exit(1)

# Start off by resetting the controller
ser.write(bytearray([0x1F]))

while True:
	for i in range(29):
		ser.write(bytearray([0x1B, 0x30, i, 4]))
		time.sleep(0.1)
	for i in range(29):
		ser.write(bytearray([0x1B, 0x30, i, 0]))
		time.sleep(0.1)
