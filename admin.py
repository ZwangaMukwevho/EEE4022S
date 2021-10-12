import os
from sheets import sheets
import asyncio
from db import database
from datetime import datetime

class admin:
    def __init__(self,dbObj,sheetsObj):
        self.sheetsObj = sheetsObj
        self.dbObj = dbObj
        self.loop = asyncio.get_event_loop()
    
    def welcomeDisplay(self):
        os.system('clear')
        print('              __________                               _________')
        print('|         |  |             |           |              /          \ ')
        print('|         |  |             |           |             /            \ ')
        print('|         |  |             |           |            |              |')
        print('|---------|  |----------   |           |            |              |')
        print('|         |  |             |           |            |              |')
        print('|         |  |             |           |             \            /')
        print('|         |  |__________   |__________ |__________    \_________ /')
    
    def dispayMenue(self):
        keepRunning = True
        while(keepRunning):

            print("")
            print("Press '1' to update courses in database:")
            print("press '2' to update lab schedule:")
            print("Press '3' to view courses in databases:")
            print("Press '4' to view register for a specific course:")
            print("Press 'q' to quit: ")
            inValue = input("")

            if inValue == '1':
                print("updating courses")
                self.loop.run_until_complete(self.sheetsObj.AddCourse(self.dbObj))
                print("done updating courses")
            
            if inValue == '3':
                print("")
                print("The following courses are on the database")
                self.loop.run_until_complete(self.sheetsObj.showCourses(self.dbObj))
            
            if inValue == 'q':
                print("quitting")
                keepRunning = False

    
    def updateCourse(self):
        pass


if __name__ == "__main__":
    dbObj = database("eee4022sdatabase-do-user-9871310-0.b.db.ondigitalocean.com",
    "admin",
    "aGAPX1Hn5TdTE-4I",
    "lab_system",
    "25060",
    "mysql_native_password"
    )
    datetime_obj = datetime.strptime("10/15/2021", "%m/%d/%Y")
    print(datetime_obj)
    # sheetObj = sheets()
    # adObj = admin(dbObj,sheetObj)
    # adObj.welcomeDisplay()
    # adObj.dispayMenue()



