"""
Count no of bits in the number --> meaning counting no of 1s
Space: O(1), Time: O(k) where k = no of 1s
"""


def count_number_of_bits(num):
    count = 0
    while num != 0:
        count += 1
        num = num & (num-1)
    return count


if __name__ == "__main__":
    print(count_number_of_bits(23))
    print(count_number_of_bits(4))
    print(count_number_of_bits(7))
