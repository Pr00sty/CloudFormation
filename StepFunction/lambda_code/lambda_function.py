from time import sleep
from typing import Optional, Dict


def lambda_handler(
    event: Optional[Dict] = None, context: Optional[Dict] = None
) -> None:
    print(f"Got event: {event}")
    print(f"Got context: {context}")
    print("Wait 2 sec and go forward")
    sleep(2)
    print("Time is done.")
