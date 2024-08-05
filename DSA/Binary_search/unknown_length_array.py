def get_ele_from_unknown_length_array(array, k):
    low = 0
    range_low = 1
    early_flag = False

    if array is None:
        return None

    # get the upper limit / length of the array
    # upper limit meaning if element found within the range, no reason to find the entire length of the array
    while 1:
        print(range_low)
        index = range_low*2
        print(index)
        try:
            temp = array[index]
            print(f"Element found at {index}: {temp}")
            if array[index] > k:
                print(f"k found at index < {index}")
                early_flag = True
                high = index
                break
            range_low = index
        except IndexError as e:
            high = index
            break
    print(f"Current status: {low}, {range_low}, {high}, {index}")

    # binary search for finding the upper index
    if early_flag is False:
        while range_low <= high:
            mid = range_low + (high - range_low) // 2
            try:
                temp = array[mid]
            except IndexError as e:
                high = mid-1
                continue

            try:
                temp = array[mid+1]
            except IndexError as e:
                high = mid
                break

    # binary search for the element
    print(f"length of array:{low} to {high}")
    while low <= high:
        mid = low + (high-low)//2
        print(f"low:{low}, mid:{mid}, high:{high}")
        if array[mid] < k:
            low = mid+1
        elif array[mid] > k:
            high = mid-1
        else:
            return mid
    return -1


if __name__ == '__main__':
    array = [0]
    print(get_ele_from_unknown_length_array(array, -1213))
    pass
