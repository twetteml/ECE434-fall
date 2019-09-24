#!/usr/bin/env python
import sys
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

l_Encoder = RotaryEncoder(eQEP2)
l_Encoder.setAbsolute()
l_Encoder.enable()

r_Encoder = RotaryEncoder(eQEP1)
r_Encoder.setAbsolute()
r_Encoder.enable()

# Setting up matrix
bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

etch=[0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00]
        
empty=[0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00]
        
bus.write_i2c_block_data(matrix, 0, etch)

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

x = 3
y = 3
window = 7

r_pos = r_Encoder.position
l_pos = l_Encoder.position
new_r_pos = r_pos
new_l_pos = l_pos

while(1):

    new_r_pos = r_Encoder.position
    new_l_pos = l_Encoder.position
    if (new_l_pos < l_pos):
	    y = y + 1
	    if y>=window:
	        y=window
	    time.sleep(0.1)
    if (new_l_pos > l_pos):
	    y = y - 1
	    if y<0:
	        y=0
	    time.sleep(0.1)
    if (new_r_pos < r_pos):
	    x = x + 1
	    if x>=window:
	        x=window
	    time.sleep(0.1)
    if (new_r_pos > r_pos):
	    x = x - 1
	    if x < 0:
	        x=0
	    time.sleep(0.1)
    if GPIO.input(button1) and GPIO.input(button4):
	    bus.write_i2c_block_data(matrix, 0, empty)
	    break
    r_pos = new_r_pos
    l_pos = new_l_pos
    etch[2*x] = etch[2*x]|(0x80>>y)
    bus.write_i2c_block_data(matrix, 0, etch)
