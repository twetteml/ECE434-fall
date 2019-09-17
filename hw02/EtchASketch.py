#!/usr/bin/env python
import curses
import sys
import Adafruit_BBIO.GPIO as GPIO

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


class Sketch(object):
	def __init__(this):
		this.pos = [0, 0]
		this.pastPos = list(this.pos)
		this.width=0
		this.height=0
		this.drawn = "O"
		this.empty = " "
		this.cursorM = "^"
		this.stdscr = None


	def shake(this):
		this.height, this.width = this.stdscr.getmaxyx()
		for y in range(0, this.height):
			for x in range(0, this.width):
				try:
					this.stdscr.addstr(y, x, this.drawn)
				except curses.error:
					pass

	def cursor(this):
		try:
			this.stdscr.addstr(this.pos[1], this.pos[0], this.cursorM)
		except curses.error:
			pass

	def main(this, stdscr):
		this.stdscr = stdscr
		stdscr.clear()
		this.shake()
		print("Use buttons keys to sketch")
		print("Press s key to reset the board")
		print("Press q key to quit")
		while True:
			this.cursor()
			c = stdscr.getch(this.height - 1, this.width - 1)
			if GPIO.input(button1):
				if this.pos[1] > 0:
					this.pos[1] -= 1
			elif GPIO.input(button2):
				if this.pos[1] < this.height - 1:
					this.pos[1] += 1
			elif GPIO.input(button3):
				if this.pos[0] > 0:
					this.pos[0] -= 1
			elif GPIO.input(button4):
				if this.pos[0] < this.width - 1:
					this.pos[0] += 1
			elif c == ord('q'):
				break
			elif c == ord('s'):
				this.shake()
				this.pastPos = list(this.pos)
				continue
			else:
			    continue
			stdscr.addstr(this.pastPos[1], this.pastPos[0], this.empty)
			this.pastPos = list(this.pos)

sketch = Sketch()
curses.wrapper(sketch.main)