import json
import boto3

# s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')
bucket_name = 'demo-bucket-acs'
object_key = 'version.json'
update_key = "image_version"
new_value = "5.5.1"
response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
json_data = json.loads(response['Body'].read())
json_data[update_key] = new_value
s3_client.put_object(
    Bucket=bucket_name,
    Key=object_key,
    Body=json.dumps(json_data)
)
print(json.dumps(json_data, indent=4))
