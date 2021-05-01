import boto3
import json

s3 = boto3.client("s3")

def lambda_handler (event,context):
    bucket = "terraform-bucket-nithin"
    key = "script/f"
    
    try:
        data = s3.get_object(Bucket=bucket, Key=key)
        json_data = data ["Body"].read()

        return{
            "response_code" : 200,
            "data": str(json_data)
        }
    except Exception as e:
        print (e)