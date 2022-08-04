import sys
from typing import List, Optional


class HeapUnderflow(Exception):
    pass


class HeapOverflow(Exception):
    pass


class Node:
    def __init__(self, value, index):
        self.__value = value
        self.__index = index
        self.__parent_index: int = Max_Heap.parent(self.__index)
        self.__left_child_index: int = Max_Heap.left(self.__index)
        self.__right_child_index: int = Max_Heap.right(self.__index)

    def get_value(self):
        return self.__value

    def get_parent_index(self):
        return self.__parent_index

    def get_left_child_index(self):
        return self.__left_child_index

    def get_right_child_index(self):
        return self.__right_child_index

    def get_index(self):
        return self.__index

    def set_index(self, new_index):
        self.__index = new_index
        self.__parent_index: int = Max_Heap.parent(self.__index)
        self.__left_child_index: int = Max_Heap.left(self.__index)
        self.__right_child_index: int = Max_Heap.right(self.__index)


class Max_Heap:
    def __init__(self, capacity):
        self.__array: List[Node] = [Node(-sys.maxsize, i) for i in range(capacity)]
        self.__size = 0

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    @staticmethod
    def left(index):
        return (2 * index) + 1

    @staticmethod
    def right(index):
        return (2 * index) + 2

    def is_valid(self, index):
        return 0 <= index < self.__size

    def get_max(self):
        if self.__size == 0:
            raise HeapUnderflow

        return self.__array[0].get_value()

    def insert(self, new):
        if self.__array[-1].get_value() != -sys.maxsize:
            raise HeapOverflow

        new_element_index = self.__size
        self.__array[self.__size] = Node(new, new_element_index)
        self.__size += 1

        self.propagate_up(new_element_index)

    def delete_max(self):
        if self.__size == 0:
            raise HeapUnderflow

        self.__size -= 1

        # replacing the max element with the rightmost (the last) element
        self.__array[0] = self.__array[self.__size-1]
        self.__array[self.__size - 1] = Node(-sys.maxsize, self.__size - 1)
        self.__array[0].set_index(0)
        self.heapify(0)

    def delete_a_node(self, node: Node):
        index = node.get_index()
        if self.is_valid(index) is False:
            raise Exception("Not a valid index")

        self.__array[index] = self.__array[self.__size-1]
        self.__array[self.__size - 1] = Node(-sys.maxsize, self.__size - 1)

        self.__size -= 1
        if index != 0 and self.__array[self.parent(index)] < self.__array[index]:
            self.propagate_up(index)
        else:
            self.heapify(index)

    def propagate_up(self, index):
        print("propagating up...")
        print(self.parent(index), self.__array[self.parent(index)].get_value(), self.__array[index].get_value())
        while self.__array[self.parent(index)].get_value() < self.__array[index].get_value() and index > 0:
            self.__array[self.parent(index)], self.__array[index] = self.__array[index], self.__array[
                self.parent(index)]

            self.__array[self.parent(index)].set_index(self.parent(index))
            self.__array[index].set_index(index)

            index = self.parent(index)

    # time complexity - O(n)
    def heapify(self, index):
        left_child = self.__array[self.left(index)] \
            if self.is_valid(self.left(index)) is True else Node(-sys.maxsize, self.__size)
        right_child = self.__array[self.right(index)] \
            if self.is_valid(self.right(index)) is True else Node(-sys.maxsize, self.__size)

        print(f"left_child:{left_child}, right_child:{right_child}")
        max_element = max(max(self.__array[index].get_value(), left_child.get_value()), right_child.get_value())
        print(f"max element: {max_element}")

        # if an element is repeating, this method will only take the relevant index instead
        max_index = index
        if max_element == left_child.get_value():
            max_index = self.left(index)
        elif max_element == right_child.get_value():
            max_index = self.right(index)

        print(f"max_index: {max_index}")
        if max_index != index:
            self.__array[index], self.__array[max_index] = self.__array[max_index], self.__array[index]
            self.__array[index].set_index(index)
            self.__array[max_index].set_index(max_index)
            self.heapify(max_index)

    def print_heap_array(self):
        print([node.get_value() for node in self.__array[:self.__size]])


if __name__ == '__main__':
    my_heap = Max_Heap(8)

    for num in [10, 2, 8, 4, 6, 3, 1]:
        print(f"Inserting {num}")
        my_heap.insert(num)

    my_heap.print_heap_array()
    my_heap.insert(9)
    my_heap.print_heap_array()
    print(my_heap.parent(1), my_heap.left(1), my_heap.right(1))

    my_heap.delete_max()
    my_heap.print_heap_array()
