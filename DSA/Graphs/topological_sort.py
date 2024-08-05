from enum import Enum
from typing import List


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


def dfs_visit(node: Node, stack: List[Node]):
    # mark as visiting
    node.set_state(State.VISITING)

    # run dfs_visit for neighbours
    for neighbour in node.get_neighbours():
        if neighbour.get_state() == State.UNVISITED:
            dfs_visit(neighbour, stack)

    # mark the node as visited
    node.set_state(State.VISITED)

    # push to the stack
    stack.append(node)


def topological_sort_dag(graph: Graph):
    stack: List[Node] = []

    for node in graph.get_all_nodes():
        if node.get_state() == State.UNVISITED:
            dfs_visit(node, stack)

    return stack


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.add_neighbours(node2)
    node1.add_neighbours(node3)
    node2.add_neighbours(node4)
    node3.add_neighbours(node4)
    node2.add_neighbours(node5)
    node4.add_neighbours(node5)

    my_graph = Graph([node1, node2, node3, node4, node5])
    sorted_nodes = topological_sort_dag(my_graph)

    print([node.get_value() for node in sorted_nodes[::-1]])
