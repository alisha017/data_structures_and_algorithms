def is_string_a_rotation(string: str, to_check: str):
    if string == to_check:
        return True
    else:
        appended_string = string + string
        if to_check in appended_string and len(to_check) == len(string):
            return True
        else:
            return False


def reverse_words_in_a_string(string: str):
    if string == "":
        return string
    if string is None:
        raise Exception("Null string exception")

    reversed_string = string[::-1]
    # print(reversed_string, str(reversed_string))

    reversed_string_words_list = reversed_string.split(" ")
    # print(reversed_string_words_list)

    words_reversed = " ".join([word[::-1] for word in reversed_string_words_list])
    return words_reversed


def rotate_an_array_by_x(arr, x):
    """
    Applying the same concept as reversing the string
    :space_complexity: O(1)
    :time_complexity: O(n)
    :param arr: list
    :param x: int
    :return: list
    """
    if len(arr) < x or len(arr) < 1 or x is None or arr is None:
        return None
    reversed_array = arr[::-1]
    # print(reversed_array)
    arr1 = reversed_array[:x][::-1]  # reversed[len(arr):x-1:-1]
    # print(arr1)
    arr2 = reversed_array[x:][::-1]  # reversed[x:][::1]
    # print(arr2)

    return arr1 + arr2  # arr2+arr1


def is_valid_index(array, index):
    if index < 0 or index >= len(array):
        return False
    else:
        return True


def longest_palindrome(string: str):
    """
    :time_complexity: O(n^2)
    :space_complexity: O(n)
    :param string: str
    :return: str, largest palindrome
    """
    if string is None or string == "":
        return None
    elif len(string) == 1:
        return string
    elif len(string) == 2:
        if string[0] == string[1]:
            return string
        else:
            return string[0]

    longest_palindrome_str: str = string[0]

    # for odd length of palindrome
    for i in range(0, len(string)):
        offset = 0

        while is_valid_index(string, i - offset) is True and is_valid_index(string, i + offset) is True \
                and string[i + offset] == string[i - offset]:
            offset += 1

        if len(longest_palindrome_str) < offset * 2 + 1:
            longest_palindrome_str = string[i - offset+1:i + offset]

    # for even length palindrome
    for i in range(0, len(string)):
        offset = 0

        while is_valid_index(string, i - offset) is True and is_valid_index(string, i + offset + 1) is True \
                and string[i + offset + 1] == string[i - offset]:
            offset += 1

        if len(longest_palindrome_str) < offset * 2:
            longest_palindrome_str = string[i - offset + 1:i + offset+1]

    return longest_palindrome_str


if __name__ == '__main__':
    # words = [("bobcat", "catbob"), ("laisha", "alisha"), ("mehul", "ehu")]
    # for strings in words:
    #     if is_string_a_rotation(strings[0], strings[1]):
    #         print(f"Yes, {strings[1]} is a rotation of {strings[0]}")
    #     else:
    #         print(f"No, {strings[1]} is not a rotation of {strings[0]}")

    print(reverse_words_in_a_string("this is a string"))
    print(reverse_words_in_a_string("alisha is super awesome"))
    print(reverse_words_in_a_string("mehul is super awesome too"))

    print(rotate_an_array_by_x([1, 2, 3, 4, 5, 6], 2))
    print(longest_palindrome("abcivicyz"))
    print(longest_palindrome("kayaknancy"))
    print(longest_palindrome("mausikanak"))
    print(longest_palindrome("abccbabob"))
    print(longest_palindrome("bestabbamusic"))
    print(longest_palindrome("sttscannac"))
    print(longest_palindrome("kayakabba"))
