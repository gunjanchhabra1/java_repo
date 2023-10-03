import json
import boto3

s3 = boto3.resource('s3')

json_object =  s3.Object('demo-bucket-acs', 'version.json')
json_object["image_version"] = "2.2.0"
print(json_object)