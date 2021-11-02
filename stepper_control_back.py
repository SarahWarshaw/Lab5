#!/usr/bin/python3

import RPi.GPIO as gpio
import time
import json

# Set gpio pins as outputs with 100 Hz frequency
gpio.setmode(gpio.BCM)
gpio.setup(13, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.setup(26, gpio.OUT)
pwm1 = gpio.PWM(13, 100)
pwm2 = gpio.PWM(19, 100)
pwm3 = gpio.PWM(26, 100)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)

# Infinite loop reading data from file saved by cgi code
while True:
  with open('stepper_control.txt','r') as f:
    data = json.load(f)

# duty cycle (1-100) is the value of 'slider' and ledPin(13,19, or 26) is the value of 'LED'
  dutyCycle = float(data['slider'])
  ledPin = data['Buttons']

#from PCF8591 import PCF8591
#from Stepper import Stepper
#import RPi.GPIO as GPIO
#import time
import json

#GPIO.setmode(GPIO.BCM)

# myStepper = Stepper(0x48)
# Infinite loop reading data from file saved by cgi code
prevAng = 0
#while True:
with open('stepper_control.txt','r') as f:
   data = json.load(f)
print(data)
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
