import sys
from typing import List
# from functools import cmp_to_key


class Point:
    def __init__(self, y_height: int, x_coord: int, is_start_point: bool):
        self.__y_height = y_height
        self.__x_coord = x_coord
        self.__is_start_point = is_start_point
    def get_x_coord(self):
        return self.__x_coord

    def get_is_start_point(self):
        return self.__is_start_point

    def get_y_height(self):
        return self.__y_height

    def __lt__(self, other):
        if self.__x_coord == other.get_x_coord():
            return 1 if self.__is_start_point is True else -1
        return 1 if self.__y_height > other.__y_height else -1


class Building:
    def __init__(self, x_start: int, x_end: int, y_height: int):
        self.__x_start = x_start
        self.__x_end = x_end
        self.__y_height = y_height

    def get_x_start_coord(self):
        return self.__x_start

    def get_x_end_coord(self):
        return self.__x_end

    def get_y_height_coord(self):
        return self.__y_height


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
            return None

        return self.__array[0].get_value()

    def insert(self, new):
        if self.__array[-1].get_value() != -sys.maxsize:
            raise HeapOverflow

        new_element_index = self.__size
        new_node = Node(new, new_element_index)
        self.__array[self.__size] = new_node
        self.__size += 1

        self.propagate_up(new_element_index)
        return new_node

    def delete_max(self):
        if self.__size == 0:
            raise HeapUnderflow

        self.__size -= 1

        # replacing the max element with the rightmost (the last) element
        self.__array[0] = self.__array[self.__size - 1]
        self.__array[self.__size - 1] = Node(-sys.maxsize, self.__size - 1)
        self.__array[0].set_index(0)
        self.heapify(0)

    def delete_a_node(self, node: Node):
        index = node.get_index()
        print(f"index: {index}, self.__size: {self.__size}")
        if self.is_valid(index) is False:
            raise Exception("Not a valid index")

        self.__array[index] = self.__array[self.__size - 1]
        self.__array[self.__size - 1] = Node(-sys.maxsize, self.__size - 1)
        self.__array[index].set_index(index)

        self.__size -= 1
        if index != 0 and self.__array[self.parent(index)].get_value() < self.__array[index].get_value():
            self.propagate_up(index)
        else:
            if self.__size == 0:
                return
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

    def heapify(self, index):
        left_child = self.__array[self.left(index)] \
            if self.is_valid(self.left(index)) is True else Node(-sys.maxsize, self.__size)
        right_child = self.__array[self.right(index)] \
            if self.is_valid(self.right(index)) is True else Node(-sys.maxsize, self.__size)

        print(f"left_child:{left_child.get_value()}, right_child:{right_child.get_value()}")
        max_element = max(max(self.__array[index].get_value(), left_child.get_value()), right_child.get_value())

        # if an element is repeating, this method will only take the relevant index instead
        max_index = index
        if max_element == left_child.get_value():
            max_index = self.left(index)
        elif max_element == right_child.get_value():
            max_index = self.right(index)
        # print(f"max element: {max_element}, max_index: {max_index}")

        if max_index != index:
            self.__array[index], self.__array[max_index] = self.__array[max_index], self.__array[index]
            self.__array[index].set_index(index)
            self.__array[max_index].set_index(max_index)
            print("heapifying...")
            print(self.parent(max_index), self.__array[self.parent(max_index)].get_value(), self.__array[max_index].get_value())
            self.heapify(max_index)

    def print_heap_array(self):
        print([node.get_value() for node in self.__array[:self.__size]])


class Building_Map:
    def __init__(self):
        self.__building_dictionary = {}
        self.__max_heap = Max_Heap(100)

    def add(self, building_point: Point):
        new_node = self.__max_heap.insert(building_point.get_y_height())
        if new_node.get_value() in self.__building_dictionary:
            self.__building_dictionary[new_node.get_value()].append(new_node)
        else:
            self.__building_dictionary[new_node.get_value()] = [new_node]

    def remove(self, building_point: Point):
        if building_point.get_y_height() not in self.__building_dictionary:
            return

        to_delete: List[Node] = self.__building_dictionary[building_point.get_y_height()]
        self.__max_heap.delete_a_node(to_delete[-1])
        print(f"To delete: {to_delete[-1].get_value()}, {to_delete[-1].get_index()}")
        del to_delete[-1]

        print(f"Current heap status:")
        self.__max_heap.print_heap_array()
        print("Building word_map:", self.__building_dictionary)

    def get_max(self):
        return self.__max_heap.get_max()


def draw_skyline(buildings: List[Building]):
    points_list: List[Point] = []
    for building in buildings:
        points_list.append(Point(building.get_y_height_coord(), building.get_x_start_coord(), True))
        points_list.append(Point(building.get_y_height_coord(), building.get_x_end_coord(), False))

    sorted_points = sorted(points_list, key=lambda point: point.get_x_coord())
    print([(point.get_y_height(), point.get_x_coord(), point.get_is_start_point()) for point in sorted_points])

    building_map = Building_Map()

    current_max = 0
    result = []
    for point in sorted_points:
        if point.get_is_start_point() is True:
            if point.get_y_height() > current_max:
                current_max = point.get_y_height()
                result.append((point.get_x_coord(), point.get_y_height()))
            building_map.add(point)
        else:
            building_map.remove(point)
            if current_max == point.get_y_height():
                result.append((point.get_x_coord(), point.get_y_height()))
                current_max = building_map.get_max()
                if current_max is not None:
                    result.append((point.get_x_coord(), current_max))

        print(f"Point( {point.get_y_height()}, {point.get_x_coord()}, {point.get_is_start_point()}) : {result}")

    return result


if __name__ == '__main__':
    buildings_list: List[Building] = []

    for coords in [(0,2,9), (1,6,5), (4,7,14), (5,8,8)]:
        # (9, 0, True), (5, 1, True), (9, 2, False), (14, 4, True), (8, 5, True), (5, 6, False),
        # (14, 7, False), (8, 8, False)]:
        buildings_list.append(Building(*coords))

    print(draw_skyline(buildings_list))
