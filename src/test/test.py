import zipfile
from io import BytesIO
import boto3
import urllib3

url = 'https://drive.google.com/uc?id=xx1wFA6mOJJvX35h5aBr9EXiFmPTxw2xgX4&export=download'
bucket = 'priyashan-storage-bucket'
key = 'test-file.zip'

s3_resource = boto3.resource('s3')
http = urllib3.PoolManager()
# s3.upload_fileobj(http.request('GET', url, preload_content=False), bucket, key)
response = http.request('GET', url, preload_content=False)
buffer = BytesIO(response.read())

try:
    z = zipfile.ZipFile(buffer)
except Exception as e:
    print('Error: Retrieve object failed..')


# Upload
try:
    for filename in z.namelist():
        file_info = z.getinfo(filename)

        s3_resource.meta.client.upload_fileobj(
            z.open(filename),
            Bucket='priyashan-storage-bucket',
            Key=filename
        )
except Exception as e:
    print('Error: Upload failed')

