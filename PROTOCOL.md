# M18ST05A protocol

The serial port needs to be opened with 9600,N,N,1.

## Writing text
Any text sent to the serial port will immediately show up on the display. When the display is full (32 chars), it will clear the screen and place the character back at the beginning.

## Commands
All commands - with the exception of reset - begin with the escape code 0x1B, followed by 1-8 bytes of further commands.

### Reset
- `0x1F`: Resets state and clears display. 

### Text commands
- `0x1B 0x50`: Clear Display (see examples/write_text.py)
- `0x1B 0x51`: CR (return cursor to first character)
- `0x1B 0x52`: Show character display
- `0x1B 0x53`: Turn off character display, without clearing memory

### Status Display
The source and media type segments can be dimmed by using a value between 0-4 (inclusive) for the fourth bit. The remaining segments can only be toggled.

An example for activating every segment can be found in examples/segments.py

- `0x1B 0x30 0 4`: HDD
- `0x1B 0x30 1 4`: FireWire (IEEE 1394)
- `0x1B 0x30 2 4`: CD drive (see [below](#animations))
- `0x1B 0x30 3 4`: USB
- `0x1B 0x30 4 4`: Movie
- `0x1B 0x30 5 4`: TV
- `0x1B 0x30 6 4`: Music
- `0x1B 0x30 7 4`: Photos
- `0x1B 0x30 8 1`: Red record circle (see [below](#animations))
- `0x1B 0x30 9 1`: Letter - outer segment
- `0x1B 0x30 10 1`: Letter - inner segment
- `0x1B 0x30 11 1`: Volume 1
- `0x1B 0x30 12 1`: Volume 2
- `0x1B 0x30 13 1`: Volume 3
- `0x1B 0x30 14 1`: Volume 4
- `0x1B 0x30 15 1`: Volume 5
- `0x1B 0x30 16 1`: Volume 6
- `0x1B 0x30 17 1`: Volume 7
- `0x1B 0x30 18 1`: Red line below volume
- `0x1B 0x30 19 1`: Speaker
- `0x1B 0x30 20 1`: Crossed speaker (mute)
- `0x1B 0x30 21 1`: Wave 1 (above volume display, see [below](#animations))
- `0x1B 0x30 22 1`: Wave 2
- `0x1B 0x30 23 1`: Wave 3
- `0x1B 0x30 24 1`: Source border
- `0x1B 0x30 25 1`: Media border
- `0x1B 0x30 26 1`: Record/graphical border
- `0x1B 0x30 27 1`: Mail icon border
- `0x1B 0x30 28 1`: Volume border

### Animations
Segments must be turned on manually before animation can be played. See examples/anim.py for examples.
- `0x1B 0x32 X`: Rotational speed of CD. `X` is an integer between 0-4 (inclusive). Lower numbers are faster.
- `0x1B 0x33 X`: Flash rate of record logo. `X` is an integer between 0-4 (inclusive). Lower numbers are faster.
- `0x1B 0x34 X`: Show a 'transmit' animation on the three wave segments in the speaker box.

### Graphical Display
There is a small display next to the record logo that is 9x7 pixels large. This is controlled through a single command that updates the entire screen:

`0x1B 0x31 B1 B2 B3 B4 B5 B6 B7 B8 B9`

Each of the B1-B9 is a single byte representing one column in the display. B1 is the right-most column and B9 the left-most column. The LSB is the top-most pixel in the column, and the MSB is discarded.

Example icons and animations can be found in examples/graphical.py.

### Clock
- `0x1B 0x00 Min Hour Day Month Year Year`: Set date & time, each of the values is in BCD.
- `0x1B 0x01`: 24 hour time
- `0x1B 0x02`: US-style 12-hour time
- `0x1B 0x03`: Clock centred
- `0x1B 0x04`: Clock moving
- `0x1B 0x05`: Show clock on-screen
- To hide clock, write text to the screen

### Other notes
- `0x1B 0x54`: Built-in demo snow/rain effect - can only be quit with a reset.
