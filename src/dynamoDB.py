import boto3

dynamodb_client = boto3.client('dynamodb')

response = dynamodb_client.get_item(
    TableName='users',
    Key={
        'id': {'S': 'aa'}
    }
)

print(response['Item'])
