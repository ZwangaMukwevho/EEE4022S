#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from LED import LED

reader = SimpleMFRC522()

class rfid:
        reader = SimpleMFRC522()
        LEDObj = LED()
        def __init__(self):
               
                # GPIO.setmode(GPIO.BCM)
                pass
        
        def writeData(self):
                """ Wrties data to RFID card
                """
                try:
                        text = input('New data:')
                        print("Now place your tag to write")
                        reader.write(text)
                        print("Written")
                finally:
                        GPIO.cleanup()
        
        def readData(self,check):
                """Reads Data from the rfid card
                Turns on green LED if access granted
                Turns on RED LED if access denied"""
                try:
                        print("running")
                        id, text = reader.read()
                        # print(id)
                        print(text)

                        text = text.strip()
                        if text == check:
                                print("true")
                                self.LEDObj.swichOnGreen()
                        else:
                                print("false")
                                self.LEDObj.swichOnRed()
                        
                finally:
                        GPIO.cleanup()

rfid_obj = rfid()
# rfid_obj.readData("MKWZWA003")
rfid_obj.writeData()

print("hello world")
GPIO.cleanup()