from pygame import *
from RPi.GPIO import * #type: ignore

class Pin():
    def __init__(self, state, pinNum):
        self.state = state
        setup(pinNum, OUT)
        pass

    def ChangeState(self):
        if self.state:
            self.state = False
        else:
            self.state = True


class Functions():
    #create functions
    @staticmethod
    def ThrottleControlUp(pwr):
        pwr += 1
        time.sleep(0.1)
        print("throttle up")
        return pwr
    
    @staticmethod
    def ThrottleControlDown(pwr):
        pwr += 1
        time.sleep(0.1)
        print("Throttle down")
        return pwr
    
    @staticmethod
    def LeftMotor(bInput):
        #Left motor GPIO
        return
    @staticmethod
    def RightMotor(bInput):
        #Left motor GPIO
        return

Controller = Functions()