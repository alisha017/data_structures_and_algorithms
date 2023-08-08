"""
Given a number N, swap bits i and j.
num=0101, i=0 and j=3 --> 1100
"""
import math

def get_a_bit(num, bit_index):
    """ bit at 4th index would return 16, to get a boolean like value,
    use normalized version of this function """
    return num & (1 << bit_index)


def get_normalized_bit(num, bit_index):
    return (num >> bit_index) & 1


# interchanging bits at index i and j
def swap_bits(num, i, j):
    # print("\t", num, bin(num), i, get_normalized_bit(num, i), j, get_normalized_bit(num, j))
    if (get_normalized_bit(num, i)) != get_normalized_bit(num, j):
        # print("\tbits at i and j are different")
        return num ^ ((1 << i) | (1 << j))
    else:
        # print("\tbits at i and j are same")
        return num


def reverse_bits(num, no_of_bits):
    i, j = 0, no_of_bits-1
    curr_num = num
    print("j=", j)
    while i < j:
        # print(curr_num, i, j, bin(curr_num))
        curr_num = swap_bits(curr_num, i, j)
        # print("\t\t", curr_num, bin(curr_num))
        i += 1
        j -= 1

    return curr_num


if __name__ == "__main__":
    # print(swap_bits(14, 0, 3))
    print(reverse_bits(0b11001, 5))
    print(reverse_bits(0b00000010100101000001111010011100, 32))  # 964176192
