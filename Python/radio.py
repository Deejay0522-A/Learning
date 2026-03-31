from microBit import *
import radio

generator = True    

radio.on()

radio.config(channel=10,length=100)


def recieveRad():
    while generator:
        message = radio.recieve()

        if message:
            print(message)

def sendRad():
    while generator:
        message = input("message: ")

        radio.send(message)