import requests, pprint, json, csv, sys, openpyxl
parameters = {
    #"search": "secc",
    #"Response": "ppep"
    #"learner_id": "649",
    "course_template_id": "19"
}


###Admin
#response= requests.post('https://globaltiessandbox.bridgeapp.com/api/author/custom_fields', params=parameters, auth=('2e06e4c4-15f9-4aea-a056-34c101ccdeb3', 'c2df5ebf-36b1-45b2-85ea-dc3dce798ea4'))
###IT Admin
#response= requests.get('https://globaltiessandbox.bridgeapp.com/api/learner/notifications', auth=('118a7253-ffb0-42eb-b567-5c28bc1178f0', '77c92ed5-9120-483b-95e7-bc36b43b3685'))
###Author
#response= requests.post('https://globaltiessandbox.bridgeapp.com/api/learner/notifications', auth=('1ec99ae5-4b5c-44a2-b11e-cd302005e9a1', 'd96af8fd-d57b-43ce-8a2b-fc60f5174520'))
###Learner
#response= requests.get('https://globaltiessandbox.bridgeapp.com/api/learner/notifications', auth=('c27c5d14-2200-4a5e-8805-37489e1a38ee', '7d002734-47b0-497c-abd0-313e555a15a8', params= parameters))
###Account Admin
#response= requests.get('https://globaltiessandbox.bridgeapp.com/api/author/tasks', auth=('81265ad8-e65b-46d7-ab8b-7f22d669953b', 'affe15bc-7042-4a09-8a80-f5aa64e4eae2'), params= parameters)
###Account Admin in Prod
#response= requests.post('https://globaltiesus.bridgeapp.com/api/admin/data_dumps', auth=('f5249139-be37-45f9-9035-11b3d0fd2a30', 'b6785070-04e5-4b19-b6db-2ab13133a411'), params= parameters)
##response= requests.get('https://globaltiesus.bridgeapp.com/api/admin/data_dumps/download', auth=('f5249139-be37-45f9-9035-11b3d0fd2a30', 'b6785070-04e5-4b19-b6db-2ab13133a411'), params= parameters)
##print(response.headers)
#print(response.headers)


##This turns Bridge IDs into Emails. Can also be changed to First Names or Last Names.
##
##
##wbTest=openpyxl.load_workbook('C:/Users/sreitz/Desktop/test.xlsx') #This is the thing that needs to be translated
##wsTest=wbTest.active
##toBeTranslated= wsTest['B'] #Particular userid column
##
##wbUsers=openpyxl.load_workbook('C:/Users/sreitz/Desktop/wbusers.xlsx') #This contains the translations
##wsUsers=wbUsers.active
##toTranslate= wsUsers['A'] #This is the column with the userIds
##translated=wsUsers['C'] #This is the column with the email ('C'), First Name('G'), or Last Name('H')
##for x in range(len(toBeTranslated)): 
##    tbtCell=toBeTranslated[x].value
##    for y in range(len(toTranslate)):
##        tTCell=toTranslate[y].value
##        translatedCell=translated[y].value
##        if tTCell==tbtCell:
##            toBeTranslated[x].value=translatedCell
##wbUsers.save('C:/Users/sreitz/Desktop/wbusers.xlsx')
##wbTest.save('C:/Users/sreitz/Desktop/test.xlsx')
##


#This counts users who have completed programs
#
#
#
completedProgramCounter=0
for x in range(22,735):
    response= requests.get('https://globaltiesus.bridgeapp.com/api/admin/users/'+str(x)+'/summary', auth=('f5249139-be37-45f9-9035-11b3d0fd2a30', 'b6785070-04e5-4b19-b6db-2ab13133a411'), params= parameters)
    bridgeResponse= response.json()
    #if bridgeResponse['summary'].get('completed_programs')!=0 or None:
    completedProgramCounter=completedProgramCounter+1
    print("Counting..."+str(x))
print(completedProgramCounter)


#This doe
#
##checkpoints_parsed= response.json()
##chkpts_data=checkpoints_parsed['reports']
##chkpts_data=open('test.csv','r+')
##csvwriter= csv.writer(chkpts_data)
##count=0
##for chkpt in chkpts_data:
##    if count==0:
##        header=chkpt.keys()
##        csvwriter.writerow(header)
##        count+=1
##    csvwriter.writerow(chkpt.values())
##
##chkpts_data.close()
##with open('data.txt', 'w') as f:
##  json.dump((response.json()), f, ensure_ascii=False,indent=4, sort_keys=True)
##






