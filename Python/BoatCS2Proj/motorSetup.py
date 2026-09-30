from RPi.GPIO import * #type: ignore

class GpioSetup():
    @staticmethod
    def BoardSetup():
        boardType: str = str(__builtins__.input("Which board type? (BCM/)"))

        if boardType.lower() == "bcm":
            setmode(BCM)
        else:
            setmode(BOARD)

BoardSetup = GpioSetup()