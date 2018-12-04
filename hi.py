import os, openpyxl
wbMaster= openpyxl.load_workbook('test.xlsx')
sheet= wbMaster.get_sheet_by_name('Complete')
wbCompletion= openpyxl.load_workbook('test2.xlsx')
sheet2= wbCompletion.get_sheet_by_name('Complete')
wbNLI=openpyxl.load_workbook('test3.xlsx')
sheet3= wbNLI.get_sheet_by_name('Students-Never-Logged-into-Blue')
userNLI={}
emailCheck={}
for row in range(1, 427):
        user= sheet3['D'+str(row)].value
        userNLI.setdefault(user,{})
        email= sheet2['C'+str(row)].value
        emailCheck.setdefault(email,{})
for rowNum in range(1,427):
    allUser= sheet['E'+str(rowNum)].value
    allEmails= sheet['D'+str(rowNum)].value
    if allUser in userNLI:
        sheet.cell(row=rowNum, column=7).value= 'No'
    else:
        sheet.cell(row=rowNum, column=7).value= 'Sí'
    if allEmails in emailCheck:
        sheet.cell(row=rowNum, column=8).value= 'Complete'
wbMaster.save('updated.xlsx')
