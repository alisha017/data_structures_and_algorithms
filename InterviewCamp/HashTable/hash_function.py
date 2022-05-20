def hash_function(string: str) -> int:

    if string is None:
        return 0
    hash_sum: int = ord(string[0])
    x = 31
    for i in range(1, len(string)):
        hash_sum = hash_sum * x + ord(string[i])

    return hash_sum


if __name__ == '__main__':
    str1: str = "mehul"
    print(hash_function(str1))

