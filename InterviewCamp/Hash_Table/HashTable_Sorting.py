"""
Given an array of integers, find a pair of integers that sums to a number X.

For e.g, if A = [6,3,5,2,1,7]. X = 4, Result= [3,1]
"""


def get_pair(array: list, result: int) -> list:
    array.sort()
    num_dict: dict = {num: array.count(num) for num in array}
    result_array: list = []
    for num, count in num_dict.items():
        if result-num in num_dict:
            result_array.extend([num, result-num])
            break
    return result_array


if __name__ == '__main__':
    A: list = [6, 3, 5, 2, 1, 7]
    x: int = 4

    print(get_pair(A, x))

