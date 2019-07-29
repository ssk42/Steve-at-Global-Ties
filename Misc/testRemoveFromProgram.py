import requests, pprint, json, csv, sys, openpyxl
parameters = {
    #"search": "secc",
    #"Respon    se": "ppep"
   # "learner_id":"494",
    #'id': '127'
}

data={
'enrollments': [
                        {
                              'active': True,
                              'can_be_made_optional': False,
                              'can_be_removed': False,
                              'completed_at': None,
                              'course_template': '16',
                              'created_at': '2018-11-09T11:14:56.364-05:00',
                              'end_at': '2018-11-30T23:59:59.001-05:00',
                              'expires_at': None,
                              'id': '2933',
                              'user_id': '44',
                              'is_archived': False,
                              'is_permanently_failed': False,
                              'links': {'learner': {'id': '44', 'type': 'learners'}},
                              'progress': 0.2941,
                              'required': True,
                              'score': 0,
                              'state': 'active',
                              'updated_at': '2018-11-09T11:15:48.497-05:00'},
                 ]
    }

response= requests.patch('https://globaltiesus.bridgeapp.com/api/author/enrollments/16', auth=('f5249139-be37-45f9-9035-11b3d0fd2a30', 'b6785070-04e5-4b19-b6db-2ab13133a411'), data=data)
print(response.headers)
pprint.pprint((response.json()))
