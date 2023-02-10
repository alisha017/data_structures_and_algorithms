from typing import Optional, List


def swap(a: int, b: int):
    temp: int = a
    a = b
    b = temp
    return a, b

'''
You are given an array of integers. Rearrange the array so that all zeroes are at the beginning of the array.
For example, [4,2,0,1,0,3,0] -> [0,0,0,4,1,2,3]
'''

def zeroes_at_the_end(arr: List[int] = None) -> Optional[List[int]]:
    if arr is None:
        return arr
    else:
        zero_cloud_ele: int = len(arr) - 1
        counter: int = len(arr) - 1
        while counter >= 0:
            if arr[counter] == 0:
                arr[counter], arr[zero_cloud_ele] = swap(arr[counter], arr[zero_cloud_ele])
                zero_cloud_ele -= 1
            counter -= 1
        return arr


def zeroes_at_the_beginning(arr: List[int] = None) -> Optional[List[int]]:
    if arr is None:
        return arr
    else:
        zero_cloud_ele: int = 0
        counter: int = 0
        while counter < len(arr):
            if arr[counter] == 0:
                arr[counter], arr[zero_cloud_ele] = swap(arr[counter], arr[zero_cloud_ele])
                zero_cloud_ele += 1
            counter += 1
        return arr

'''
Given an array with n marbles colored Red, White or Blue, sort them so that marbles of the same color are adjacent, with the colors in the order Red, White and Blue.
Assume the colors are given as numbers - 0 (Red), 1 (White) and 2 (Blue).
For example, if A = [1,0,1,2,1,0,1,2], Output = [0,0,1,1,1,1,2,2].
'''
def dutch_flag_problem(pivot: int = None, arr: List[int] = None) -> Optional[List[int]]:
    if arr is None or pivot is None:
        return arr
    else:
        low_boundary: int = 0
        high_boundary: int = len(arr)-1
        i = 0
        while i <= high_boundary:
            if arr[i] < pivot:
                arr[i], arr[low_boundary] = swap(arr[i], arr[low_boundary])
                low_boundary += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[high_boundary] = swap(arr[i], arr[high_boundary])
                high_boundary -= 1
            else:
                i += 1
        return arr


if __name__ == '__main__':
    array: List[int] = [4, 2, 0, 1, 0, 3, 0]
    print(zeroes_at_the_end(array))
    print(zeroes_at_the_beginning(array))

    print(dutch_flag_problem(4, [5, 2, 4, 4, 6, 4, 4]))
