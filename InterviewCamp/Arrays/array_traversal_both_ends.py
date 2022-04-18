"""
Level: MediumGiven an array of integers, find the shortest sub array, that if sorted, results in the entire array being sorted.

For example:[1,2,4,5,3,5,6,7] --> [4,5,3] - If you sort from indices 2 to 4, the entire array is sorted.
[1,3,5,2,6,4,7,8,9] --> [3,5,2,6,4] -  If you sort from indices 1 to 5, the entire array is sorted.
"""

from typing import Optional, List


def get_subarray_sort(arr:List[int]=None) -> Optional[List[int]]:

    if arr is None:
        return arr
    else:
        lower_index = i = 0
        upper_index = j = len(arr)-1
        while i < len(arr):
            if arr[i+1]-arr[i] < 0:
                lower_index = i
                break
            else:
                i += 1

        while j >= 0:
            if arr[j-1]-arr[j] > 0:
                upper_index = j
                break
            else:
                j -= 1

        min_ele = min(arr[lower_index:upper_index+1])
        max_ele = max(arr[lower_index:upper_index+1])

        i, j = j+1, i-1

        while i < len(arr):
            if arr[i] < max_ele:
                upper_index += 1
            i += 1

        while j >= 0:
            if arr[j] > min_ele:
                lower_index -= 1
            j -= 1

        return arr[lower_index:upper_index+1]


if __name__ == '__main__':
    array:List[int] = [1,3,5,2,6,4,7,8,9]

    print(get_subarray_sort(array))
