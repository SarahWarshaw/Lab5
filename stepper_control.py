from Stepper import Stepper
import RPi.GPIO as GPIO
import time

myStepper = Stepper(0x48)

try:
  X = myStepper.__turnSteps()
except:
  pass
GPIO.cleanup()