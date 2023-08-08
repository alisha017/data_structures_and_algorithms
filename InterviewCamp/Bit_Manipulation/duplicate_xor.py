"""
tgrtetyr
"""
from typing import List


def find_missing_num(num_array:List[int], n:int):
    if not num_array:
        return None
    n_xor = 0
    for i in range(1, n+1):
        n_xor ^= i

    for num in num_array:
        n_xor ^= num

    return n_xor

"""
a list contains all numbers twice except one, find the unique num
"""
def find_non_duplicate_number(num_array:List[int]):
    result = 0

    for num in num_array:
        result ^= num

    return result

if __name__ == "__main__":
    print(find_missing_num([1,3,5,4,6], 6))
    print(find_non_duplicate_number([2,2,3,4,3,5,6,5,6]))