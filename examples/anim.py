#!/usr/bin/python3

# This is an example of how to set up the spinning CD and blinking record
# icons. The benefit of this is that the attached software does not need to
# update the display constantly, but can rather set and forget.

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

ser.write("Enable CD, reco-rd and wave anim".encode('ascii'))

ser.write(bytearray([0x1B, 0x30, 2, 3])) # Turn CD segment on
ser.write(bytearray([0x1B, 0x32, 1])) # Set CD animation speed, higher values for third argument reduce speed

ser.write(bytearray([0x1B, 0x30, 8, 3])) # Turn record segment on
ser.write(bytearray([0x1B, 0x33, 3]))

for i in range(3):
    ser.write(bytearray([0x1B, 0x30, 21+i, 3])) # Turn wave segments on
ser.write(bytearray([0x1B, 0x34, 3]))

ser.close()
