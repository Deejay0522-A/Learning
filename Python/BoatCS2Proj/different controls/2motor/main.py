from pygame import *
from controls import *
#from motorSetup import *
# from RPi.GPIO import * #type: ignore
import time


#setup CMDS
# BoardSetup.BoardSetup()

#variables
throttle = 0

init()
#Use for keybinds
screen = display.set_mode((800, 600))

running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False 

    keys = key.get_pressed()

    if keys[K_w]:
        print("Forward")
        Controller.LeftMotor(True, True)
        Controller.RightMotor(True, True)
    elif keys[K_a]:
        print("Left")
        Controller.LeftMotor(True, True)
        Controller.RightMotor(False, None)
    elif keys[K_d]:
        print("Right")
        Controller.LeftMotor(False, None)
        Controller.RightMotor(True, True)
    elif keys[K_s]:
        print("Back")
        Controller.LeftMotor(True, False)
        Controller.RightMotor(True, False)
    elif keys[K_s] and keys[K_d]:
        print("Back Right")
        Controller.LeftMotor(True, False)
        Controller.RightMotor(False, None)
    elif keys[K_s] and keys[K_a]:
        print("Back Left")
        Controller.LeftMotor(False, None)
        Controller.RightMotor(True, False)

    elif keys[K_i]:
        Controller.ThrottleControl(throttle, True)
    elif keys[K_o]:
        Controller.ThrottleControl(throttle, False)
    else:
        print("off")
        Controller.LeftMotor(False, None)
        Controller.RightMotor(False, None)

display.flip()



quit()