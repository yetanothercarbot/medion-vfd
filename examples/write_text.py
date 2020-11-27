# This script shows how to clear the screen and write text to it.

import random, serial, struct, time

ser = serial.Serial('/dev/ttyUSB0')
s_send_data = struct.Struct('b b b b')

# Clear screen
data_format = struct.Struct("b b")
commands = (0x1B, 0x52)
command_packed_data = data_format.pack(*commands)
ser.write(command_packed_data)
input() # Wait for enter
# Write some random numbers to it
ser.write(str(random.randint(1,1e10)).encode('ascii'))

# Close serial port before exiting
ser.close()
