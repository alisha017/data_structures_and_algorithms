def search_for_k(array, k):
    start = 0
    end = len(array) - 1

    if len(array) == 0 or array is None:
        return -1
    while start <= end:
        mid = start + (end - start) // 2
        if k < array[mid]:
            end = mid-1
        elif k > array[mid]:
            start = mid+1
        else:
            return mid


def index_of_k_when_inserted(array, k):
    low = 0
    high = len(array) - 1
    print("mid\tarray[mid]\thigh\tlow")

    if array[low] > k:
        return low
    elif array[high] < k:
        return high
    else:
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] > k:
                print()
                high = mid-1
                print(f"{mid}\t\t{array[mid]}\t\t{high}\t\t{low}")
            elif array[mid] < k:
                low = mid+1
                print(f"{mid}\t\t{array[mid]}\t\t{high}\t\t{low}")
            else:
                if array[mid + 1] == k:
                    # high = mid-1 ## if insert before all the ks
                    low = mid + 1
                    print(f"{mid}\t\t{array[mid]}\t\t{high}\t\t{low}")
                else:
                    print(f"{mid}\t\t{array[mid]}\t\t{high}\t\t{low}")
                    return mid

            if low == high - 1:
                print(f"{mid}\t\t{array[mid]}\t\t{high}\t\t{low}")
                return high


def find_first_occurrence(array, target):
    high = len(array) -1
    low = 0
    result = -1

    while low <= high:
        mid = (high+low)//2

        if array[mid] > target :
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else:
            result = mid
            high = mid - 1

    return result


def find_last_occurrence(array, target):
    high = len(array) -1
    low = 0
    result = -1

    while low <= high:
        mid = (high+low)//2

        if array[mid] > target :
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else:
            result = mid
            low = mid + 1

    return result


def find_target_or_nearest_element(array, k):
    low = 0
    high = len(array) - 1
    print("mid\tarray[mid]\thigh\tlow")
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] > k:
            high = mid+1
        elif array[mid] < k:
            low = mid-1
        else:
            return mid

        print(f"{mid}\t\t{array[mid]}\t\t{high}\t\t{low}")

        if low == high - 1:
            if abs(array[low] - k) < abs(array[high] - k):
                return low
            else:
                return high


if __name__ == '__main__':
    array = [1,2,6,8]
    k = 6
    # print(search_for_k(array, k))
    # print(index_of_k_when_inserted([1,2,4,4,6,8], 3))
    # print(index_of_k_when_inserted([1,2,4,4,6,8], 0))
    # print(index_of_k_when_inserted([1,2,4,4,4,6,8], 4))
    # print(find_target_or_nearest_element([1, 2, 4, 5, 8, 9], 6))
    print(find_first_occurrence([1,2,2,2,3,4,4,4,5], 2))
    print(find_last_occurrence([1,2,2,2,3,4,4,4,5], 4))
