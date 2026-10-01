from pygame import * # type: ignore
from controls import *
from motorSetup import * # type: ignore
from RPi.GPIO import * #type: ignore
import time

setmode(BCM)

#GpioSetup.RudderSetup(4)

init()
screen = display.set_mode((800, 600))
running = True
throttle = 0
tick = 0

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                Functions.MotorSet('forward')
                print("Forward")
            elif e.key == K_s:
                Functions.MotorSet('backward')
            elif e.key == K_a:
                Functions.RudderSet("Left")
            elif e.key == K_d:
                Functions.RudderSet("Right")
        elif e.type == KEYUP:
            if e.key == K_w or e.key == K_s:
                Functions.MotorSet("off")
            elif e.key == K_a or e.key == K_d:
                Functions.RudderSet(None)


    display.flip()

quit()