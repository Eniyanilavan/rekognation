import json
import datetime
import requests
present = []
collegeid='pu1030'
with open('prediction.json','r') as fp:
    responce = fp.readline()
    responce = json.loads(responce)
    if responce['JobStatus'] == 'SUCCEEDED':
        for person in responce['Persons']:
            if "FaceMatches" in person:
                if len(person["FaceMatches"]) != 0:
                    if person['FaceMatches'][0]['Face']['ExternalImageId'] not in present:
                        present.append(person['FaceMatches'][0]['Face']['ExternalImageId'])
print(present)
res = requests.post('http://localhost:3002/tutelage/attendance',{'collid':collegeid,'date':str(datetime.datetime.now().date()),'attendance':present})
print(res)
with open('server','r+') as fp1:
    data = fp1.read()
    data = json.loads(data)
    # print(datetime.datetime.now().date())
    data['collid']=collegeid
    data['attendance'][str(datetime.datetime.now().date())]=present
    fp1.seek(0)
    data = json.dumps(data)
    fp1.write(data)