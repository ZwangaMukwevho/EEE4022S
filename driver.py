# from rfid import rfid
import RPi.GPIO as GPIO
from temp import temp
from rfid import rfid
from LED import LED

def checkTemp(tempObj,LEDObj):
    if(tempObj.readTemp()) > 25.00:
        LEDObj.swichOnTempRed()
        print("too much")
    else:
        LEDObj.swichOnTempGreen()
        print("perfect")

def checkRficCard(rfidObj,LEDObj,validateText):
    # text = rfidObj.readData()
    # print("text "+str(text))
    print("validate text "+validateText)
    if validateText == text:
        LEDObj.swichRfidOnGreen()
    else: 
        LEDObj.swichRfidOnRed()

    pass

if __name__ == "__main__":
    tempObj = temp()  # Temp class object
    rfidObj = rfid() # rfid object object
    LEDObj = LED() # #LED class object
    # print(GPIO.getmode())
    # mfrc22 module uses BCM mode, if you set-up GPIO using board mode, the data won't be read
    checkRficCard(rfidObj,LEDObj,"MKWZWA003")
    checkTemp(tempObj,LEDObj)
    
    