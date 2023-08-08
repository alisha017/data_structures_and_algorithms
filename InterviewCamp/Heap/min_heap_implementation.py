import sys
from typing import List


class Node:
    def __init__(self, value, index):
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


class Min_Heap:
    def __init__(self, max_size):
        self.__array: List[Node] = [Node(sys.maxsize, i) for i in range(max_size)]
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



    def is_valid_index(self, index):
        return True if 0 <= index < len(self.__array) else False

    def insert(self, new_val: int):
        if self.is_full():
            print("Heap Overflow. Cannot insert a new element...")
            return
            # raise Exception("Heap is full")

        new_node_index = self.__size
        self.__array[new_node_index] = Node(new_val, new_node_index)
        self.__size += 1

        self.propagate(new_node_index)

    def delete_max(self):
        if self.is_empty():
            print("Heap Underflow, cannot delete any element...")
            return
            # raise Exception("Heap is empty")

        self.__size -= 1
        self.__array[0], self.__array[self.__size] = self.__array[self.__size], self.__array[0]
        self.__array[0].set_index(0)
        self.__array[self.__size] = Node(sys.maxsize, self.__size)
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
        self.__array[self.__size] = Node(
            sys.maxsize, self.__size)

        self.__array[to_del_index].set_index(to_del_index)

        if to_del_index != 0 and \
                self.__array[self.parent(to_del_index)].get_value() > self.__array[to_del_index].get_value():
            self.propagate(to_del_index)
        else:
            self.heapify(to_del_index)

    def propagate(self, index):
        while self.__array[self.parent(index)].get_value() > self.__array[index].get_value() and index > 0:
            self.__array[self.parent(index)], self.__array[index] = self.__array[index], self.__array[
                self.parent(index)]

            self.__array[self.parent(index)].set_index(self.parent(index))
            self.__array[index].set_index(index)

            index = self.parent(index)

    def heapify(self, index):
        print(f"current:{self.__array[index].get_value()} at {index}")
        left_child = self.__array[self.left(index)] if self.is_valid_index(self.left(index)) else Node(sys.maxsize,
                                                                                                       self.__size)
        right_child = self.__array[self.right(index)] if self.is_valid_index(self.right(index)) else Node(sys.maxsize,
                                                                                                          self.__size)
        print(
            f"left_child:{left_child.get_value()}, right_child:{right_child.get_value()}, current:{self.__array[index].get_value()}")
        print(
            f"left_child:{left_child.get_index()}, right_child:{right_child.get_index()}, current:{self.__array[index].get_index()}")

        min_element = min(min(left_child.get_value(), self.__array[index].get_value()), right_child.get_value())
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
            print(f"min element {min_element} at {min_index}")
            print(f"heapifying {min_index} with element {self.__array[min_index].get_value()}")
            print()
            self.heapify(min_index)

    def print_heap_array(self):
        print([node.get_value() for node in self.__array[:self.__size]])

    def get_min(self):
        return self.__array[0]


if __name__ == '__main__':
    my_heap = Min_Heap(10)

    for num in [6, 3, 6, 6, 2, 2]:
        print(f"Inserting {num}")
        my_heap.insert(num)

    my_heap.print_heap_array()
    my_heap.insert(4)
    my_heap.print_heap_array()
    print(my_heap.parent(3), my_heap.left(3), my_heap.right(3))
    print(my_heap.parent(4), my_heap.left(4), my_heap.right(4))

    my_heap.delete_max()
    my_heap.print_heap_array()


