"""
Get complement of integer (from the most significant bit)
num 00101 --> 1s complement = 00010
"""
import math


def get_ones_complement(num):
    mask = (1 << (math.floor(math.log2(num)+1))) - 1

    return num ^ mask


if __name__ == "__main__":
    print(get_ones_complement(5))