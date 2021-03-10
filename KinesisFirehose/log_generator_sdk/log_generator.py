import logging
import random
import string
import time
import boto3
from botocore.exceptions import ClientError

firehose_client = boto3.client('firehose')

my_logger = logging.getLogger(__name__)
FORMAT = '%(asctime)-15s - %(message)s'
logging.basicConfig(format=FORMAT)
logging.Logger.setLevel(my_logger, level=logging.INFO)

list_of_chars = list(string.ascii_lowercase)

for i in range(0, 100):
    log_time = time.strftime("%Y%m%d-%H%M%S")
    record = f"{log_time} - {random.choice(list_of_chars)} - XXX\n"

    try:
        response = firehose_client.put_record(
            DeliveryStreamName='MyLogStream',
            Record={
                'Data': record.encode()
            }
        )
        my_logger.info(f"Inserted record: {record}")
    except ClientError as e:
        my_logger.error(f"Got exception: {e}")
    time.sleep(1)
