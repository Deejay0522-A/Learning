from pygame import *
#from RPi.GPIO import * #type: ignore
import time as stopper

class Pin():
    """def __init__(self, state, pinNum):
        self.state = state
        setup(pinNum, OUT)
        pass"""

    def ChangeState(self):
        if self.state:
            self.state = False
        else:
            self.state = True


class Functions():
    #create functions
    @staticmethod
    def ThrottleControl(pwr: int, ctrl: bool):
        if ctrl:
            pwr += 1
            print("throttle up")
        elif not ctrl:
            pwr -= 1
            print("throttle down")
        stopper.sleep(0.1)
        return pwr
    
    @staticmethod
    def LeftMotor(bInput, dir):
        #Left motor GPIO
        return
    @staticmethod
    def RightMotor(bInput, dir):
        #Left motor GPIO
        return

Controller = Functions()