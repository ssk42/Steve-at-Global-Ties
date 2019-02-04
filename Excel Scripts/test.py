import requests, pprint, json, csv, sys, openpyxl
parameters = {
    'program_id': 5
}

bridgeAPIurl= 'https://globaltiesus.bridgeapp.com/api'
bridgeAcctAdminKey= 'f5249139-be37-45f9-9035-11b3d0fd2a30'
bridgeAcctAdminSecret= 'b6785070-04e5-4b19-b6db-2ab13133a411'

fall2018PPEPSections={5,6,7,8,9,10,11,12,13}

bridgeResponse= requests.get(bridgeAPIurl+'/author/course_templates/116/slides',auth=(bridgeAcctAdminKey,bridgeAcctAdminSecret), params=parameters)
print(bridgeResponse.json)