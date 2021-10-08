# import MySQLdb
import mysql.connector
import asyncio
from datetime import datetime

class database:
    db = None
    cursor = None

    def __init__(self,hostVar,userVar,passwdVar,databaseVar,portVar,auth_pluginVar):
        self.db = mysql.connector.connect(
        host= hostVar,
        user=userVar,
        passwd=passwdVar,
        database=databaseVar,
        port =portVar,
        auth_plugin=auth_pluginVar)

        self.cursor = self.db.cursor()
    
    def findStudentNumber(self,studentNumber):
        """Returns results Select statement that looks for a student number in the student table

        :param studentNumber: [MKWZWA0003]
        :type studentNumber: [String]
        :return: [List of records obtained from the query]
        :rtype: [List]
        """
        query = "SELECT * FROM student WHERE student_no = '{}';".format(studentNumber)
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def markRegister(self,studentNumber,activity): 
        """[summary]

        :param studentNumber: [description]
        :type studentNumber: [type]
        :param activity: [description]
        :type activity: [type]
        """
        return ""
    
    def getDB(self):
        return self.cursor
    
    async def insertData(self,query):
        """Inserts data to the enrolls the database using the given qeury

        :param query: [query to be executed on the database]
        :type query: [String]
        """
        self.cursor.execute(query)
        self.db.commit()
    
    def getCurrentActivity(self):

        now = datetime.now() # The current time
        print(now)
        query = "SELECT * FROM lab_schedule WHERE start <= '{}' and end >= '{}'".format(now,now)
        
        self.cursor.execute(query)

        results = self.cursor.fetchall()
        return results
    
    def markAttendance(self,student_no):
        results = self.getCurrentActivity()
        for activity in results:
            schedule_id = activity[0]
            query = "UPDATE register SET status = '1' WHERE student_no = '{}' AND schedule_id = '{}';".format(student_no,schedule_id)
            print(query)
            self.cursor.execute(query) 
            self.db.commit()
    

# dbObj = database("eee4022sdatabase-do-user-9871310-0.b.db.ondigitalocean.com",
#     "admin",
#     "aGAPX1Hn5TdTE-4I",
#     "lab_system",
#     "25060",
#     "mysql_native_password"
#     )

# results = dbObj.findStudentNumber("MKWZA004")
# print(results)

# Creating curser
# cursor = db.cursor()
# cursor.execute("SHOW TABLES")

# for table_name in cursor:
#    print(table_name)