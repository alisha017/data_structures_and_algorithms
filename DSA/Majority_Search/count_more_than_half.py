from typing import List


def find_majority_number(array: List[int]):
    if len(array) == 0 or array is None:
        return None

    candidate: int = array[0]
    count = 1
    for num in array:
        if num == candidate:
            count += 1
        elif count > 0:
            count -= 1
        else:
            candidate = num
            count = 1

    count = 0

    for num in array:
        if num == candidate:
            count += 1

    return candidate if count > len(array) // 2 else None


if __name__ == "__main__":
    array = [[1, 2, 1, 3, 4, 1, 1], [1, 2, 3, 4, 5, 6, 7]]

    for arr in array:
        print(arr)
        print(f"Majority candidate:{find_majority_number(arr)}")
