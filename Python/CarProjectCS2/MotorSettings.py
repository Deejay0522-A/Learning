#from RPi.GPIO import * #type: ignore
#from gpiozero import Servo # type: ignore
#from gpiozero.pins.pigpio import PiGPIOFactory # type: ignore
import json
import os
from pathlib import Path

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