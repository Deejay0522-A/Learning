from gpiozero import Button # type: ignore
import time

button = Button(26, bounce_time=0.1)

def ButtonPress():
    print("Button Pushed")

button.when_pressed = ButtonPress()

message = input("press enter to quit")