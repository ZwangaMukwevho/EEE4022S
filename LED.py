import RPi.GPIO as GPIO
import time
import asyncio

class LED:
    
    def __init__(self): 
            pass
    
    async def swichRfidOnGreen(self):
        """Switches on green Green LED on and off for the RFID subsystem
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(24,GPIO.OUT)
        GPIO.output(24,GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(24,GPIO.LOW)
    
    async def swichRfidOnRed(self):
        """Switches on green RED LED on and off for the RFID subsystem
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(23,GPIO.OUT)
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.7) 
        GPIO.output(23,GPIO.LOW) 

    async def swichOnTempRed(self):
        """Switches on green RED LED on and off for the Temperature subsystem
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(17,GPIO.OUT)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(17,GPIO.LOW)

    async def swichOnTempGreen(self):
        """Switches on green GREEEN LED on and off for the TEMP subsystem
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(27,GPIO.OUT)
        GPIO.output(27,GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(27,GPIO.LOW)
    