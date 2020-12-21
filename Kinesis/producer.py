import json
import time
from typing import Any, Dict, List

import boto3
import random

STREAM_NAME = 'MyKinesisStream'


def produce_records(num_of_records: int) -> List[Dict[str, Any]]:
    records = []
    for lamp_id in range(0, num_of_records):
        data_point = {
            "lamp_id": f"lamp_{lamp_id + 1}",
            "lightness": random.random()
        }
        records.append(
            {
                'Data': json.dumps(data_point),
                'PartitionKey': 'partition_key'}
        )
    return records


def insert_records(
        records: List[Dict[str, Any]],
        kinesis_client: boto3.client = boto3.client('kinesis')
) -> None:
    response = kinesis_client.put_records(StreamName=STREAM_NAME, Records=records)
    print(f"response: {response}")
    print(f"inserted: {records}")


def main():
    x = boto3.session.Session(profile_name='cap')
    kinesis = x.client('kinesis')
    while True:
        records = produce_records(num_of_records=3)
        insert_records(records, kinesis_client=kinesis)
        time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
