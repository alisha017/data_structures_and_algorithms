from typing import List, Dict


def count_majority_1_over_k(array: List[int], k: int):
    if array is None or len(array) == 0:
        return None
    hash_map: Dict[int, int] = {}
    for num in array:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

        if len(hash_map) == k:
            for val in hash_map:
                hash_map[val] -= 1

        for key in list(hash_map.keys()):
            if hash_map[key] == 0:
                del hash_map[key]

    return max(hash_map, key=hash_map.get) if len(hash_map) > 0 else None


if __name__ == "__main__":
    array = [[2, 4, 5, 2, 4, 2, 2, 1, 5], [2, 4, 5, 2, 4, 2, 6, 1, 5]]
    k = [3, 3]
    for i in range(len(array)):
        print(array[i])
        print(f"Majority n/k (k={k[i]}, n={len(array[i])}) = {count_majority_1_over_k(array[i], k[i])}")
