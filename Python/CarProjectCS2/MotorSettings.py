from RPi.GPIO import * #type: ignore
from gpiozero import Servo # type: ignore
from gpiozero.pins.pigpio import PiGPIOFactory # type: ignore
import time
import json
import os
from pathlib import Path

<<<<<<< Updated upstream
=======
MotorLF = Pin(21)
MotorRF = Pin(20)
MotorLB = Pin(16)
MotorRB = Pin(26)

class Controls():
    #create functions
    @staticmethod
    def ThrottleControl(pwr: int, ctrl: bool):
        if pwr >= 100:
            pwr = 100
            return pwr
        if ctrl:
            pwr += 1
            print("throttle up")
        elif not ctrl:
            pwr -= 1
            print("throttle down")
        stopper.sleep(0.1)
        return pwr
    
    @staticmethod
    def MotorSet(dir: str):
        if dir.lower() == 'forward':
            in1.ChangeState(True)
            in4.ChangeState(True)
            
        elif dir.lower() == 'backward':
            in2.ChangeState(True)
            in3.ChangeState(True)
        
        else:
            in1.ChangeState(False)
            in2.ChangeState(False)
            in3.ChangeState(False)
            in4.ChangeState(False)

        print(in1,in2,in3,in4) 
    
    @staticmethod
    def RudderSet(dir):
        print("rudder change")

        if dir == "Left":
            servo.value = -1
        elif dir == "Right":
            servo.value = 1
        elif not dir:
            servo.value = 0


# Setting up via settings

>>>>>>> Stashed changes
class Pin():
    def __init__(self, pinNum):
        self.state = False
        self.pinNum = pinNum
        setup(pinNum, OUT)
        output(pinNum, LOW)
        pass
    def ChangeState(self, newState):
        if newState:
            self.state = True
            output(self.pinNum, HIGH)
        else:
            self.state = False
            output(self.pinNum, LOW)

#change pins pls
forwardL = Pin(1)
forwardR = Pin(2)
backwardL = Pin(3)
backwardR = Pin(4)

my_factory = PiGPIOFactory()
servo = Servo(4, pin_factory = my_factory)

class Controls():
    #create functions
    @staticmethod
    def ThrottleControl(pwr: int, ctrl: bool):
        if pwr >= 100:
            pwr = 100
            return pwr
        if ctrl:
            pwr += 1
            print("throttle up")
        elif not ctrl:
            pwr -= 1
            print("throttle down")
        time.sleep(0.1)
        return pwr
    
    @staticmethod
    def Movement(dir: str):
        if dir.lower() == 'forward':
            print("Moving Ahead.")
            forwardL.ChangeState(True)
            forwardR.ChangeState(True)
            
        elif dir.lower() == 'backward':
            print("Falling Back")
            backwardL.ChangeState(True)
            backwardR.ChangeState(True)
        
        else:
            print("off")
            forwardL.ChangeState(False)
            forwardR.ChangeState(False)
            backwardL.ChangeState(False)
            backwardR.ChangeState(False)
    
    @staticmethod
    def Rotation(dir):
        print("rudder change")

        if dir == "left":
            servo.value = -1
        elif dir == "right":
            servo.value = 1
        elif not dir:
            servo.value = 0