from datetime import datetime
import boto3

import subprocess


def put_s3_object():
    output_str = subprocess.run(
        f"aws s3 ls",
        capture_output=True,
        text=True,
    ).stdout
    print(output_str)

if __name__ == '__main__':
    put_s3_object()