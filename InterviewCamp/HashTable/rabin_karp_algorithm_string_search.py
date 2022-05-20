from typing import Any


def hash_function(string: str, hash_val: int) -> int:
    if string is None:
        return 0
    hash_sum: int = ord(string[0])
    x = hash_val
    for i in range(1, len(string)):
        hash_sum = hash_sum * x + ord(string[i])
    return hash_sum


def rabin_karp_string_search(string, to_search):
    if string is None or to_search is None:
        raise Exception("Null pointer exception")

    if to_search == "":
        return 0

    window_size: int = len(to_search)
    hash_val = 31
    hash_sum = 0
    result_hash_sum = hash_function(to_search, hash_val)

    for i in range(0, len(string)-window_size+1):
        print(f"string[i:window_size]: {string[i:i + window_size]}")
        # print(f"string[i + window_size]: {string[i + window_size]}")

        if i != 0:
            hash_sum = (hash_sum - ord(string[i-1])*(hash_val**(window_size-1))) * hash_val \
                       + ord(string[i + window_size - 1])
            # print(f"string[i-1]: {string[i - 1]}\n{hash_sum - ord(string[i - 1]) ** (window_size - 1)}")
        else:
            hash_sum = hash_function(string[i:i+window_size], hash_val)

        # print(f"hash_sum: {hash_sum}, result_wanted: {result_hash_sum}\n")

        if hash_sum == result_hash_sum and to_search == string[i:i+window_size]:
            return i

    return -1


if __name__ == '__main__':
    # str1: str = "mehul"
    # print(f"{str1}: {hash_function(str1, 31)}")

    print(rabin_karp_string_search("abcdefghij", "efg"))
    print(rabin_karp_string_search("mehulandalisha", ""))
    print(rabin_karp_string_search("mehulandalisha", "alisha"))
    print(rabin_karp_string_search("mehulandalisha", "hula"))
    print(rabin_karp_string_search("mehulandalisha", "andali"))

