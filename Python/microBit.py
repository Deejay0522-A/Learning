#code for freshman

from microbit import * #type:ignore
import radio #type:ignore
import display #type: ignore
import button_a #type:ignore
import button_b #type:ignore

radio.on
radio.config(channel=7, length=50)

loop = True

while loop:
    messageRecieved = radio.receive()

    if messageRecieved:
        display.scroll(messageRecieved)
    else:
        if button_a.is_pressed():
            print("Button Pressed, Now Sending")
            message = input("What do you want to say?\n")
            radio.send(message)
            continue