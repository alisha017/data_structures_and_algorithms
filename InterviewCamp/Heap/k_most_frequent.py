import sys
from typing import List, Dict, Set


class Node:
    def __init__(self, word, value, index):
        self.__word = word
        self.__value = value
        self.__index = index
        self.__parent_index = Min_Heap.parent(index)
        self.__left_child_index = Min_Heap.left(index)
        self.__right_child_index = Min_Heap.right(index)

    def get_value(self):
        return self.__value

    def get_index(self):
        return self.__index

    def get_parent_index(self):
        return self.__parent_index

    def get_left_child_index(self):
        return self.__left_child_index

    def get_right_child_index(self):
        return self.__right_child_index

    def set_value(self, new_val):
        self.__value = new_val

    def set_index(self, new_index):
        self.__index = new_index

        self.__parent_index = Min_Heap.parent(self.__index)
        self.__left_child_index = Min_Heap.left(self.__index)
        self.__right_child_index = Min_Heap.right(self.__index)

    def get_word(self):
        return self.__word

    def set_word(self, new_word):
        self.__word = new_word

    def __lt__(self, other:'Node'):
        print(self.get_word(), self.get_value(), other.get_word(), other.get_value())
        if self.get_value() < other.get_value():
            print("self.get_value() < other.get_value()")
            return True
        elif self.get_value() > other.get_value():
            print("self.get_value() > other.get_value()")
            return False
        else:
            if self.get_word() >= other.get_word():
                print("self.get_value() = other.get_value(), self.get_word() >= other.get_word()")
                return False
            else:
                print("self.get_value() = other.get_value(), self.get_word() < other.get_word()")
                return True


class Min_Heap:
    def __init__(self, max_size):
        self.__array: List[Node] = [Node("", sys.maxsize, i) for i in range(max_size)]
        self.__size = 0

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    @staticmethod
    def left(index):
        return 2 * index + 1

    @staticmethod
    def right(index):
        return 2 * index + 2

    def is_empty(self):
        return True if self.__size == 0 else False

    def is_full(self):
        return True if self.__size == len(self.__array) else False

    def is_valid_index(self, index):
        return True if 0 <= index < len(self.__array) else False

    def insert(self, new_val: Node):
        if self.is_full():
            print("Heap Overflow. Cannot insert a new element...")
            return
            # raise Exception("Heap is full")

        new_node_index = self.__size
        new_val.set_index(new_node_index)
        self.__array[new_node_index] = new_val
        self.__size += 1

        self.propagate(new_node_index)

    def delete_min(self):
        if self.is_empty():
            print("Heap Underflow, cannot delete any element...")
            return
            # raise Exception("Heap is empty")

        self.__size -= 1
        self.__array[0], self.__array[self.__size] = self.__array[self.__size], self.__array[0]
        self.__array[0].set_index(0)
        self.__array[self.__size] = Node("", sys.maxsize, self.__size)
        if self.__size != 0:
            self.heapify(0)

    def delete_a_node(self, node: Node):
        to_del_index = node.get_index()

        if not self.is_valid_index(to_del_index):
            print("Invalid index...")
            return

        if self.is_empty():
            print("Heap Underflow, cannot delete any element...")
            return

        self.__size -= 1

        self.__array[to_del_index] = self.__array[self.__size]
        self.__array[self.__size] = Node("",
            sys.maxsize, self.__size)

        self.__array[to_del_index].set_index(to_del_index)

        if to_del_index != 0 and \
                self.__array[to_del_index] < self.__array[self.parent(to_del_index)]:
            self.propagate(to_del_index)
        else:
            self.heapify(to_del_index)

    def propagate(self, index):
        while self.__array[index] < self.__array[self.parent(index)] and index > 0:
            self.__array[self.parent(index)], self.__array[index] = self.__array[index], self.__array[
                self.parent(index)]

            self.__array[self.parent(index)].set_index(self.parent(index))
            self.__array[index].set_index(index)

            index = self.parent(index)

    def heapify(self, index):
        # print(f"current:{self.__array[index].get_value()} at {index}")
        left_child = self.__array[self.left(index)] if self.is_valid_index(self.left(index)) \
            else Node("", sys.maxsize, self.__size)
        right_child = self.__array[self.right(index)] if self.is_valid_index(self.right(index)) \
            else Node("", sys.maxsize, self.__size)
        # print(f"left_child:{left_child.get_value()}, right_child:{right_child.get_value()}, current:{self.__array[index].get_value()}")
        # print(f"left_child:{left_child.get_index()}, right_child:{right_child.get_index()}, current:{self.__array[index].get_index()}")

        min_element = min(min(left_child, self.__array[index]), right_child)
        min_index = index
        if min_element == left_child.get_value():
            min_index = self.left(index)
        elif min_element == right_child.get_value():
            min_index = self.right(index)

        if min_index != index:
            # swap max_index with current
            self.__array[min_index], self.__array[index] = self.__array[index], self.__array[min_index]
            self.__array[min_index].set_index(min_index)
            self.__array[index].set_index(index)
            # print(f"min element {min_element} at {min_index}")
            # print(f"heapifying {min_index} with element {self.__array[min_index].get_value()}")
            # print()
            self.heapify(min_index)

    def print_heap_array(self):
        print([(node.get_word(), node.get_value()) for node in self.__array[:self.__size]])

    def get_min(self):
        return self.__array[0]

    def get_size(self):
        return self.__size


def get_k_most_frequent(arr, k):
    my_heap = Min_Heap(k)
    # my_heap = Min_Heap(len(arr))
    hash_map: Dict[str,  Node] = {}
    in_heap:Set[Node] = set()

    first_node = Node(arr[0], 1, -1)
    in_heap.add(first_node)
    my_heap.insert(first_node)
    hash_map[arr[0]] = first_node

    for i in range(1, len(arr)):
        word = arr[i]
        print(f"Current word:{word}")
        if word in hash_map:
            print(f'\tword already in hash_map... new count:{hash_map[word].get_value()}')

            hash_map[word].set_value(hash_map[word].get_value() + 1)
            print(f'\t\tnew count:{hash_map[word].get_value()}')
            if hash_map[word] in in_heap:
                # print(f'\tword already in heap... heapifying...')
                my_heap.heapify(hash_map[word].get_index())
        else:
            print("\tnew word, adding to the hash map")
            hash_map[word] = Node(word, 1, -1)

            print(f'\tcurrent node:{(hash_map[word].get_word(), hash_map[word].get_value())},\n\tcurrent heap_min = '
                  f'{(my_heap.get_min().get_word(), my_heap.get_min().get_value())}')

        if hash_map[word] not in in_heap:
            if my_heap.get_min() < hash_map[word]:
                print(f"\t\t{my_heap.get_min().get_value()}, {my_heap.get_min().get_word()} < {hash_map[word].get_value()}, {hash_map[word].get_word()} --> inserting in the heap..")
                if my_heap.is_full():
                    in_heap.remove(my_heap.get_min())
                    my_heap.delete_min()
                my_heap.insert(hash_map[word])
                in_heap.add(hash_map[word])
        print("\ncurrent state heap:")
        my_heap.print_heap_array()
        print("In heap:", [(node.get_word(), node.get_value()) for node in in_heap])
        print("*"*100)

    result = []
    while not my_heap.is_empty():
        print("Current min:", my_heap.get_min().get_word())
        result.append(my_heap.get_min().get_word())
        my_heap.delete_min()

    return result


if __name__ == '__main__':
    words = ["i","love","leetcode","i","love","coding", "i", "mehul", "mehul", "alisha", "mehul", "i", "mehul", "leetcode", "love"]
    # print(get_k_most_frequent(words, 4))
    print(get_k_most_frequent(["i", "love", "leetcode", "i", "love", "coding"], 2))







