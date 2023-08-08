"""
Given an integer, flip all its bits.
----> XOR gate:
    0^0 = 1^1 = 0
    1^0 = 0^1 = 1

----> XOR to flip bits
    a^1 = ~a
        a = 1 : 1^1 = 0
        a = 0 : 0^1 = 1
"""


def flip_bits(num: int):
    bit_length = num.bit_length()
    flipper: int = int(bin((2**bit_length)-1), base=2)
    print(flipper)

    return num ^ flipper


def toggle_a_bit(num, bit_index):
    return num ^ (1 << bit_index)


def get_a_bit(num, bit_index):
    return num & (1 << bit_index)


def set_a_bit(num, bit_index, to_set):
    if to_set == 1:
        return num | (1 << bit_index)
    else:
        return num & (~ (1 << bit_index))


if __name__ == "__main__":
    to_flip: int = 25
    print(flip_bits(to_flip))
    print(toggle_a_bit(to_flip, 3))
    print(get_a_bit(to_flip, 3))
    print(set_a_bit(to_flip, 3, 1))
    print(get_a_bit(to_flip, 0))
    print(set_a_bit(to_flip, 0, 0))

    for i in range(to_flip.bit_length()):
        print(i, get_a_bit(to_flip, i), to_flip, bin(to_flip))

    print(3, get_a_bit(to_flip, 3), to_flip, bin(to_flip))
