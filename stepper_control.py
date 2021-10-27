from PCF8591 import PCF8591
from Stepper import Stepper
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
myStepper = Stepper(0x48)

try:
  print('here')
  myStepper.goAngle(360,1)
except Exception as e: 
  print(e)
GPIO.cleanup()