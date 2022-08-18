from typing import List

PHONE_MNEMONIC = {
    0: [],
    1: [],
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"]
}


def print_combinations(array, buffer_, array_index=0, buffer_index=0):
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


def print_phone_mnemonics(phone_number: List[int], buffer: List[str], array_index: int = 0, buffer_index: int = 0):
    # termination case:
    if buffer_index == len(buffer) or array_index == len(phone_number):
        print(buffer)
        return

    # finding candidates
    possible_elements = PHONE_MNEMONIC[phone_number[array_index]]
    # print(f"Current: {phone_number[array_index]} -- {possible_elements}")
    if len(possible_elements) == 0:
        print_phone_mnemonics(phone_number, buffer, array_index + 1, buffer_index)

    # placing items in buffer
    for letter in possible_elements:
        buffer[buffer_index] = letter
        print_phone_mnemonics(phone_number, buffer, array_index + 1, buffer_index + 1)


def print_subsets(array: List[int], buffer: List[int], array_index: int = 0, buffer_index: int = 0):
    # 1.termination case
    print(buffer[:buffer_index])
    if buffer_index == len(buffer) or array_index == len(array):
        return

    # 2. find all candidates
    for i in range(array_index, len(array)):  # 1, 4
        # 3. putting the candidates in the buffer
        buffer[buffer_index] = array[i]  # 2
        # print(f"Buffer: {buffer_index}, current: {i}, array:{array_index}")
        # 4. recurse into other elements
        print_subsets(array, buffer, i + 1, buffer_index + 1)  # 3,3 buf = [1, 2, -1]


def print_permutations(array: List[int], buffer: List[int], is_in_buffer: List[bool], buffer_index: int = 0):
    if buffer_index == len(buffer):
        print(buffer)
        return

    for i in range(len(array)):
        if is_in_buffer[i] is False:
            is_in_buffer[i] = True
            buffer[buffer_index] = arr[i]
            print_permutations(array, buffer, is_in_buffer, buffer_index + 1)
            is_in_buffer[i] = False


def print_coins(coins_list, target, start_index=0, buffer=[], current_sum=0):
    if current_sum > target:
        return
    if current_sum == target:
        print("********")
        print(f"Result: {buffer}")
        print("********")
        return

    for i in range(start_index, len(coins_list)):
        buffer.append(coins_list[i])
        print(f"Current buffer status (pushing): {buffer}")
        print(f"Current sum:{current_sum+coins_list[i]}")

        # note: in the recursion, we keep sending i, not updating the value,
        # hence making sure that we are resuing the value until we get the desired result
        print_coins(coins_list, target, i, buffer, current_sum+coins_list[i])
        buffer.pop()
        print(f"Current buffer status (popping): {buffer}")


def print_all_combinations_of_array(array, buffer_size):
    if buffer_size < 1 or len(array) < 1 or array is None or buffer_size is None or buffer_size > len(array):
        print("No combinations possible!")
        return
    buffer_array = [None] * buffer_size
    print_combinations(array, buffer_array)


def print_all_combos_phone_pnemonics(phone_num):
    if phone_num is None or len(phone_num) < 1:
        print("No combination of phone mnemonics possible...")
        return
    phone_num_array = [int(num) for num in phone_num]
    buffer_size = len(phone_num_array)

    buffer_size -= (phone_num_array.count(0) + phone_num_array.count(1))
    print_phone_mnemonics(phone_num_array, [""] * buffer_size)


def print_all_subsets_of_array(array):
    if len(array) < 1 or array is None:
        print("No combinations possible!")
        return
    buffer_array = [-1] * len(array)
    print(f"buffer: {buffer_array}")
    print_subsets(array, buffer_array)


def print_all_permutations_of_array(array, buffer_size):
    if buffer_size is None or array is None or len(array) < 1 or buffer_size < 1:
        print("No permutations possible")
        return

    is_in_buffer = [False] * len(array)
    buffer_array = [-1] * buffer_size

    print_permutations(array, buffer_array, is_in_buffer)


def print_all_coin_combinations(coins_list, target):
    if coins_list is None or len(coins_list) < 1 or target < 1:
        print("No coin combinations possible...")
        return

    print_coins(coins_list, target)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    # print_all_combinations_of_array(arr, 3)
    # print_all_subsets_of_array(arr)
    # print_all_permutations_of_array(arr, 3)
    phone_number = ["021", "234"]
    # [print_all_combos_phone_pnemonics(num) for num in phone_number]

    coins = [1,2,5]
    print_all_coin_combinations(coins, 5)
