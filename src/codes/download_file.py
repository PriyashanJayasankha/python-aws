import urllib.request
import os
from io import BytesIO

import boto3
import urllib3

url = 'https://drive.google.com/uc?id=1wFA6mOJJvX35h5aBr9EXiFmPTxw2xgX4&export=download'

# Direct Download ###########################################################

try:
    urllib.request.urlretrieve(url, "test-file.zip")
except Exception as e:
    print('Error: Download failed')

print(os.path.isfile('/tmp/test-file.zip'))

# Download as Stream ########################################################

# from s3
bucket_name = 'my-s3-bucket'
object_key = 'test-file.zip'

s3_resource = boto3.resource('s3')
zip_obj = s3_resource.Object(bucket_name=bucket_name, key=object_key)

stream_s3 = BytesIO(zip_obj.get()["Body"].read())

# from any
http = urllib3.PoolManager()

response = http.request('GET', url, preload_content=False)

stream_any = BytesIO(response.read())
