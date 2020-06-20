import boto3
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.update_item(
        TableName = 'visitorcount',
        Key={
            'siteUrl':{'S':"https://codeandtechresume.com/"}
        },
        UpdateExpression='SET visits = visits + :inc',
        ExpressionAttributeValues={
            ':inc': {'N': '1'}
        },
        ReturnValues="UPDATED_NEW",
    )
    response['Attributes']['visits']=int(response['Attributes']['visits']['N'])
    return { 
        "statusCode": 200,
        "headers": {'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        "body": json.dumps(response['Attributes']),
    }

