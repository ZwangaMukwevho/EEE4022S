# from rfid import rfid
import RPi.GPIO as GPIO
from temp import temp
from rfid import rfid
from LED import LED
from db import database
import time
import asyncio

async def checkTemp(tempObj,LEDObj,loop):
    """Samples temperature reading and returns it, and also flashes RED or GREEN LED based on weather the temp reading is higher than threshold.

    :param tempObj: [Object from Temp class]
    :type tempObj: [temp]
    :param LEDObj: [Object from LED class]
    :type LEDObj: [LED]
    :param loop: [Main event loop to be used to run coroutines concurrenlty]
    :type loop: [asyncio application]
    :return: [Temperature value of target object]
    :rtype: [float]
    """
    tic = time.perf_counter()
    tempValue = await asyncio.gather(tempObj.readTemp())
    toc = time.perf_counter()  
    if tempValue[0] < 35.00 and tempValue[0] > 29.00:
        tic = time.perf_counter() 
        asyncio.gather(LEDObj.swichOnTempGreen())
        toc = time.perf_counter()  
        return tempValue
        
    else:
        tic = time.perf_counter()
        asyncio.gather(LEDObj.swichOnTempRed())
        toc = time.perf_counter()  
        return tempValue
        
async def checkRficCard(text,LEDObj,dbObj,loop):
    """[Checks if student number exists in database and returns True if it exists in database, and False otherwise. Green LED toggled in True case, Red toggled in False case ]

    :param text: [The student number]
    :type text: [String]
    :param LEDObj: [Object of LED class]
    :type LEDObj: [LED]
    :param dbObj: [Database object from db class with functions for accessing remote database]
    :type dbObj: [db]
    :param loop: [Main event loop to be used to run coroutines concurrenlty]
    :type loop: [asyncio application]
    :return: [True if student number exists in database, and false otherwise]
    :rtype: [boolean]
    """
    tic = time.perf_counter()
    results = await dbObj.findStudentNumber(text)
    toc = time.perf_counter()

    if len(results) != 0:
        tic = time.perf_counter()
        asyncio.gather(LEDObj.swichRfidOnRed())  
        toc = time.perf_counter()    
        return True
    else:
        tic = time.perf_counter()
        asyncio.gather(LEDObj.swichRfidOnGreen())
        toc = time.perf_counter()      
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

    loop = asyncio.get_event_loop()
    while(True):
        student_no = loop.run_until_complete(rfidObj.readData())
        rfidCheck = loop.run_until_complete(checkRficCard(student_no,LEDObj,dbObj,loop))
        print(student_no)
        
        if(rfidCheck):
            tempCheck = loop.run_until_complete(checkTemp(tempObj,LEDObj,loop))

            if(tempCheck[0] <34.50 ):
                # Run marking of attendance register and posting to database concurrently
                loop.run_until_complete(asyncio.gather(dbObj.markAttendance(student_no),dbObj.postTempReading(student_no,tempCheck[0])))
                time.sleep(0.5)
                

