from Stepper import Stepper
import RPi.GPIO as GPIO
import time

myStepper = Stepper(0x48)

try:
  print('here')
  myStepper.__turnSteps(500,1)
  print(myStepper)
except:
  pass
GPIO.cleanup()