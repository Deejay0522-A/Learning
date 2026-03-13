from RPi.GPIO import * #type: ignore

class GpioSetup():
    @staticmethod
    def BoardSetup():
        boardType: str = input("Which board type? (BCM/)")

        if boardType.lower() == "bcm":
            setmode(BCM)
        else:
            setmode(BOARD)

BoardSetup = GpioSetup()