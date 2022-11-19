import hashlib
import os
import random

DIFFICULTY = 5
SECRET_MINIUMUM = 12000

"""
DATA-FORMAT:
result:counter_start:data
"""


def generate_data():
    data = os.urandom(12).hex()
    correct_counter = random.randint(SECRET_MINIUMUM, SECRET_MINIUMUM + DIFFICULTY * 1000000)
    # correct_counter = SECRET_MINIUMUM+DIFFICULTY*1000000
    data_to_hash = f"{correct_counter}:{data}"
    m = hashlib.sha256()
    m.update(data_to_hash.encode("utf-8"))
    hash_res = m.hexdigest()
    counter_start = DIFFICULTY * random.randint(0, SECRET_MINIUMUM)
    print(f"{hash_res}:{counter_start}:{data}")
    print(correct_counter)
    print(f"estimated time: {(correct_counter-counter_start)/10000*0.0066460387515691775}")
    return f"{hash_res}:{counter_start}:{data}"


if __name__ == '__main__':
    generate_data()
