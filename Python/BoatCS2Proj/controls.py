from pygame import *


class Functions():
    #create functions
    @staticmethod
    def ThrottleControlUp(pwr):
        pwr += 1
        time.sleep(0.1)
        return pwr
    
    @staticmethod
    def ThrottleControlDown(pwr):
        pwr += 1
        time.sleep(0.1)
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