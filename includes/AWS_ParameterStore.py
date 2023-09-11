# Library and functions to interact with the Pushover API

import boto3
from botocore.exceptions import ClientError

def get_ssm_parameter(name: str, decryption: str = True) -> str:
    """
    Get parameter from AWS Systems Manager SSM Parameter Store.
    """
    ssm = boto3.client('ssm')
    try:
        parameter = ssm.get_parameter(Name=name,WithDecryption=decryption)['Parameter']['Value']
        return parameter
    except ClientError as e:
        print(e.response['Error']['Code'])
        return False


