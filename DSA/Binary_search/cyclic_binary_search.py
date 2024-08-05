def get_smallest_ele_in_cyclic_sorted_array(array):
    '''
    Complexity: O(logn)
    :param array:
    :return: index for the minimum element
    '''
    low = 0
    high = len(array) - 1
    if array[low] < array[high]:
        return low
    elif array is None or len(array) == 0:
        return None
    else:

        while low <= high:
            mid = low + (high - low) // 2
            print(f"low:{low}\tmid:{mid}\thigh:{high}")
            print(f"{array[low]}\t{array[mid]}\t{array[high]}")

            if mid == 0:
                return mid
            # checking of next element is smaller than previous element
            # if true, return the index since it is the place where the largest and smallest element are present
            elif array[mid] > array[mid + 1]:
                return mid + 1

            # comparing with the left most element to check if the elements within the range are sorted or not
            # if not sorted, it means that the minimum element is somewhere in between
            if array[low] > array[mid]:
                high = mid
            else:
                low = mid


if __name__ == '__main__':
    a = [4]   # 6, 8,0 [789, -789, -1, 2, 99]
    # [1,2,3,4,5,6,7,8,9]
    # [4,5,6,1,2,3]
    # [2, 3, 4, 5, 1]
    # [4,5,6,1,2,3]
    # [2,3,4,5,1]

    print(get_smallest_ele_in_cyclic_sorted_array(a))
