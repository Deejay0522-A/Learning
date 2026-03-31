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


display.flip()



quit()