#!/usr/bin/python3

from Stepper import Stepper
import RPi.GPIO as GPIO
import time
import json


GPIO.setmode(GPIO.BCM)

myStepper = Stepper(0x48)
# Infinite loop reading data from file saved by cgi code
prevAng = 0
while True:
  with open('/usr/lib/cgi-bin/stepper_control.txt','r') as f:
    data = json.load(f)
  print(data)

  angle = int(data["slider"])
  selection = data["Buttons"]
  print(angle)
  print(selection)
  if (selection !="Done"):

    if (selection == "Zero Motor"):
      print('zero')
      myStepper.zero()
      #run zero code
      angle = 0
      data = {"slider":"0","Buttons":"Done"}
      with open("/usr/lib/cgi-bin/stepper_control.txt",'w') as f:
        json.dump(data,f)

    elif (selection =="Change Angle"):
      print('angle')
      if ((angle - prevAng) > 0):
        if ((angle - prevAng) <180):
          dir = 1
          degrees = angle-prevAng
        else:
          dir = -1
          degrees = (360 - angle) + prevAng
      elif ((angle - prevAng)<0):
        if (abs((angle - prevAng)) < 180):
          dir = -1
          degrees = abs(angle-prevAng)
        else:
          dir = 1
          degrees = (360 - prevAng) + angle 
      else:
        dir = 1
        degrees = 0

      myStepper.goAngle(degrees,dir)
      data = {"slider":"0","Buttons":"Done"}
      with open("/usr/lib/cgi-bin/stepper_control.txt",'w') as f:
        json.dump(data,f)
    prevAng = angle

GPIO.cleanup()
