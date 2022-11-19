import hashlib


def verify_results(data) -> bool:
    result, counter, data = data.split(":")
    hash = hashlib.sha256(f"{counter}:{data}".encode("utf-8")).hexdigest()
    print(hash)
    return hash == result


if __name__ == '__main__':
    print(verify_results("eeff8d8ec411547f50bb771df1f238c72c8cc276b45758e0766c23942b1dab49:1334862:717c9b8c63011c2432144f7a"))
