import json


def milind(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function Milind is executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
