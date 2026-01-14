import RPi.GPIO as GPIO  # pyright: ignore[reportMissingModuleSource]
import pynput
from pynput import keyboard
import time

GPIO.setmode(26, GPIO.OUT)
GPIO.setup()

activity = GPIO.output(26, GPIO.HIGH)
noActivity = GPIO.output(26, GPIO.LOW)

loop = True

def on_press(key):
    keyPressed = str(key)
    try:
        print(f"Key Pressed: {key.char}")
        print(f"keypress: {keyPressed}")
    except AttributeError:
        print(f"Special Key: {key}")
        print(f"keypress: {keyPressed}")
    
    if keyPressed == "Key.esc":
        loop = False
        print(loop)
        return False
    
def MorseCode(hi, low):
    #.... --- .-.. -.. . -. .----. ... / --. .- -.--
    #sleep(0.1) = .
    #sleep(0.5) = -

    for i in range(0,4): #....
        hi
        time.sleep(0.1)
        low
        time.sleep(0.1)
    for i in range(0,3): #---
        hi
        time.sleep(0.5)
        low
        time.sleep(0.1)
    #.-..
    hi
    time.sleep(0.1)
    low
    time.sleep(0.1)
    hi
    time.sleep(0.5)
    low
    time.sleep(0.1)
    hi
    time.sleep(0.1)
    low
    time.sleep(0.1)
    hi
    time.sleep(0.1)
    low
    time.sleep(0.1)
    #-..
    hi
    time.sleep(0.5)
    low
    time.sleep(0.1)
    hi
    time.sleep(0.1)
    low
    time.sleep(0.1)
    hi
    time.sleep(0.1)
    low
    time.sleep(0.1)
    #.
    hi
    time.sleep(0.1)
    low
    time.sleep(0.1)
    #-.
    hi
    time.sleep(0.5)
    low
    time.sleep(0.1)
    hi
    time.sleep(0.1)
    low
    time.sleep(0.1)
    #.----.
    hi
    time.sleep(0.1)
    low
    time.sleep(0.1)
    for i in range(0,4):
        hi
        time.sleep(0.5)
        low
        time.sleep(0.1)
    hi
    time.sleep(0.1)
    low
    time.sleep(0.1)

    for i in range(0,3): #...
        hi
        time.sleep(0.1)
        low
        time.sleep(0.1)

    time.sleep(1) #/

    #--.
    for i in range(0,2):
        hi
        time.sleep(0.5)
        low
        time.sleep(0.1)
    hi
    time.sleep(0.1)
    low
    time.sleep(0.1)

    #.-
    hi
    time.sleep(0.1)
    low
    time.sleep(0.1)
    hi
    time.sleep(0.5)
    low
    time.sleep(0.1)

    #-.--
    hi
    time.sleep(0.5)
    low
    time.sleep(0.1)
    hi
    time.sleep(0.1)
    low
    time.sleep(0.1)
    for i in range(0,2):
        hi
        time.sleep(0.5)
        low
        time.sleep(0.1)

while loop:
    MorseCode(activity, noActivity)


    with keyboard.Listener(
    on_press=on_press) as listener:
        listener.join()