#!/usr/bin/python3

from PCF8591 import PCF8591
from Stepper import Stepper
import RPi.GPIO as GPIO
import time
import json

GPIO.setmode(GPIO.BCM)

myStepper = Stepper(0x48)
# Infinite loop reading data from file saved by cgi code
prevAng = 0
try:
  while True:
    with open('stepper_control.txt','r') as f:
      data = json.load(f)

    value = float(data['slider'])

    if value == 400:
      myStepper.zero()
      #run zero code
    else:
      myStepper.goAngle(abs(value-prevAng),dir)
      # determine if CW or CCW based on previous angle/ whether the angle needed to turn is greater than 180
      #run angle code
    prevAng = value
    with open('stepper_control.txt','w') as f:
      data = {"slider":0}
      json.dump(data,f)
      

except Exception as e: 
  print(e)
GPIO.cleanup()
