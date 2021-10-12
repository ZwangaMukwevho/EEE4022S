import gspread
from db import database
import asyncio

class sheets:
    def __init__(self):
        self.gc1 = gspread.service_account(filename='credantials.json')
        self.sh1 = self.gc1.open_by_key('1b53CQsonQUc2DCce_fnXoeHTh2qXH1l8wuWrzDHqB4k')
        self.courseWorksheet = self.sh1.sheet1
        self.res1 = self.courseWorksheet.get_all_records()
        
        pass

    # def getCourseData(self):
    #     res = self.courseWorksheet.get_all_records()
    #     print(res)
    
    def checkCourseExistance(self,course,dbObj):
        query = "SELECT * FROM course WHERE  code = '{}'".format(course)
        cursor = dbObj.getDB()
        cursor.execute(query)

        check = False
        for item in cursor:
            # check = True
            return True
            # break
        return False
    
    async def AddCourse(self,dbObj):

        first_entry = True
        moreValues = None # Stores value for insert statement with multiple row entries
        # Checking if items are in database and if not adding them to query
        for entry in self.res1:
            course_code = entry['Course Code']
        
            # If entry already exists in database
            if( not self.checkCourseExistance(course_code,dbObj)):

                if(first_entry):
                    course_name = entry['Course name']
                    query = "INSERT INTO course(code,course_name) VALUES('{}','{}');".format(course_code,course_name)
                    first_entry = False
                else:
                    moreValues = "('{}','{}');".format(course_code,course_name)
                
                query = self.gatherInsertQueries(query,moreValues)
        
        print(query)
        await dbObj.insertData(query)
    
    async def showCourses(self,dbObj):
        cursor = dbObj.getDB()
        cursor.execute("SELECT * FROM course ORDER BY code ASC;")

        for item in cursor:
            out = "Course code: {}, Course name: {}".format(item[0],item[1])
            print(out)
       
    
    def gatherInsertQueries(self,query,newValues=None):
        """Combine multiple insert queries into one query,
        In order to allow one call to the db instead of multiple calls

        :param query: The first values to be inserted in the table, (Leading statements of the insert statements)
        :type query: [String]
        :param newValues: [The additional values that have to the leading statement of the query], defaults to None
        :type newValues: [String], optional
        :return: [The new query that has old values and the new values]
        :rtype: [String]
        """
        if(newValues is not None):
            query = query[:-1] + ", "+ newValues
        else:
            query = query
        return query




    
    # def AddCourse(self,dbObj):
    #     res = self.courseWorksheet.get_all_records()
    #     for entry in 

# Initialisations
# dbObj = database("eee4022sdatabase-do-user-9871310-0.b.db.ondigitalocean.com",
#     "admin",
#     "aGAPX1Hn5TdTE-4I",
#     "lab_system",
#     "25060",
#     "mysql_native_password"
#     )
# sheetObj = sheets()
# loop = asyncio.get_event_loop()
# # loop.run_until_complete(sheetObj.AddCourse(dbObj))
# loop.run_until_complete(sheetObj.showCourses(dbObj))
# # sheetObj.getCourseData()