# This script will enable and disable each of the graphical
# segments below the text elements. The command for each individual
# segment can be found in PROTOCOL.md

import serial, struct, time

ser = serial.Serial('/dev/ttyUSB0')
data_struct = struct.Struct('b b b b')


while True:
	for i in range(29):
		commands=(0x1B, 0x30, i, 4); cmd = data_struct.pack(*commands); ser.write(cmd)
		time.sleep(0.1)
	for i in range(29):
		commands=(0x1B, 0x30, i, 0); cmd = data_struct.pack(*commands); ser.write(cmd)
		time.sleep(0.1)
