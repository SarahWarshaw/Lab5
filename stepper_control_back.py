#!/usr/bin/python3

#from PCF8591 import PCF8591
#from Stepper import Stepper
#import RPi.GPIO as GPIO
#import time
import json

#GPIO.setmode(GPIO.BCM)

# myStepper = Stepper(0x48)
# Infinite loop reading data from file saved by cgi code
prevAng = 0
while True:
  with open('stepper_control.txt','r') as f:
    data = json.load(f)
  # selection = data['Buttons']
  #angle = int(data['slider'])


  #if selection == 'Zero Motor':
    #myStepper.zero()
    #run zero code
  #else:
  #  myStepper.goAngle(angle,dir)
    # determine if CW or CCW based on previous angle/ whether the angle needed to turn is greater than 180
    #run angle code
  #prevAng = angle
  #with open('stepper_control.txt','w') as f:
    #data = {"slider":0,"Buttons": "Change Angle"}
    #json.dump(data,f)

  #GPIO.cleanup()
