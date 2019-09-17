#!/usr/bin/env python

# Madeline Twetten
# ECE 434 HW 2
# Blink LEDs

import Adafruit_BBIO.GPIO as GPIO

button1 = "P8_11"
button2 = "P8_12"
button3 = "P8_17"
button4 = "P8_18"

led1 = "P8_7"
led2 = "P8_8"
led3 = "P8_9"
led4 = "P8_10"

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while(1):
    if GPIO.input(button1):
        GPIO.output(led1, GPIO.HIGH)
        
    elif GPIO.input(button2):
        GPIO.output(led2, GPIO.HIGH)
        
    elif GPIO.input(button3):
        GPIO.output(led3, GPIO.HIGH)
        
    elif GPIO.input(button4):
        GPIO.output(led4, GPIO.HIGH)
        
    else:
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(led4, GPIO.LOW)
        