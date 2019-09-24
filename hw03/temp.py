#!/usr/bin/env python
import sys
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

led1 = "P8_7"
led2 = "P8_8"
tempAlert2 = "P8_15"
tempAlert1 = "P8_16"

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

#GPIO.setup(tempAlert2, GPIO.IN)
#GPIO.setup(tempAlert1, GPIO.IN)

bus = smbus.SMBus(2)
temp1 = 0x48
temp2 = 0x4a
#Thigh = 28
#Tlow = 23
alarm = [tempAlert1, tempAlert2]

def handleAlarm(alertPin):
    if(alertPin == alarm[0]):
        print("Temperature 1 out of range of Thigh and Tlow", end= "\n")
        GPIO.output(led1, GPIO.HIGH)
        time.sleep(0.2)
    if(alertPin == alarm[1]):
        print("Temperature 2 out of range of Thigh and Tlow", end= "\n")
        GPIO.output(led2, GPIO.HIGH)
        time.sleep(0.2)

for alarmVar in alarm:
    GPIO.setup(alarmVar, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(alarmVar, GPIO.BOTH, callback=handleAlarm)

#writing high and low data for 1
bus.write_byte_data(temp1, 3, 27)
bus.write_byte_data(temp1, 2, 23)

#writing high and low data for 2
bus.write_byte_data(temp2, 3, 27)
bus.write_byte_data(temp2, 2, 23)

while(1):
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    temp11 = bus.read_byte_data(temp1, 0)
    temp22 = bus.read_byte_data(temp2, 0)
    print("Temperature 1: " + str(temp11), end=" ")
    print("Temperature 2: " + str(temp22), end="\r")