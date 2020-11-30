import json
import zipfile
from io import BytesIO
import boto3
import urllib3

url = 'https://drive.google.com/uc?id=1wFA6mOJJvX35h5aBr9EXiFmPTxw2xgX4&export=download'

# 1. Retrieve the file from Lei ##########################################################

http = urllib3.PoolManager()
response = http.request('GET', url, preload_content=False)

buffer = BytesIO(response.read())

try:
    zip = zipfile.ZipFile(buffer)
except Exception as e:
    zip = None
    print('Error: Object retrieve failed..')

# 2. Upload to S3 ######################################################################

s3_resource = boto3.resource('s3')

try:
    for filename in zip.namelist():
        s3_resource.meta.client.upload_fileobj(
            zip.open(filename),
            Bucket='my-bucket',
            Key='my-folder' + '/' + filename
        )
except Exception as e:
    print('Error: Upload failed..')
