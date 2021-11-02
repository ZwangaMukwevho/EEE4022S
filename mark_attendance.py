import asyncio
from LED import LED
from rfid import rfid
from db import database
import time

if __name__ == "__main__":
    # initialise objects
    rfidObj = rfid() # rfid object object
    LEDObj = LED() # #LED class object
    dbObj = database("eee4022sdatabase-do-user-9871310-0.b.db.ondigitalocean.com",
    "admin",
    "aGAPX1Hn5TdTE-4I",
    "lab_system",
    "25060",
    "mysql_native_password") # 


    loop = asyncio.get_event_loop()

    while(True):
        
        student_no = loop.run_until_complete(rfidObj.readData())
        loop.run_until_complete(asyncio.gather(dbObj.markAttendance(student_no)))
        output = "processed {}".format(student_no)
        print(output)
        time.sleep(0.5)
    