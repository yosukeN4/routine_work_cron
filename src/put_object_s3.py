from datetime import datetime
import boto3

import subprocess


def put_s3_object():
    output_str = subprocess.call(
        f"aws s3 ls",
        capture_output=True,
        text=True,
    ).stdout
    print(output_str)
