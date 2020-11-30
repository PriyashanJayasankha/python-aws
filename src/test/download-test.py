import os
import urllib.request


# download
from botocore.exceptions import ClientError

url_1 = 'https://drive.google.com/uc?id=1wFA6mOJJvX35h5aBr9EXiFmPTxw2xgX4&export=download'
url_2 = 'https://leidata.gleif.org/api/v1/concatenated-files/repex/20201129/zip'
urllib.request.urlretrieve(url_2, "test-file.zip")

print(os.path.isfile('test-file.zip'), " - file_downloaded")

