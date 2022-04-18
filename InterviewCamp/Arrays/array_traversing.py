"""
Given an array of numbers, replace each even number with two of the same number. e.g, [1,2,5,6,8] -> [1,2,2,5,6,6,8,8].
Assume that the array has enough space to accommodate the result.
"""

from typing import Optional, List


def my_solution(array: list = None) -> Optional[list]:
    """
    Time complexity - O(nlogn)
    Space complexity - O(n)
    :param array: list
    :return: list
    """
    result_array: list = array + [num for num in array if num % 2 == 0]
    result_array.sort()
    return result_array


def better_solution(array: list = None) -> Optional[list]:
    """
    Time complexity - O(n)
    Space complexity - O(n)
    :type array: list
    """
    if array is None or len(array) == 0:
        return array

    result_array = []
    for i in range(len(array)):
        result_array.append(array[i])
        if array[i] % 2 == 0:
            result_array.append(array[i])
    return result_array


def expand_array_for_even_numbers(array: List[int]) -> List[int]:
    """
    :rtype: List[int]
    :type array: list[int]
    """
    for num in array:
        if num % 2 == 0:
            array.append(-1)
    return array


def best_solution(array: List[int] = None) -> Optional[List[int]]:
    """
    Time complexity : O(n)
    Space complexity : O(1)
    :type array: List[int]
    """
    if array is None or len(array) == 0:
        return array

    iterator: int = len(array)-1
    array = expand_array_for_even_numbers(array)
    end: int = len(array)

    while iterator >= 0:
        if array[iterator] % 2 == 0:
            end -= 1
            array[end] = array[iterator]
            end -= 1
            array[end] = array[iterator]
        else:
            end -= 1
            array[end] = array[iterator]

        iterator -= 1

    return array


def reverse_sentence(string: str) -> str:
    """

    :type string: str
    """
    string_list: List[str] = string.split(" ")
    string_list.reverse()
    return " ".join(string_list)


if __name__ == '__main__':
    num_array: list = [1, 2, 5, 6, 8]

    print(my_solution(num_array))

    print(better_solution(num_array))

    print(best_solution(num_array))

    string: str = "i live in a house"
    print(reverse_sentence(string))





