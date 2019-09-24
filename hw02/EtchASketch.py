#!/usr/bin/env python
import curses
import sys
import Adafruit_BBIO.GPIO as GPIO
import time

button1 = "P8_11"
button2 = "P8_12"
button3 = "P8_17"
button4 = "P8_18"

GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

x = 0
y = 0
window = 10
stdscr = curses.initscr()

while(1):

	if GPIO.input(button1):
		y = y + 1
		if y>=window:
			y=window
		stdscr.addstr(y, x, "0")
		time.sleep(0.1)
		
	elif GPIO.input(button2):
		y = y - 1
		if y<0:
			y=0
		stdscr.addstr(y, x, "0")
		time.sleep(0.1)
		
	elif GPIO.input(button3):
		x = x + 1
		if x>=window*2:
			x=window*2
		stdscr.addstr(y, x, "0 ")
		time.sleep(0.1)
		
	elif GPIO.input(button4):
		x = x - 1
		if x < 0:
			x=0
		stdscr.addstr(y, x, "0")
		time.sleep(0.1)
		
	elif GPIO.input(button1) and GPIO.input(button4):
		break
		
		
	stdscr.refresh()
