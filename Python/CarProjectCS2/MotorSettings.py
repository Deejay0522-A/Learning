#from RPi.GPIO import * #type: ignore
#from gpiozero import Servo # type: ignore
#from gpiozero.pins.pigpio import PiGPIOFactory # type: ignore
import json
import os
from pathlib import Path

SAVESFILE = Path(__file__).parent / "saves"


settings = {}

motors = {}

# Inputs
session = input(f"Type your previous session's key or press Enter to make a new one.\n")
sessionName = input("Enter a session key. \n")
settings["key"] = sessionName

motorNums = int(input("How many motors are present?\n"))
for i in range(1, motorNums + 1):
    loop = i
    motorPin = input(f"What pin is motor{i}?\n")
    motors[f"motor{i}"] = motorPin
settings["motors"] = motors

print(settings)

#save/loading functions

