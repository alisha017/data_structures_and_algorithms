def is_string_a_rotation(string: str, to_check: str):
    if string == to_check:
        return True
    else:
        appended_string = string+string
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


def longest_palindrome(string: str):
    print(string)

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

    for i in range(0, len(string)):
        pass

    pass


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