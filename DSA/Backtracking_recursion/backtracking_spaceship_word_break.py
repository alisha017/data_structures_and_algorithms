from enum import Enum
from typing import List, Set


class State(Enum):
    UNVISITED = 0
    NOT_FOUND = 1


def split_word(string: str, start_index: int, memo: List[State], result: List[str], dictionary: Set[str]):
    # print(f"Current result:{result}, memo[{start_index}]:{memo[start_index]}")
    if start_index == len(string):
        print("Reached end!!")
        return True

    if memo[start_index] == State.NOT_FOUND:
        print(f"Word not found at this index: {start_index}")
        return False

    for i in range(start_index, len(string)):
        candidate = string[start_index:i + 1]
        print(f"Candidate:{candidate}")
        if candidate in dictionary:
            result.append(candidate)
            if split_word(string, i + 1, memo, result, dictionary) is True:
                return True
            else:
                result.pop()
        print(f"New result:{result}, memo[{i}]:{memo[i]}, string[{i}]:{string[i]}")
    memo[start_index] = State.NOT_FOUND
    return False


def word_break_problem(string: str):
    if string is None or len(string) < 1:
        return None

    memo = [State.UNVISITED] * len(string)
    # dictionary = {"i", "like", "man", "mango", "tan", "tango", "go", "a"}
    dictionary = {"an", "the", "cats", "cat", "dog", "and", "sand"}
    result = []

    if split_word(string, 0, memo, result, dictionary) is True:
        return result
    else:
        return None


if __name__ == "__main__":
    print("Hello world!")

    # words = ["ilikemangotango", "ilikemango", "ilikechocolate"]
    words = ["catsandogcat"]

    for word in words:
        print(word_break_problem(word))
