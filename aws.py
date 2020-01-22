import json
import boto3
import cv2
from util import NumpyEncoder, filterResponse

endpoint_name = "sagemaker-tensorflow-2020-01-21-01-40-19-479"


def invoke_model(image_path):

    image = cv2.imread(image_path)
    image = cv2.resize(image, (220, 220))
    image = image.reshape(-1, 220, 220, 3)

    client = boto3.Session().client('sagemaker-runtime')

    json_dump = json.dumps(image, cls=NumpyEncoder)

    response_payload = client.invoke_endpoint(
        EndpointName=endpoint_name, Body=json_dump)
    response_body = response_payload['Body'].read()

    formated_response = filterResponse(response_body)
    return formated_response['outputs']['score']['floatVal']
