import json
import boto3

s3 = boto3.resource('s3')
# s3 = boto3.client('s3')
                #  aws_access_key_id='MY_AWS_KEY_ID',
                #  aws_secret_access_key='MY_AWS_SECRET_ACCESS_KEY'
                
json_object =  s3.Object('demo-bucket-acs', 'version.json')
json_object["image_version"] = "2.2.0"
print(json_object)