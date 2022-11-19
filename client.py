import hashlib
import os
import random
import time
import timeit

DIFFICULTY = 5
SECRET_MINIUMUM = 12000

"""
DATA-FORMAT:
result:counter_start:data
"""


def calculate_input(input: str) -> str:
    result, counter_start, data = input.split(":")
    hash_result = ""
    counter_start = int(counter_start)
    start = timeit.default_timer()
    while hash_result != result:
        hash_result = hashlib.sha256(f"{counter_start}:{data}".encode("utf-8")).hexdigest()
        counter_start += 1
    end = timeit.default_timer()
    print(counter_start, f"{end-start}")
    return f"{result}:{counter_start-1}:{data}"


if __name__ == '__main__':
    print(calculate_input("78916a39f3fb9950befce6efb5dce63d80be5036361c95fea6697a19617a8f0e:42965:a922618641d6bcc3a7d02a39"))
