import json
import urllib.request
import os
import boto3
import logging
from botocore.exceptions import ClientError

url = 'https://drive.google.com/uc?id=1wFA6mOJJvX35h5aBr9EXiFmPTxw2xgX4&export=download'

# 1. download ##########################################################################

# download file
try:
    urllib.request.urlretrieve(url, "test-file.zip")
except Exception as e:
    print('Error: Download failed')

# check file downloaded
if not os.path.isfile('/tmp/test-file.zip'):
    print('Error: Download failed')

# 2. upload ############################################################################

s3_client = boto3.client('s3')

bucket = 'my-bucket'
file_name = 'test-file.zip'
object_name = 'myFolder' + '/' + 'test-file.zip'

try:
    response = s3_client.upload_file(file_name, bucket, object_name)
except Exception as e:
    print('Error: Upload failed')