import boto3
client = boto3.client('s3')

response = client.list_objects(
    Bucket='newprojectboto3'
)

for content in response['Contents']:
    print(content['Key'])