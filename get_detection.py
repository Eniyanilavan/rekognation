import boto3
import json
client = boto3.client('rekognition',region_name='us-east-1',aws_access_key_id='AKIAIJA2OES4WABDE6AA',aws_secret_access_key='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')
with open('responceid.txt','r') as fp:
    jobid = fp.readline()
    response = client.get_face_search(
        JobId=jobid,
        SortBy='INDEX'
    )
    result = json.dumps(response)
    with open('prediction.json','w') as fp:
        fp.writelines(result)
    print(response)