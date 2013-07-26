#!/usr/bin/env python

from serial import Serial

br = 38400

o=0

for item in ["/dev/ttyACM0", "/dev/ttyACM1", "/dev/ttyUSB0", "/dev/ttyUSB1"]:
    try:
        o = Serial(item, br)
        break
    except Exception as e:
        print e

if o == 0:
	raise (BaseException("dude, wheres your arduino?"))

from curses import *

i = initscr()

def digitalwrite(p,v):
    o.write(chr((p<<1)|v))
    i.addstr(0,p,str(v))

colemak_ups   ="qwfpgjluy;[]"
colemak_downs ="arstdhneio'\\"
colemak_pulses="zxcvbkm,./"
             
qwerty_ups  ="qwertyuiop[]"
qwerty_downs="asdfghjkl;'\\"

ups = colemak_ups
downs = colemak_downs
pulses = colemak_pulses

try:
    i.keypad(1)
    noecho()
    while 1:
	i.refresh()
	k = chr(i.getch())
	if k in ups:
	    digitalwrite(  ups.index(k)+2, 1)
	if k in downs:
	    digitalwrite(downs.index(k)+2, 0)
	if k in pulses:
	    digitalwrite(pulses.index(k)+2, 1)
	    digitalwrite(pulses.index(k)+2, 0)
finally:
    endwin()
