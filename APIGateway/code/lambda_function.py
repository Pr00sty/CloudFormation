import json


def lambda_handler(event, context):
    if not event:
        return {
            "statusCode": 400,
            "body": json.dumps({
                    "Error": "Got empty body"
                })
            # "headers": {
            #     'Content-Type': 'application/json'
            # }
        }
    else:
        name = event.get("name")
        weight = event.get("weight")
        height = event.get("height")
        # insert to db
        return {
            "statusCode": 200,
            "body": "OK"
        }


if __name__ == '__main__':
    test_event = {"name": "John", "weight": 70, "height": 171}
    test_context = {}
    lambda_handler(test_event, test_context)
