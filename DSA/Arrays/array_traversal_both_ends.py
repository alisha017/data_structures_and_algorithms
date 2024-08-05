from typing import Optional, List


# Level: Medium
# Given an array of integers, find the shortest sub array, that if sorted, results in the entire array being sorted.
#
# For example:[1,2,4,5,3,5,6,7] --> [4,5,3] - If you sort from indices 2 to 4, the entire array is sorted.
# [1,3,5,2,6,4,7,8,9] --> [3,5,2,6,4] -  If you sort from indices 1 to 5, the entire array is sorted.
# For example: A = [0,2,3,1,8,6,9], result is the subarray [2,3,1,8,6]
def get_subarray_sort(arr: List[int] = None) -> Optional[List[int]]:
    if arr is None:
        return arr
    else:
        lower_index = i = 0
        upper_index = j = len(arr) - 1
        while i < len(arr):
            if arr[i + 1] - arr[i] < 0:
                lower_index = i
                break
            else:
                i += 1

        while j >= 0:
            if arr[j - 1] - arr[j] > 0:
                upper_index = j
                break
            else:
                j -= 1

        print(f"i={i}, j={j}, lower_index={lower_index}, upper_index={upper_index}")
        min_ele = min(arr[lower_index:upper_index + 1])
        max_ele = max(arr[lower_index:upper_index + 1])
        print(f"min:{min_ele}, max:{max_ele}")
        i, j = j + 1, i - 1

        while i < len(arr):
            if arr[i] < max_ele:
                upper_index += 1
                print(f"iterating in i, i={i}, arr[i]={arr[i]}, upper={upper_index}")
            i += 1

        while j >= 0:
            if arr[j] > min_ele:
                lower_index -= 1
                print(f"iterating in j, j={j}, arr[j]={arr[j]}, upper={lower_index}")

            j -= 1

        return arr[lower_index:upper_index + 1]


# Given a sorted array in non-decreasing order, return an array of squares of each number, also in non-decreasing order.
# For example: [-4,-2,-1,0,3,5] -> [0,1,4,9,16,25]
# How can you do it in O(n) time?
def sorted_square_num(array: List[int]) -> List[int]:
    """
    Approach: maintain 2 pointers from start and end and compare values and based on the greater number,
    fill the output array from the back
    Time: O(n)
    Space: O(1) (doesn't include output complexity)
    :param array: list of integers
    :return: list of sorted squares of numbers
    """

    result = [0] * len(array)
    start, end, index = 0, len(array) - 1, len(array) - 1

    while start <= end:
        if abs(array[start]) < abs(array[end]):
            curr = array[end]
            end -= 1
        elif abs(array[start]) > abs(array[end]):
            curr = array[start]
            start += 1
        else:
            curr = array[start]
            end -= 1
            start += 1

        result[index] = curr * curr
        index -= 1

    return result


# Reverse the order of elements in an array. For example, A = [1,2,3,4,5,6], Output = [6,5,4,3,2,1]
def reverse_array(arr: List[int]) -> None:
    start, end = 0, len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


# (Level: Easy) Two Sum Problem - Find 2 numbers in a sorted array that sum to X.
# For example, if A = [1,2,3,4,5] and X = 9, the numbers are 4 and 5.
def two_sum(arr, target):
    """
    using 2 pointers
    Time: O(n)
    Space: O(1)
    :param arr: Array of whole numbers (won't work for negative numbers)
    :param target: target sum
    :return: list of 2 integers which add up to target
    """
    start, end = 0, len(arr) - 1

    while start < end:
        to_find = target - arr[start]
        if to_find > arr[end]:
            end -= 1
        elif to_find < arr[end]:
            start += 1
        else:
            return [arr[start], arr[end]]

    return ["gol gol anda"]


if __name__ == '__main__':
    array: List[int] = [1, 3, 5, 2, 6, 4, 7, 8, 9]

    print(get_subarray_sort(array))
    print("Sorted squares:")
    nums = [[-4, -2, -1, 0, 3, 5], [-9, 8, 9], [1, 2, 3, 4]]
    for nums_arr in nums:
        print(nums_arr)
        print(sorted_square_num(nums_arr))
        print(two_sum(nums_arr, 5))
        reverse_array(nums_arr)
        print(nums_arr)
        print()
