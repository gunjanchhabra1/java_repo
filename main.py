import json
import boto3

s3 = boto3.resource('s3')
# s3 = boto3.client('s3')
                #  aws_access_key_id='MY_AWS_KEY_ID',
                #  aws_secret_access_key='MY_AWS_SECRET_ACCESS_KEY'
                
bucket_name = 'demo-bucket-acs'
object_key = 'version.json'
json_object =  s3.Object(bucket_name,object_key)
metadata = {"image_version": "2.2.0"}
json_object.copy_from(CopySource={'Bucket': bucket_name, 'Key': object_key}, Metadata=metadata, MetadataDirective='REPLACE')
updated_metadata = json_object.metadata
print(updated_metadata)