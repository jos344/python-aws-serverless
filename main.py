import json
import boto3

iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda')

AWS_REGION = 'us-east-1'
ENDPOINT_URL = 'http://localhost:4566'

lambda_client = boto3.client("lambda", region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)
iam_client = boto3.client("iam", region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)

# upload code and create lambda function
# upload your deployment package

with open('lambda.zip', 'rb') as f:
	zipped_code = f.read()
  
role = iam_client.get_role(RoleName='LambdaBasicExecution')

response = lambda_client.create_function(
    FunctionName='helloWorldLambda',
    Runtime='python3.9',
    Role=role['Role']['Arn'],
    Handler='handler.lambda_handler',
    Code=dict(ZipFile=zipped_code),
    Timeout=300, # Maximum allowable timeout
)

print(response)