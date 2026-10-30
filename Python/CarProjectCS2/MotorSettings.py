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

savedSettings = {}

if session != "":
    for save in SAVESFILE.glob("*.json"):
        try:
            with save.open() as saveFile:
                data = json.load(saveFile)
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(data, dict) and data.get("key") == session:
            savedSettings = data
            break

if savedSettings:
    settings = savedSettings
    motors = settings.get("motors", {})
else:
    sessionName = input("Enter a session key. \n")
    settings["key"] = sessionName
    motorNums = int(input("How many motors are present?\n"))
    for i in range(1, motorNums + 1):
        loop = i
        motorPin = input(f"What pin is motor{i}?\n")
        motors[f"motor{i}"] = motorPin
    settings["motors"] = motors

    print(settings)

with open(SAVESFILE / f"{sessionName}.json", "w", encoding="utf-8") as file:
    json.dump(settings, file, indent=4)

print(f"File created as: {sessionName}.json")


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

for m in settings["motors"]:
    print(m)