import requests, pprint, json, csv, sys, openpyxl
import pandas as pd
parameters = {

    'distribution':{
		"title":"Python Test",

		"closes_at":"2019-06-02T05:59:00.000Z",

		"recipient_groups":[{"group_id":"58"}]
		},
    'survey_id':'9'
}

bridgeAPIurl= 'https://globaltiesus.bridgeapp.com/api'
bridgeAcctAdminKey= 'f5249139-be37-45f9-9035-11b3d0fd2a30'
bridgeAcctAdminSecret= 'b6785070-04e5-4b19-b6db-2ab13133a411'

bridgeSbAPIurl= 'https://globaltiessandbox.bridgeapp.com/api'
bridgeSbAdminKey= '81265ad8-e65b-46d7-ab8b-7f22d669953b' 
bridgeSbAdminSecret= 'affe15bc-7042-4a09-8a80-f5aa64e4eae2'

fall2018PPEPSections={5,6,7,8,9,10,11,12,13}

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
# bridgeResponse= requests.get(bridgeAPIurl+'/author/course_templates?includes[]sort=archived&archived=1&limit=2000',auth=(bridgeAcctAdminKey,bridgeAcctAdminSecret), params=parameters)

#print(response.headers)

#for program in fall2018PPEPSections:

extraParams='?with_deleted=true&includes[]=programsgi'
# bridgePost= requests.post(bridgeAPIurl+'/author/surveys/1/distributions',auth=(bridgeAcctAdminKey,bridgeAcctAdminSecret), params=parameters)
# bridgeSbPost= requests.post(bridgeSbAPIurl+'/author/surveys/9/distributions',auth=(bridgeSbAdminKey,bridgeSbAdminSecret), params=parameters)
# bridgeGet=requests.get(bridgeAPIurl+'/author/users/2/notifications',auth=(bridgeAcctAdminKey,bridgeAcctAdminSecret), params=parameters)
grantsGet=requests.get('https://www.globaltiesus.org')
# bridgeResponse=pd.DataFrame(bridgeResponse.json())
# bridgeResponse.to_csv('F:/Steve/notificationsForSupport.csv')

print(grantsGet)
# print(bridgeGet.json())
# dataFrames=pd.DataFrame([])
# def formADataFrame(xyz):
# 	bridgeResponse= requests.get(bridgeAPIurl+'/author/users/'+str(xyz)+'/notifications',auth=(bridgeAcctAdminKey,bridgeAcctAdminSecret), params=parameters)
# 	notifications=pd.DataFrame(bridgeResponse.json()['notifications'])
# 	return notifications

# for xyz in range(2,740):
# 	test=formADataFrame(xyz)
# 	if xyz!=2:
# 		dataFrames=pd.concat([dataFrames,test])
# 		print('processing'+str(xyz))
# 	if xyz==736:
# 		dataFrames.to_csv('F:/Steve/notificationsAll.csv')
# 		print('Saved at '+str(xyz))
# courseTemplates=pd.DataFrame(bridgeResponse.json()['notifications'])
# courseTemplates2=pd.DataFrame(bridgeResponse2.json()['notifications'])
#courseTemplates=pd.concat([courseTemplates,courseTemplates2])
# courseTemplates.to_csv('F:/Steve/notifications2.csv', encoding='latin1')


##This turns Bridge IDs into Emails. Can also be changed to First Names or Last Names.
##
##DEPRICATED: PLEASE SEE TRANSLATE BRIDGE ID TO HUMAN.py
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
##response= requests.get('https://globaltiesus.bridgeapp.com/api/admin/users/22/summary', auth=('f5249139-be37-45f9-9035-11b3d0fd2a30', 'b6785070-04e5-4b19-b6db-2ab13133a411'), params= parameters)
##bridgeResponse= response.json()
##print(bridgeResponse)
##    
##
##completedProgramCounter=0
##skippedCounter=0
##for x in range(22,735):
##    parameters= {
##        "id": x
##        }
##    try:
##        response= requests.get('https://globaltiesus.bridgeapp.com/api/admin/users/'+str(x)+'/summary', auth=('f5249139-be37-45f9-9035-11b3d0fd2a30', 'b6785070-04e5-4b19-b6db-2ab13133a411'), params= parameters)
##        bridgeResponse= response.json()
##        if bridgeResponse['summary'].get('completed_programs')!=0 &bridgeResponse['summary'].get('total_overdue')==0 :
##            completedProgramCounter=completedProgramCounter+1
##        print("Counting..."+str(x))
##    except json.decoder.JSONDecodeError:
##        skippedCounter=skippedCounter+1
##        print("Skipping..."+str(x))
##    
##print("Total number completed is: "+str(completedProgramCounter))
##print("Total number skipped is: "+str(skippedCounter))
##



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






