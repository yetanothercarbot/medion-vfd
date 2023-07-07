#!/usr/bin/python3
# This script will trigger the controller's built-in demo mode which has a 
# rain/snow type effect, and end it when the script is exited.

import argparse, serial, sys

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
ser.write(bytearray([0x1B, 0x54]))

print("Displaying display's built-in demo. Press ^C to exit...")

try:
  while True:
    pass
except KeyboardInterrupt:
  ser.write(bytearray([0x1F]))
