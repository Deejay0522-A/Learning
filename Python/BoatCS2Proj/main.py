from pygame import *
from controls import *
import time

#variables
throttle = 0

init()
#Use for keybinds
screen = display.set_mode((800, 600))

running = True

while running:
    for e in event.get:
        if e.type == QUIT:
            running = False 

display.flip()



quit()