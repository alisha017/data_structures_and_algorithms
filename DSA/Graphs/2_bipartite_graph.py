from enum import Enum

from typing import List, Dict, Any, Optional


class State(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Node:
    def __init__(self, value, neighbours: List['Node'] = None):
        self.__neighbours: List['Node'] = neighbours if neighbours is not None and len(neighbours) > 0 else []
        self.__value = value
        self.__state: State = State.UNVISITED
        self.__level = -1

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

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level


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


def bfs_visit_check_and_create_bipartite(graph: Graph, start_node: Node):
    nodes_queue: Queue = Queue(len(graph.get_all_nodes()))
    odd_nodes: List[Node] = []
    even_nodes: List[Node] = []

    nodes_queue.enqueue(start_node)

    start_node.set_level(0)
    start_node.set_state(State.VISITING)

    while nodes_queue.is_empty() is False:
        current: Node = nodes_queue.dequeue()
        # adding to the even and odd nodes list
        if current.get_level() % 2 == 0:
            even_nodes.append(current)
        else:
            odd_nodes.append(current)

        # updating the level of neighbours and checking if the graph is bipartite
        for neighbour in current.get_neighbours():
            if neighbour.get_state() == State.UNVISITED:
                nodes_queue.enqueue(neighbour)
                neighbour.set_state(State.VISITING)
                neighbour.set_level(current.get_level() + 1)
            elif neighbour.get_state() == State.VISITING:
                if neighbour.get_level() == current.get_level():
                    return None

        current.set_state(State.VISITED)

    return odd_nodes, even_nodes


def bipartite(graph: Graph):
    odd_nodes: List[Node] = []
    even_nodes: List[Node] = []

    for node in graph.get_all_nodes():
        if node.get_state() == State.UNVISITED:
            groups = bfs_visit_check_and_create_bipartite(graph, node)
            if groups is None:
                return None
            odd_nodes.extend(groups[0])
            even_nodes.extend(groups[1])

    return odd_nodes, even_nodes


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.add_neighbours(node2)
    node1.add_neighbours(node4)
    node2.add_neighbours(node1)
    node2.add_neighbours(node3)
    node3.add_neighbours(node2)
    node3.add_neighbours(node4)
    node4.add_neighbours(node1)
    node4.add_neighbours(node3)

    my_graph = Graph([node1, node2, node3, node4])
    result = bipartite(my_graph)

    if result is None:
        print("Not a bipartite graph")
    else:
        print(f"Odd nodes: {[node.get_value() for node in result[0]]}")
        print(f"Even nodes: {[node.get_value() for node in result[1]]}")

    a_node = Node("a")
    b_node = Node("b")
    c_node = Node("c")
    d_node = Node("d")

    a_node.add_neighbours(b_node)
    a_node.add_neighbours(c_node)
    a_node.add_neighbours(d_node)
    b_node.add_neighbours(c_node)
    b_node.add_neighbours(a_node)
    c_node.add_neighbours(a_node)
    c_node.add_neighbours(b_node)
    c_node.add_neighbours(d_node)
    d_node.add_neighbours(a_node)
    d_node.add_neighbours(c_node)

    my_graph = Graph([a_node, b_node, c_node, d_node])
    result = bipartite(my_graph)

    if result is None:
        print("Not a bipartite graph")
    else:
        print(f"Odd nodes: {[node.get_value() for node in result[0]]}")
        print(f"Even nodes: {[node.get_value() for node in result[1]]}")
