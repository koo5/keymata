#!/usr/bin/env python

from serial import Serial

br = 38400

try:
    o = Serial("/dev/ttyACM0", br)
except Exception as e:
    print e
    o = Serial("/dev/ttyACM1", br)

from curses import *

i = initscr()

def digitalwrite(p,v):
    o.write(chr((p<<1)|v))
    i.addstr(0,p,str(v))

colemak_ups  ="qwfpgjluy;[]"
colemak_downs="arstdhneio'\\"
             
qwerty_ups  ="qwertyuiop[]"
qwerty_downs="asdfghjkl;'\\"

ups = colemak_ups
downs = colemak_downs

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
finally:
    endwin()
