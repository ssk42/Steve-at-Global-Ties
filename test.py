import requests
parameters = {"clone_objects":[{"source_id": 240, "source_type": "Course"}]}
###Admin
response= requests.get('https://globaltiessandbox.bridgeapp.com/api/learner/notifications', auth=('2e06e4c4-15f9-4aea-a056-34c101ccdeb3', 'c2df5ebf-36b1-45b2-85ea-dc3dce798ea4'))
###IT Admin
#response= requests.get('https://globaltiessandbox.bridgeapp.com/api/learner/notifications', auth=('118a7253-ffb0-42eb-b567-5c28bc1178f0', '77c92ed5-9120-483b-95e7-bc36b43b3685'))
###Author
#response= requests.get('https://globaltiessandbox.bridgeapp.com/api/author/notifications', auth=('1ec99ae5-4b5c-44a2-b11e-cd302005e9a1', 'd96af8fd-d57b-43ce-8a2b-fc60f5174520'))
###Learner
#response= requests.get('https://globaltiessandbox.bridgeapp.com/api/learner/notifications', auth=('c27c5d14-2200-4a5e-8805-37489e1a38ee', '7d002734-47b0-497c-abd0-313e555a15a8'))
###Account Admin
#response= requests.get('https://globaltiessandbox.bridgeapp.com/api/learner/notifications', auth=('81265ad8-e65b-46d7-ab8b-7f22d669953b', 'affe15bc-7042-4a09-8a80-f5aa64e4eae2'))

#print(response.json())
print(response.json())

# 9 people are currently in space.

