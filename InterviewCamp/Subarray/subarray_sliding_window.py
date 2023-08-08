"""
Given: an array of positive integers
Expected result: starting and ending indices of the subarray
find a subarray with a given sum = N.
"""

from typing import Optional, List, Set


def get_subarray_with_sum_n(arr: List[int] = None, target: int = None) -> Optional[Set[int]]:
    start_pos: int = 0
    end_pos: int = 0
    sum = arr[start_pos]

    while start_pos < len(arr):
        if start_pos == len(arr) - 1:
            break

        if sum > target:
            sum -= arr[start_pos]
            start_pos += 1
        elif sum < target:
            end_pos += 1
            sum += arr[end_pos]
        else:
            break

    print(arr[start_pos:end_pos + 1])
    return {start_pos, end_pos}


def get_longest_substring_with_unique_char(string: str) -> str:  # Optional[Set[int]]:
    string.lower()
    end_pos = 0
    start_pos = 0
    substr = ''
    # a dictionary to maintain the latest position of the characters
    char_dictionary = {}
    max_substr = substr

    for i in range(len(string)):

        if string[i] in char_dictionary:
            print(f"char = {string[i]} max of {char_dictionary[string[i]]+1}, {start_pos} ")

            # why max? because if there's another repeating char between previous occurrence of char and current
            # occurrence, then taking the latest one
            # j = max of last pos of repeating char + 1 and start of the substring

            # since the char already exists in the dictionary,
            # char_dictionary[string[i]] + 1 --> char next to the repeating one
            # susbtr[0] --> the start of the substring
            # if the substr contains string[i] i.e.location of string[i] < substr[0] then taking the next character
            # eg: what[w]hywhere -- what --> hatw
            # if location of string[i] > substr[0], then updating a substring from there
            # eg. whatwhyw[h]ere -- atwhy -- ywh

            j = max(char_dictionary[string[i]]+1, char_dictionary[substr[0]])
            char_dictionary[string[i]] = i
            substr = string[j:i+1]
            print(f"In dictionary: {substr}")
        else:
            char_dictionary[string[i]] = i
            substr += string[i]
            print(f"Not In dictionary: {substr}")

        if len(max_substr) < len(substr):
            print(max_substr, substr)
            max_substr = substr
            end_pos = i
            start_pos = char_dictionary[substr[0]]

        print(f"Max substring: {max_substr}")
        print(char_dictionary)
        print(start_pos, end_pos)

    print("Largest substring:", string[start_pos:end_pos+1])
    print(string[start_pos:end_pos+1])
    return string[start_pos:end_pos+1]


if __name__ == '__main__':
    array = [3,1,3,5,9,2,1,4,5,6,0]
    target = 10
    print(get_subarray_with_sum_n(array, target))

    # print(get_longest_substring_with_unique_char("whatwhywhere"))
    # print(get_longest_substring_with_unique_char("GEEKSFORGEEKS"))
    # print(get_longest_substring_with_unique_char("mehulmistryalishasingh"))
    # print(get_longest_substring_with_unique_char("pickoutthelongestsubstring"))
