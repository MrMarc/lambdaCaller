import json
import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-1',
)

lambda_client = boto3.client('lambda',config=my_config)

try:
    response = lambda_client.invoke(FunctionName='RemoteCallExampleFunction',
                     InvocationType='RequestResponse',
                     LogType='None',
                     )

    response_payload = json.loads(response['Payload'].read().decode("utf-8"))

    print ("Response Payload: {}".format(response_payload))

except:
    print("Exception")