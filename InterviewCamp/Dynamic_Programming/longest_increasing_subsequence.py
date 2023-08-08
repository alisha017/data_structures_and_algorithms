from typing import List


def get_longest_increasing_subsequence(num_list: List[int]):
    """
    - having the longest increasing subsequence length upto i+1 (bottom-up approach)
    :time_complexity: O(n^2)
    :space_complexity: O(n)
    :param num_list: List[int]
    :return: int, length of the longest increasing subsequence
    """
    longest = [1]*len(num_list)
    result = 1
    print(num_list, "\n************")
    for i in range(len(num_list)):
        for j in range(i):
            if num_list[j] < num_list[i]:
                print(f"\tnum_list[j] < num_list[i]--> longest[i]={longest[i]}, longest[j]+1={longest[j]+1}")
                longest[i] = max(longest[i], longest[j]+1)
            print(f"num[i]:{num_list[i]}({i}), num[j]:{num_list[j]}({j}), longest:{longest}")

        result = max(result, longest[i])
    return result


if __name__ == "__main__":
    print(get_longest_increasing_subsequence([1, 3, 2, 5, 3, 5, 6]))
    print(get_longest_increasing_subsequence([6, 9, 8, 2, 3, 5, 1, 4, 7]))
    print(get_longest_increasing_subsequence([4, 1, 3, 6, 8, 2, 9]))
