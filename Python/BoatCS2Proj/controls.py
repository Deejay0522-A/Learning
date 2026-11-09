from pygame import * #type: ignore
from RPi.GPIO import * #type: ignore
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from os import * # type: ignore
import subprocess
import time as stopper

setmode(BCM)

#password = ""
#sudoProcess = subprocess.Popen(f"sudo pigpiod")
#sudoProcess.stdin.write(f"{password}\n")
#sudoProcess.stdin.flush()
#procOutput, procError = sudoProcess.communicate()

my_factory = PiGPIOFactory()
servo = Servo(4, pin_factory = my_factory)

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

in1 = Pin(21)
in2 = Pin(20)
in3 = Pin(16)
in4 = Pin(26)

class Functions():
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


Controller = Functions()