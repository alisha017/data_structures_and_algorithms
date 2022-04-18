from typing import Optional, List


def get_contiguous_array_with_max_sum(arr: List[int] = None) -> Optional[List[int]]:
    if arr is None:
        return None
    else:
        current_sum = max_sum = arr[0]
        lower_boundary = 0
        upper_boundary = 0

        for i in range(1, len(arr)):
            current_sum += arr[i]
            # print(current_sum, max_sum)

            if current_sum < arr[i]:
                current_sum = max_sum = arr[i]
                lower_boundary = i
            if max_sum < current_sum:
                max_sum = current_sum
                upper_boundary = i

            # print(arr[lower_boundary:upper_boundary + 1], current_sum)

        return arr[lower_boundary:upper_boundary + 1]


if __name__ == '__main__':
    array = [1, 2, -1, 2, -3, 2, -5]
    array2 = [-2, -3, 4, -1, -2, 1, 5, -1]
    array3 = [-3, 1, -8, 12, 0, -3, 5, -9, 4]
    print(get_contiguous_array_with_max_sum(array))
    print(get_contiguous_array_with_max_sum(array2))
    print(get_contiguous_array_with_max_sum(array3))
