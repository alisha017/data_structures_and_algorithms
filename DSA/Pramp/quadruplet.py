def print_combinations(array, buffer_, target, array_index=0, buffer_index=0):
    # 1.termination case
    if buffer_index == len(buffer_):
        print(buffer_[:buffer_index])
        return
    if array_index == len(array):
        return
    # 2. find all candidates
    for i in range(array_index, len(array)):  # 1, 4
        # 3. putting the candidates in the buffer
        buffer_[buffer_index] = array[i]  # 2

        # 4. recurse into other elements
        print_combinations(array, buffer_, i + 1, buffer_index + 1)  # 3,3 buf = [1, 2, -1]


def print_all_combinations_of_array(array, buffer_size, target):
    if buffer_size < 1 or len(array) < 1 or array is None or buffer_size is None or buffer_size > len(array):
        print("No combinations possible!")
        return
    buffer_array = [None] * buffer_size
    print_combinations(array, buffer_array, target)


if __name__ == "__main__":
    print_all_combinations_of_array([2, 7, 4, 0, 9, 5, 1, 3], 4, 20)