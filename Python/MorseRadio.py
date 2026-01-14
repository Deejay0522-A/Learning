from microbit import * # pyright: ignore
import music # type: ignore
import button #type: ignore
import radio #type: ignore

loop = True

button_a = button
button_b = button

radio.on()
radio.config(channel=7, length=100)

while loop:
    message = radio.recieve()

    if message:
        music.play(message)

    sendMess = None
    print(temperature()) # type: ignore
    if button_a.is_pressed(): #c = -
        music.play(['c'])
        sendMess = ['c']
    elif button_b.is_pressed(): #d = .
        music.play(['d'])
        sendMess = ['d']
