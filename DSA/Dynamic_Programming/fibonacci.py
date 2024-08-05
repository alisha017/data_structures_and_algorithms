from typing import Dict


def get_fibonacci_using_memoization(num: int, fibo_dict: Dict[int, int]):
    """
    Recursion + memoization
    Top-down approach
    time complexity :
    Space complexity: O(n)
    :param num: int -- the number whose fibonacci is to be found out
    :param fibo_dict: dictionary - key: num, value: fibonacci
    :return: fibonacci of the num
    """
    if num == 0 or num == 1:
        return 1
    if num in fibo_dict:
        return fibo_dict[num]

    result = get_fibonacci_using_memoization(num - 1, fibo_dict) + get_fibonacci_using_memoization(num - 2, fibo_dict)
    fibo_dict[num] = result

    # print(fibo_dict)
    return result


def get_fibonacci_using_tabulation(num: int):
    """
    Dynamic programming through tabulation, saving only last 2 values at a time.
    Bottom-Up approach
    Time complexity: O(n)
    Space complexity: O(1)
    :type num: int, num whose fibonacci number is to be found out
    :return fibonacci number of num
    """
    if num < 0:
        return None

    minus_1: int = 1
    minus_2: int = 1
    nth = 1

    for i in range(2, num + 1):
        # print(f"i:{i} --> nth:{nth}, minus1:{minus_1}, minus2:{minus_2}")
        nth = minus_1 + minus_2
        minus_2 = minus_1
        minus_1 = nth
    return nth


if __name__ == "__main__":
    print(get_fibonacci_using_memoization(13, {}))
    print(get_fibonacci_using_tabulation(13))
