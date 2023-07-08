import boto3
import json

AWS_REGION = 'us-east-1'
ENDPOINT_URL = 'http://localhost:4566'

lambda_client = boto3.client("lambda", region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)

test_event = dict()

response = lambda_client.invoke(
  FunctionName='helloWorldLambda',
  Payload=json.dumps(test_event),
)

#print(response['Payload'])
print(response['Payload'].read().decode("utf-8"))