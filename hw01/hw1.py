import curses
import sys

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
		print("Use arrow keys to sketch")
		print("Press s key to reset the board")
		print("Press q key to quit")
		while True:
			this.cursor()
			c = stdscr.getch(this.height - 1, this.width - 1)
			if c == curses.KEY_UP:
				if this.pos[1] > 0:
					this.pos[1] -= 1
			elif c == curses.KEY_DOWN:
				if this.pos[1] < this.height - 1:
					this.pos[1] += 1
			elif c == curses.KEY_LEFT:
				if this.pos[0] > 0:
					this.pos[0] -= 1
			elif c == curses.KEY_RIGHT:
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
