# This is an example of how to set up the spinning CD and blinking record
# icons. The benefit of this is that the attached software does not need to
# update the display constantly, but can rather set and forget.
import serial, struct, time

ser = serial.Serial('/dev/ttyUSB0')
segment_struct = struct.Struct('b b b b')
speed_struct = struct.Struct('b b b')

commands=(0x1B, 0x30, 2, 3)
cmd = segment_struct.pack(*commands)
ser.write(cmd) # Turn CD segment on
commands=(0x1B, 0x32, 1) # Higher values for third argument reduce speed
cmd = speed_struct.pack(*commands)
ser.write(cmd) # Set CD animation speed

commands=(0x1B, 0x30, 8, 3)
cmd = segment_struct.pack(*commands)
ser.write(cmd) # Turn record segment on
commands=(0x1B, 0x33, 3)
cmd = speed_struct.pack(*commands)
ser.write(cmd)

for i in range(3):
    commands=(0x1B, 0x30, 21+i, 3)
    cmd = segment_struct.pack(*commands)
    ser.write(cmd) # Turn wave segment on
commands=(0x1B, 0x34, 3)
cmd = speed_struct.pack(*commands)
ser.write(cmd)

ser.close()
