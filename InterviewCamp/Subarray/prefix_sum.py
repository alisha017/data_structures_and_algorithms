"""
Prefix Sums ; Level: Medium
Given an array of integers, both -ve and +ve, find a contiguous subarray that sums to 0.
For example: [2,4,-2,1,-3,5,-3] --> [4,-2,1,-3]
"""


def get_prefix_sum_to_zero(array):
    sum_dictionary = dict()
    sum = 0
    for i in range(len(array)):
        sum += array[i]

        if sum == 0:
            return array[0:i+1]

        if sum in sum_dictionary:
            return array[sum_dictionary[sum]+1:i+1]
        else:
            sum_dictionary[sum] = i


def get_prefix_sum_to_x(array, x):
    sum_dictionary = dict()
    sum = 0
    for i in range(len(array)):
        sum += array[i]

        if sum == x:
            return array[0:i + 1]

        if (sum-x) in sum_dictionary:
            print(sum, x - sum)
            print(sum_dictionary[x-sum], i)
            print(array[sum_dictionary[sum-x] + 1:i + 1])
            return array[sum_dictionary[sum-x] + 1:i + 1]
        else:
            sum_dictionary[sum] = i


if __name__ == '__main__':
    array = [2,4,-2,1,-3,5,-3]
    # print(get_prefix_sum_to_zero(array))
    # print(get_prefix_sum_to_x(array, 5))

    print(get_prefix_sum_to_x([4,-8,9,-4,1,-8,-1,6], 6))
    pass
