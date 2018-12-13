import requests, pprint, json, csv, sys, openpyxl
parameters = {
#"search": "secc",
#"Response": "ppep"
#"learner_id": "649",
#"course_template_id": "19"

}
    

completedProgramCounter=0
skippedCounter=0
for x in range(22,735):

    try:
        response= requests.get('https://globaltiesus.bridgeapp.com/api/admin/users/'+str(x)+'/summary', auth=('f5249139-be37-45f9-9035-11b3d0fd2a30', 'b6785070-04e5-4b19-b6db-2ab13133a411'), params= parameters)
        bridgeResponse= response.json()
        if bridgeResponse['summary'].get('completed_programs')!=0:
            if bridgeResponse['summary'].get('completed_courses')>10:
                completedProgramCounter=completedProgramCounter+1
                print(bridgeResponse)
        #print("Counting..."+str(x))
    except json.decoder.JSONDecodeError:
        skippedCounter=skippedCounter+1
        print("Skipping..."+str(x))
    
print("Total number completed is: "+str(completedProgramCounter))
print("Total number skipped is: "+str(skippedCounter))

