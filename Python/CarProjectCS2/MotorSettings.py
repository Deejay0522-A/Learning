from pygame import * #type: ignore
import RPi.GPIO as GPIO #type: ignore
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from os import * # type: ignore
import subprocess
import time as stopper

class Pin:
    def __init__(self, pinNum):
        self.state = False
        self.pinNum = pinNum
        GPIO.setup(pinNum, GPIO.OUT)
        GPIO.output(pinNum, GPIO.LOW)
        pass
    def ChangeState(self, newState):
        self.state = bool(newState)
        GPIO.output(
            self.pinNum,
            GPIO.HIGH if self.state else GPIO.LOW,
        )

my_factory = PiGPIOFactory()
servo = Servo(5, pin_factory = my_factory)

# change pins

motor1Forward = Pin(1)
motor1Backward = Pin(2)
motor2Forward = Pin(3)
motor2Backward = Pin(4)

class Controls:
    @staticmethod
    def Movement(dir : str):
        if dir.lower() == 'forward':
            motor1Forward.ChangeState(True)
            motor2Forward.ChangeState(True)
            
        elif dir.lower() == 'backward':
            motor1Backward.ChangeState(True)
            motor2Backward.ChangeState(True)
        
        else:
            motor1Forward.ChangeState(False)
            motor1Backward.ChangeState(False)
            motor2Forward.ChangeState(False)
            motor2Backward.ChangeState(False)
    
    @staticmethod
    def Rotation(dir : str):
        if dir == "Left":
            servo.value = -1
        elif dir == "Right":
            servo.value = 1
        elif not dir:
            servo.value = 0