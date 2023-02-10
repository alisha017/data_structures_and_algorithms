from typing import List


def zero_pad_array(array, pad_len):
    for i in range(pad_len):
        array.insert(0, 0)


def add_without_operator(num1: List[int], num2: List[int]):
    larger_num, smaller_num = (num1, num2) if len(num1) > len(num2) else (num2, num1)

    result = [0] * (len(larger_num) + 1)

    zero_pad_array(smaller_num, len(larger_num) + 1 - len(smaller_num))
    zero_pad_array(larger_num, 1)

    carry = 0

    for i in range(len(larger_num) - 1, -1, -1):
        # print(i, larger_num[i], smaller_num[i])
        sum = larger_num[i] + smaller_num[i] + carry
        result[i] = sum % 10
        carry = sum // 10

    return result


def multiply_without_operator(num1: List[int], num2: List[int]):
    zero_end_pad = 0
    result = [0] * (len(num1) + len(num2))

    for i in range(len(num1) - 1, -1, -1):
        intermediate_result = [0] * (len(num2) + zero_end_pad + 1)
        carry = 0
        for j in range(len(num2) - 1, -1, -1):
            product = num1[i] * num2[j] + carry
            intermediate_result[j+1] = product % 10
            carry = product // 10

        result = add_without_operator(result, intermediate_result)
        zero_end_pad += 1

    return result


if __name__ == "__main__":
    print(add_without_operator([1, 2, 1, 3], [1, 2, 9]))
    print(add_without_operator([9, 9, 9, 9], [9, 9]))
    # a = [1,2]
    # zero_pad_array(a, 5)
    # print(a)

    print(multiply_without_operator([1, 1, 0], [1, 2]))
