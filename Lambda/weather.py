import json
import boto3
from datetime import datetime
s3 = boto3.client('s3')

BUCKET_NAME = 'weather-lamb-project1'

print(event)

    for record in event['Records']:

        new_image = record['dynamodb'].get('NewImage', {})

        data = {}

        for key, value in new_image.items():
            data[key] = list(value.values())[0]