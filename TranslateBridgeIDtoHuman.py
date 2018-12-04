import requests, pprint, json, csv, sys, openpyxl
parameters = {
    #"search": "secc",
    #"Response": "ppep"
    #"learner_id": "649",
    "course_template_id": "19"
}

response= requests.get('https://globaltiesus.bridgeapp.com/api/admin/users/2/', auth=('f5249139-be37-45f9-9035-11b3d0fd2a30', 'b6785070-04e5-4b19-b6db-2ab13133a411'), params= parameters)
print(response.headers)

wbTest=openpyxl.load_workbook('C:/Users/sreitz/Desktop/test.xlsx') #This is the thing that needs to be translated
wsTest=wbTest.active
toBeTranslated= wsTest['B'] #Particular userid column

wbUsers=openpyxl.load_workbook('C:/Users/sreitz/Desktop/wbusers.xlsx') #This contains the translations
wsUsers=wbUsers.active
toTranslate= wsUsers['A'] #This is the column with the userIds
translated=wsUsers['C'] #This is the column with the email ('C'), First Name('G'), or Last Name('H')
for x in range(len(toBeTranslated)): 
    tbtCell=toBeTranslated[x].value
    for y in range(len(toTranslate)):
        tTCell=toTranslate[y].value
        translatedCell=translated[y].value
        #print(str(tTCell)+' '+str(tbtCell))
        if tTCell==tbtCell:
            #print(str(tTCell)+' '+str(tbtCell))
##            tbtCell=translated[y].value
            toBeTranslated[x].value=translatedCell

wbUsers.save('C:/Users/sreitz/Desktop/wbusers.xlsx')
wbTest.save('C:/Users/sreitz/Desktop/test.xlsx')
