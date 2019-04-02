import boto3
client = boto3.client('rekognition',region_name='us-east-1',aws_access_key_id='AKIAIJA2OES4WABDE6AA',aws_secret_access_key='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')
response = client.start_face_search(
    Video={
        'S3Object': {
            'Bucket': 'com.tutelage',
            'Name': 'attendance_video/sample3.mp4',
        }
    },
    ClientRequestToken='job2',
    FaceMatchThreshold=70,
    CollectionId='tutelate_attendance',
    NotificationChannel={
        'SNSTopicArn': 'arn:aws:sns:us-east-1:302190334691:tutelage_attendance',
        'RoleArn': 'arn:aws:iam::302190334691:role/tutelage_attendance'
    },
    JobTag='job2 '
)
print(response)
with open('responceid.txt', 'w') as id:
    id.writelines(response['JobId'])

