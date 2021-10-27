from PCF8591 import PCF8591
import RPi.GPIO as GPIO
import time
import smbus

class Stepper:
  pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
  sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
        [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

  state = 0 #current position in stator sequence 
  
  def __init__(self,address):
    self.myPCF8591 = PCF8591(address)
    for pin in Stepper.pins:
      GPIO.setup(pin, GPIO.OUT, initial=0)


  def delay_us(self,tus): # use microseconds to improve time resolution
    endTime = time.time() + float(tus)/ float(1E6)
    while time.time() < endTime:
      pass
  
  def __halfstep(self):
    # dir = +/- 1 for CCW or CW
    Stepper.state += dir
    if Stepper.state>7: Stepper.state = 0
    elif Stepper.state<0: Stepper.state = 7
    for pin in range(4):    # 4 pins that need to be energized
      GPIO.output(Stepper.pins[pin], Stepper.sequence[Stepper.state][pin])
    self.delay_us(1000)
    
  def __turnSteps(self,steps,dir):   
    for step in range(steps):
      self.__halfstep(dir)

  # def goAngle(self, angle):
    # move to a specified angle
  # def zero(self):
    # turn the motor until the photores
  