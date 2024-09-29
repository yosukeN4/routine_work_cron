from datetime import datetime
import boto3

import subprocess

def show_s3_ls_object():
    output_str = subprocess.run(
        'aws s3 ls',
        capture_output=True,
        text=True,
    ).stdout
    print(output_str)

if __name__ == '__main__':
    show_s3_ls_object()