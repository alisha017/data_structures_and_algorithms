from enum import Enum

from typing import List, Dict, Any


class State(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Pattern_To_Word_Map:
    def __init__(self, my_dictionary):
        self.__pattern_to_word_map = {}
        self.__dictionary = my_dictionary

    def get_all_patterns(self):
        for word in self.__dictionary:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                self.add_pattern(pattern, word)

        return self.__pattern_to_word_map

    def add_pattern(self, pattern, word):
        if word not in self.__dictionary:
            self.__dictionary.add(word)
        if pattern in self.__pattern_to_word_map:
            self.__pattern_to_word_map[pattern].append(word)
        else:
            self.__pattern_to_word_map[pattern] = [word]


class Node:
    def __init__(self, value: str):
        self.__value: str = value
        self.__neighbours: List['Node'] = self.generate_neighbours()
        self.__state: State = State.UNVISITED

    def get_neighbours(self):
        return self.__neighbours

    def get_value(self):
        return self.__value

    def get_state(self):
        return self.__state

    def add_neighbours(self, new_neighbour):
        self.__neighbours.append(new_neighbour)

    def generate_neighbours(self):
        # print("generating neighbours...")
        neighbours = []
        char_list = list(self.__value)

        ptwm_obj = Pattern_To_Word_Map()
        pattern_to_word_map = ptwm_obj.get_all_patterns()

        for i in range(len(char_list)):
            temp = char_list[i]
            char_list[i] = "*"

            pattern = "".join(char_list)
            # print(f"\t\t{char_list} --> {pattern}")
            if pattern in pattern_to_word_map:
                # print(f"\t\tpattern found in map:{pattern_to_word_map[pattern]}")
                neighbours.append(Node(pattern_to_word_map[pattern]))
            char_list[i] = temp
        return neighbours

    def set_state(self, new_state):
        self.__state = new_state

    def set_value(self, new_value):
        self.__value = new_value


class Queue:
    def __init__(self, arr_len: int):
        self.__front = 0
        self.__back = 0
        self.__current_length = 0
        self.__array = [None] * arr_len

    def enqueue(self, data: Any):
        if self.__current_length == len(self.__array):
            raise Exception("Queue full!")

        self.__array[self.__back] = data
        self.__back = (self.__back + 1) % len(self.__array)
        self.__current_length += 1

    def dequeue(self) -> Any:
        if self.__current_length == 0:
            raise Exception("Empty Queue!")

        deleted_element = self.__array[self.__front]
        self.__array[self.__front] = None
        self.__front = (self.__front + 1) % len(self.__array)
        self.__current_length -= 1

        return deleted_element

    def print_queue(self):
        print(self.__array)
        print(f"Front element at: {self.__front}, {self.__array[self.__front]}")
        print(f"Back element at: {self.__back}, {self.__array[self.__back]}")
        print(f"Current length = {self.__current_length}")

    def get_front(self):
        return self.__array[self.__front]

    def get_back(self):
        return self.__array[self.__back]

    def is_empty(self):
        return True if self.__current_length == 0 else False

    def is_full(self):
        return True if self.__current_length == len(self.__array) else False


def generate_neighbours_for_string(string: str, ptwm_obj):
    # print("generating neighbours...")
    neighbours = []
    char_list = list(string)

    pattern_to_word_map = ptwm_obj.get_all_patterns()

    for i in range(len(char_list)):
        temp = char_list[i]
        char_list[i] = "*"

        pattern = "".join(char_list)
        # print(f"\t\t{char_list} --> {pattern}")
        if pattern in pattern_to_word_map:
            # print(f"\t\tpattern found in map:{pattern_to_word_map[pattern]}")
            for p in pattern_to_word_map[pattern]:
                if p is not string:
                    neighbours.append(p)
        char_list[i] = temp
    return list(set(neighbours))


def word_ladder_using_node(start_string: str, end_string: str):
    word_queue: Queue = Queue(10)
    start_string_node = Node(start_string)
    visited_words_map: Dict[Node, int] = {start_string_node: 0}
    word_queue.enqueue(start_string_node)
    start_string_node.set_state(State.VISITING)

    while not word_queue.is_empty():
        current: Node = word_queue.dequeue()
        print(f"\nCurrent:{current.get_value()}, end string:{end_string}")
        if current.get_value() == end_string:
            return visited_words_map[current]

        print(f"{current.get_value()}'s neighbours: {current.get_neighbours()}")
        for neighbour in current.get_neighbours():
            print(f"Adding neighbour:{neighbour.get_value()} to current:{current.get_value()}")
            word_queue.enqueue(neighbour)
            neighbour.set_state(State.VISITING)
            visited_words_map[neighbour] = visited_words_map[current] + 1

        current.set_state(State.VISITED)
        print("*** Current visited map:", [(key.get_value(), value) for key, value in visited_words_map.items()])

    return -1


def word_ladder(start_string: str, end_string: str, my_dictionary):
    if start_string == end_string:
        return 0

    word_queue: Queue = Queue(10000)
    visited_words_map: Dict[str, int] = {start_string: 0}
    word_queue.enqueue(start_string)

    ptwm_obj = Pattern_To_Word_Map(my_dictionary)
    while not word_queue.is_empty():
        current: str = word_queue.dequeue()
        print(f"\nCurrent:{current}, end string:{end_string}")
        if current == end_string:
            return visited_words_map[current] + 1

        print(f"{current}'s neighbours: {generate_neighbours_for_string(current, ptwm_obj)}, "
              f"\nlevel:{visited_words_map[current]}")
        for neighbour in generate_neighbours_for_string(current, ptwm_obj):
            # print(f"Adding neighbour:{neighbour} to current:{current}")
            if neighbour in visited_words_map:
                continue
            word_queue.enqueue(neighbour)
            visited_words_map[neighbour] = visited_words_map[current] + 1

        print("*** Current visited map:", [(key, value) for key, value in visited_words_map.items()])

    return -1


if __name__ == "__main__":
    # cab_node = Node("cab")
    # print([neighbour.get_value() for neighbour in cab_node.get_neighbours()])

    dictionary = {("cab", "dog"): {"dog", "cog", "cat", "cab", "cob"},
                  ("fit", "dog"): {"hit", "hot", "cot", "dog", "dot", "log", "cog"},
                  ("fool", "sage"): {"cool", "pool", "poll", "foil", "fail", "pole", "pope", "pale", "page", "sage", "sale", "fall"},
                  ("age", "age"): {"age", "ape", "axe", "ale"}
                  }

    for key, my_dict in dictionary.items():
        word_map = Pattern_To_Word_Map(my_dict)
        # print(word_map.get_all_patterns())
        seed = key[0]
        target = key[-1]
        print("\nTotal transformations:", word_ladder(seed, target, my_dict), "\n\n")
