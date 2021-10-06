# print(sheet.cell_value(0,0))
import openpyxl
from openpyxl import load_workbook
from pathlib import Path
import asyncio
from db import database

class excel_input():

    def __init__(self):
        pass
        # self.wb = load_workbook(fileName)
        # self.sheet = wb.active

    # wb_obj = load_workbook('course_students.xlsx')
    # sheet = wb_obj.active
    # Cell row 
    # cell_obj = sheet.cell(row=1,column=1)

    async def getStudents(self,sheet):
        counter = 0 # Counter
        max_rows = sheet.max_row
        check = True

        for i in range(2,max_rows+1):
            cell_obj = sheet.cell(row=i,column=2)
            student_no = cell_obj.value

            if (check):
                courseCode = sheet.cell(row=i,column=1).value
                check = False

            if student_no != None:
                await self.postToEnrolls(student_no,courseCode)
                counter += 1
            elif student_no == None:
                check = True

    async def postToDB(self):
        await print("post to DB")

    def getCourse(self,sheet):
        max_rows = sheet.max_row
        for i in range(2,max_rows+1):
            cell_obj = sheet.cell(row=i,column=1)
            student_no = cell_obj.value
            print(student_no)

    async def createEnrollsID(self,student_id,code):
        return student_id+code
        # Gets the course names from the first column

    async def postToEnrolls(self,student_no,code):
        enrollsID = await self.createEnrollsID(student_no,code)
        query = "INSERT INTO enrolls(enrolls_id,student_no,code) VALUES('{}','{}','{}')".format(enrollsID,student_no,code)
        print(query)

# Initialisations
wb_obj = load_workbook('course_students.xlsx')
sheet = wb_obj.active
exObj = excel_input()

loop = asyncio.get_event_loop()
loop.run_until_complete(exObj.getStudents(sheet))

# print(cell_obj.value)
# print(sheet.max_row)
# print(sheet.max_column)


# getCourse(sheet)