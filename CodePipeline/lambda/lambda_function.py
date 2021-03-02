def lambda_handler(event, context):
    print(f"event: {event}")
    print(f"event: {context}")
    return {"event": event, "context": context}


if __name__ == '__main__':
    event = {"key1": "xxx", "key2": "yyy"}
    context = {}
    lambda_handler(event, context)
