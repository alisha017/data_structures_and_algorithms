from enum import Enum

from typing import List, Dict, Any


class State(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Node:
    def __init__(self, value, neighbours: List['Node'] = None):
        self.__neighbours: List['Node'] = neighbours if neighbours is not None and len(neighbours) > 0 else []
        self.__value = value
        self.__state: State = State.UNVISITED

    def get_neighbours(self):
        return self.__neighbours

    def get_value(self):
        return self.__value

    def get_state(self):
        return self.__state

    def add_neighbours(self, new_neighbour):
        self.__neighbours.append(new_neighbour)

    def set_state(self, new_state):
        self.__state = new_state

    def set_value(self, new_value):
        self.__value = new_value


class Graph:
    def __init__(self, nodes: List[Node] = None):
        self.__nodes_list = nodes if nodes is not None and len(nodes) > 0 else []

    def get_all_nodes(self):
        return self.__nodes_list

    def add_new_node(self, new_node):
        self.__nodes_list.append(new_node)


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


def bfs_visit(graph: Graph, start_node: Node, target: int) -> bool:
    nodes_queue: Queue = Queue(len(graph.get_all_nodes()))

    nodes_queue.enqueue(start_node)
    start_node.set_state(State.VISITING)
    while nodes_queue.is_empty() is False:
        current: Node = nodes_queue.dequeue()
        if current.get_value() == target:
            return True
        for node in current.get_neighbours():
            nodes_queue.enqueue(node)
            node.set_state(State.VISITING)

        current.set_state(State.VISITED)

    return False


def bfs_print_level_using_marker(graph: Graph, start_node: Node) -> str:
    nodes_queue: Queue = Queue(len(graph.get_all_nodes()))

    nodes_queue.enqueue(start_node)
    start_node.set_state(State.VISITING)

    result = ""
    marker = Node(0)
    nodes_queue.enqueue(marker)

    while nodes_queue.is_empty() is False:
        current: Node = nodes_queue.dequeue()
        # print(f"Current: {current.get_value()}")
        if current == marker:
            # print("hello i am at a marker\n")
            if nodes_queue.is_empty() is False:
                # print("inserting a marker...")
                nodes_queue.enqueue(marker)
            result += "\n"
            continue

        result += (str(current.get_value()) + "-")
        # print(f"finding neighbours for {current.get_value()}")
        for node in current.get_neighbours():
            # print(f"\tCurrent neighbour:{node.get_value()}")
            if node.get_state() == State.UNVISITED:
                nodes_queue.enqueue(node)
                node.set_state(State.VISITING)

        current.set_state(State.VISITED)
    return result


def bfs_print_level_using_2_queues(graph: Graph, start_node: Node):
    current_queue: Queue = Queue(len(graph.get_all_nodes()))
    next_level_queue: Queue = Queue(len(graph.get_all_nodes()))

    current_queue.enqueue(start_node)
    start_node.set_state(State.VISITING)

    while current_queue.is_empty() is False:
        current: Node = current_queue.dequeue()
        print(f"{current.get_value()}")

        # print(f"finding neighbours for {current.get_value()}")
        for node in current.get_neighbours():
            # print(f"\tCurrent neighbour:{node.get_value()}")
            if node.get_state() == State.UNVISITED:
                next_level_queue.enqueue(node)
                node.set_state(State.VISITING)

        if current_queue.is_empty():
            print("************")
            current_queue = next_level_queue
            next_level_queue = Queue(len(graph.get_all_nodes()))

        current.set_state(State.VISITED)


def bfs(graph: Graph, target: int) -> bool:
    for node in graph.get_all_nodes():
        if node.get_state() == State.UNVISITED and bfs_visit(graph, node, target):
            return True

    return False


def level_order_print_graph(graph: Graph, way: int = 0) -> None:
    for node in graph.get_all_nodes():
        if node.get_state() == State.UNVISITED:
            print("Island:")
            if way == 0:
                print(bfs_print_level_using_marker(graph, node))
            elif way == 1:
                bfs_print_level_using_2_queues(graph, node)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node7 = Node(7)
    node8 = Node(8)

    node1.add_neighbours(node2)
    node1.add_neighbours(node3)
    node2.add_neighbours(node4)
    node3.add_neighbours(node4)
    node3.add_neighbours(node5)
    node4.add_neighbours(node6)
    node5.add_neighbours(node6)

    node7.add_neighbours(node8)

    my_graph = Graph([node1, node2, node3, node4, node5, node6, node7, node8])

    # print(bfs(my_graph, 3))
    # print(bfs(my_graph, 5))
    # print(bfs(my_graph, 39))
    level_order_print_graph(my_graph)
