#!/usr/bin/env python

# Python script for toggling
# Madeline Twetten

import Adafruit_BBIO.GPIO as GPIO
import time

pin1 = "P9_12"
GPIO.setup(pin1, GPIO.OUT)
toggle = 0
period = 0.1

while(1):
    if toggle==0:
        GPIO.output(pin1, GPIO.HIGH)
        toggle = 1
        time.sleep(period/2)
    else:
        GPIO.output(pin1, GPIO.LOW)
        toggle = 0
        time.sleep(period/2)
