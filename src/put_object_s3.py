from datetime import datetime
import boto3

import subprocess

def put_s3_object():
    subprocess.call(f'aws s3 ls')