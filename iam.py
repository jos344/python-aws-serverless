import boto3
import json

AWS_REGION = 'us-east-1'
ENDPOINT_URL = 'http://localhost:4566'

iam = boto3.client("iam", region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)

role_policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

response = iam.create_role(
  RoleName='LambdaBasicExecution',
  AssumeRolePolicyDocument=json.dumps(role_policy),
)

print(response)