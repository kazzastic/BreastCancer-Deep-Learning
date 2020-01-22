import json
import boto3
import numpy as np
import io
import cv2

endpoint_name = "sagemaker-tensorflow-2020-01-21-01-40-19-479"


def in


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


image = cv2.imread('cancer.jpg')
image = cv2.resize(image, (220, 220))
image = image.reshape(-1, 220, 220, 3)


client = boto3.Session().client('sagemaker-runtime')

json_dump = json.dumps(image, cls=NumpyEncoder)
# The sample model expects an input of shape [1,50]
#data = np.random.randn(1, 50).tolist()
response = client.invoke_endpoint(EndpointName=endpoint_name, Body=json_dump)
response = response['Body'].read()


# my_bytes_value = b'[{\'Date\': \'2016-05-21T21:35:40Z\', \'CreationDate\': \'2012-05-05\', \'LogoType\': \'png\', \'Ref\': 164611595, \'Classe\': [\'Email addresses\', \'Passwords\'],\'Link\':\'http://some_link.com\'}]'

# Decode UTF-8 bytes to Unicode, and convert single quotes
# to double quotes to make it valid JSON
my_json = response.decode('utf8').replace("'", '"')
# print(my_json)


# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)
s = json.dumps(data, indent=4, sort_keys=True)
print(json.loads(s))
