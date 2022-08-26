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
        self.__longest_path = 0

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

    def get_longest_path(self):
        return self.__longest_path

    def set_longest_path(self, longest_path):
        self.__longest_path = longest_path


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


def topological_sort(node: Node):
    stack: List[Node] = []
    dfs_visit(node, stack)
    return stack


def get_max_diameter(start: Node):
    topological_sorted_stack = topological_sort(start)

    diameter = 0

    while len(topological_sorted_stack) > 0:
        current_node: Node = topological_sorted_stack.pop()
        diameter = max(diameter, current_node.get_longest_path())
        for neighbour in current_node.get_neighbours():
            if current_node.get_longest_path() + 1 > neighbour.get_longest_path():
                neighbour.set_longest_path(current_node.get_longest_path() + 1)

    return diameter


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
    diameter_of_graph = get_max_diameter(node1)

    print(f"Diameter of the graph:{diameter_of_graph}")

    node_a = Node("a")
    node_b = Node("b")
    node_c = Node("c")
    node_d = Node("d")
    node_e = Node("e")
    node_f = Node("f")
    node_g = Node("g")
    node_h = Node("h")
    node_i = Node("i")

    node_a.add_neighbours(node_b)
    node_a.add_neighbours(node_d)

    node_b.add_neighbours(node_c)
    node_b.add_neighbours(node_f)

    node_f.add_neighbours(node_h)
    node_f.add_neighbours(node_g)

    node_h.add_neighbours(node_i)

    node_d.add_neighbours(node_e)

    node_e.add_neighbours(node_i)

    another_graph = Graph([node_a, node_b, node_c, node_d, node_e, node_f, node_g, node_h, node_i])
    diameter_of_graph = get_max_diameter(node_a)

    print(f"Diameter of the graph:{diameter_of_graph}")
