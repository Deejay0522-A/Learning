#forgot to turn this in last time, i thought you were just checking the file yourself not expecting a submission

import time

class LED():
    def __init__(self, voltage, color, current):
        self.current = current
        self.voltage = voltage
        self.color = color
        self.state = False

    def blink(self, changeState, repeat, delay=0.5):
        repeat = int(input("How many times do you want the LED to blink?: "))

        for i in range(repeat):
            if self.state:
                self.state = not self.state
                print(f"{self.color} LED is ON")
            else:
                self.state = not self.state
                print(f"{self.color} LED is OFF")
            time.sleep(delay)

ledOne = LED(3.1, "blue", 10)
ledTwo = LED(2.1, "yellow", 20)
ledThree = LED(2.1, "red", 20)

ledList = [ledOne, ledTwo, ledThree]

loop = True

while loop:
    gen = input("Would you like to run? (y/n): ").lower()

    if gen == "y":
        ledChoice = int(input("Which LED would you like to use? (1: blue | 2: yellow | 3: red): "))

        print(f"{ledList[ledChoice - 1].color} LED: Voltage: {ledList[ledChoice - 1].voltage}V, Current: {ledList[ledChoice - 1].current}mA")

        blinkChoice = input("Would you like to blink this LED? (y/n): ").lower()

        if blinkChoice == "y":
            ledList[ledChoice - 1].blink(ledList[ledChoice - 1].state, 0)
        else: continue
    else:
        loop = False
        break