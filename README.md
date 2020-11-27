# medion-vfd

This repository is a collection of scripts and a listing of protocol information for the M18ST05A VFD display found in the 2006 Medion MD-8800.

# Prior Art
- [spacerace/m18st05](https://github.com/spacerace/m18st05): The first repository that shows up. While the included software didn't work for me (the escape codes were being printed on screen for some reason), it was still very useful to be able to see the commands for clearing text.
- [hit-karlrsuhe.de](http://www.hit-karlsruhe.de/aol2mime/medion_md_8800_vfd.htm): A fairly complete listing of the control codes. This formed the basis of PROTOCOL.md.
- [pipperr.de](https://www.pipperr.de/dokuwiki/doku.php?id=python:python_write_serial_com_port): Example code for Pythoon 2.x. While I wasn't able to get this example code to run under Python 3, it was still useful to see the approach taken. Structs are also being used in my example code as a result.

# Basic Use
The connector (Molex 70107-series) has four pins, the first of one can be identified by a 1 and an arrow on the side opposite to the clip:

| Pin | Colour | Name     | Connect to       |
|-----|--------|----------|------------------|
| 1   | Red    | Vcc      | +5V              |
| 2   | Green  | TX       | USB-to-serial RX |
| 3   | Black  | Gnd      | Ground           |
| 4   | White  | RX       | USB-to-serial TX |

The display does not output anything, so it can safely be left disconnected. I'm not sure whether the data lines are 5v or 3v3, however my CP2102 board outputs 3v3 and the display seems to work fine.

The serial port is opened at 9600 baud with 1 stopbit (the default settings for pyserial).

# Advanced Use
Refer to PROTOCOL.md
