from typing import List
from random import randint


def single_partition(num_array: List[int], pivot_index: int, start: int, end: int) -> int:
    print("**" * 20)
    print(f"Before: {num_array}, pivot = {num_array[pivot_index]}")
    # putting the pivot element at the beginning of the array
    num_array[start], num_array[pivot_index] = num_array[pivot_index], num_array[start]
    print(f"put pivot at the beginning: {num_array}")
    # cloud for elements <= pivot element
    less = start

    for i in range(start + 1, end + 1):
        if num_array[i] <= num_array[start]:
            num_array[less + 1], num_array[i] = num_array[i], num_array[less + 1]
            less += 1
        print(f"index: {i}, less: {less}, element at less: {num_array[less]}")
    # switching back the element to the real pivot index, i.e. the end of the cloud (variable: less)
    num_array[less], num_array[start] = num_array[start], num_array[less]
    print(f"Final state: {num_array}")
    print("--" * 20)
    return less


def find_kth_helper(num_array: List[int], target_index: int, start: int, end: int) -> int:
    print(f"num_array:{num_array}, target_index:{target_index}, start:{start}, end:{end}")
    if start > end:
        raise Exception("start index > end index")
    elif start is None or end is None:
        raise Exception("IllegalArgumentException: start and end indices as None")

    random_index = randint(start, end)
    pivot_index = single_partition(num_array, random_index, start, end)
    print(f"pivot_index:{pivot_index}")
    if pivot_index == target_index:
        return num_array[pivot_index]
    elif pivot_index > target_index:
        print(f"pivot_index {pivot_index}<{target_index} target_index")
        print(f"find_kth_helper({num_array}, {target_index}, 0, {pivot_index - 1})")
        return find_kth_helper(num_array, target_index, 0, pivot_index - 1)
    else:
        print(f"pivot_index {pivot_index}>{target_index} target_index")
        print(f"find_kth_helper({num_array}, {target_index}, {pivot_index + 1}, {end})")
        return find_kth_helper(num_array, target_index, pivot_index + 1, end)


if __name__ == '__main__':
    array: List[int] = [5, 7, 4, 6, 5, 3, 3]
    k = 3
    print(find_kth_helper(array, k - 1, 0, len(array) - 1))

    array = [4, 6, 1, 2, 4, 3, 5]
    k = 3
    print(find_kth_helper(array, k - 1, 0, len(array) - 1))
