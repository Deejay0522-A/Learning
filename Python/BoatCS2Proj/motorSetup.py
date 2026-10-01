from RPi.GPIO import * #type: ignore
from gpiozero import Servo # type: ignore
from gpiozero.pins.pigpio import PiGPIOFactory # type: ignore

class GpioSetup():
    @staticmethod
    def BoardSetup():
        setmode(BCM)
    @staticmethod
    def RudderSetup(pInput: int):
        servo = Servo(pInput,
                      min_pulse_width=0.0005, 
                      max_pulse_width=0.0025, 
                      pin_factory=PiGPIOFactory())
        return servo

BoardSetup = GpioSetup()