import io
import json
import zipfile

import boto3
from botocore.exceptions import ClientError

lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')


def get_role_arn(role_name):
    try:
        # Get the role details
        response = iam_client.get_role(RoleName=role_name)

        # Extract and return the ARN
        return response['Role']['Arn']

    except ClientError as e:
        print(f"Error retrieving role ARN: {e}")
        return None


def create_lambda_function(function_name, runtime, role_arn, handler, code_string):
    try:
        # Create a ZIP file in memory
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            zip_file.writestr('lambda_function.py', code_string)
        zip_buffer.seek(0)

        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime=runtime,
            Role=role_arn,
            Handler=handler,
            Code={
                'ZipFile': zip_buffer.read()
            },
            Publish=True
        )
        return response
    except ClientError as e:
        return {"error": str(e)}


def list_lambda_functions():
    try:
        response = lambda_client.list_functions()
        return response.get('Functions', [])
    except ClientError as e:
        return {"error": str(e)}


def delete_lambda_function(function_name):
    try:
        lambda_client.delete_function(FunctionName=function_name)
        return {"status": "Function deleted successfully"}
    except ClientError as e:
        return {"error": str(e)}


def invoke_lambda_function(function_name, payload):
    try:
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )
        response_payload = json.loads(response['Payload'].read())
        return response_payload
    except ClientError as e:
        return {"error": str(e)}
