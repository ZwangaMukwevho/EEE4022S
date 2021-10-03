# from rfid import rfid
import RPi.GPIO as GPIO
from temp import temp
from rfid import rfid
from LED import LED
from db import database

def checkTemp(tempObj,LEDObj):
    if(tempObj.readTemp()) > 25.00:
        LEDObj.swichOnTempRed()
        print("too much")
    else:
        LEDObj.swichOnTempGreen()
        print("perfect")

def checkRficCard(rfidObj,LEDObj,dbObj):
    text = rfidObj.readData()
    results = dbObj.findStudentNumber(text)
    if len(results) != 0:
        LEDObj.swichRfidOnGreen()
        print("green")
        return True
    else: 
        LEDObj.swichRfidOnRed()
        print("false")
        return False

    pass

if __name__ == "__main__":
    tempObj = temp()  # Temp class object
    rfidObj = rfid() # rfid object object
    LEDObj = LED() # #LED class object
    dbObj = database("eee4022sdatabase-do-user-9871310-0.b.db.ondigitalocean.com",
    "admin",
    "aGAPX1Hn5TdTE-4I",
    "lab_system",
    "25060",
    "mysql_native_password") # database class object


    # print(GPIO.getmode())
    # mfrc22 module uses BCM mode, if you set-up GPIO using board mode, the data won't be read
    rfidCheck = checkRficCard(rfidObj,LEDObj,dbObj)
    
    # if(rfidCheck):
    #     print("succesful RFID check")
    #     checkTemp(tempObj,LEDObj)
    
    