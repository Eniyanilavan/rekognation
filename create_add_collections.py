import os
import boto3
client = boto3.client('rekognition',region_name='us-east-1',aws_access_key_id='AKIAIJA2OES4WABDE6AA',aws_secret_access_key='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')
responce = client.create_collection(CollectionId='tutelate_attendance')

files = os.listdir('images')
for i in files:
        with open('images/'+i,'rb') as fp:
            byte = fp.read()
            response = client.index_faces(
                CollectionId='tutelate_attendance',
                Image={
                    'Bytes': byte,
                },
                ExternalImageId=i.split('.')[0].replace(" ","_"),
                DetectionAttributes=[
                    'DEFAULT',
                ]
            )
            print(response)