#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import json

GPIO.setmode(GPIO.BCM)

# Infinite loop reading data from file saved by cgi code
while True:
  with open('stepper_control.py','r') as f:
    data = json.load(f)

  value = float(data['slider'])

if value == 400:
  #run zero code
else:
  # determine if CW or CCW based on previous angle/ whether the angle needed to turn is greater than 180
  #run angle code


'''
from PCF8591 import PCF8591
from Stepper import Stepper
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
myStepper = Stepper(0x48)

try:
  print('here')
  #myStepper.goAngle(360,1)
  myStepper.zero()
except Exception as e: 
  print(e)
GPIO.cleanup()
'''