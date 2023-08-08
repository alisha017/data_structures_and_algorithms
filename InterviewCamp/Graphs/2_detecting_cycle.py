from enum import Enum

from typing import List, Dict


class State(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Node:
    def __init__(self, value, neighbours:List['Node'] = None):
        self.__neighbours: List['Node'] = neighbours if neighbours is not None and len(neighbours)>0 else []
        self.__value = value
        self.__state:State = State.UNVISITED

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


def dfs_visit_check_cycle(node:Node):
    # mark as visiting
    node.set_state(State.VISITING)
    print(f"Visiting: {node.get_value()}")

    # run dfs_visit for neighbours
    for neighbour in node.get_neighbours():
        if neighbour.get_state() == State.UNVISITED:
            if dfs_visit_check_cycle(neighbour) is True:
                return True
        elif neighbour.get_state() == State.VISITING:
            print(f"Visiting again, found a cycle from : {neighbour.get_value()}")
            return True

    # mark the node as visited
    node.set_state(State.VISITED)

    return False


def dfs_detect_cycle(graph:Graph):
    for node in graph.get_all_nodes():
        if node.get_state() == State.UNVISITED and dfs_visit_check_cycle(node) is True:
            return True

    return False


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.add_neighbours(node2)
    node1.add_neighbours(node3)
    node2.add_neighbours(node4)
    node3.add_neighbours(node4)
    node3.add_neighbours(node5)
    node4.add_neighbours(node6)
    node5.add_neighbours(node6)

    my_graph = Graph([node1, node2, node3, node4, node5, node6])

    print(f"Does the graph have cycles?:{dfs_detect_cycle(my_graph)}")

    a_node = Node("a")
    b_node = Node("b")
    c_node = Node("c")
    d_node = Node("d")
    e_node = Node("e")
    f_node = Node("f")

    a_node.add_neighbours(b_node)
    a_node.add_neighbours(e_node)
    b_node.add_neighbours(c_node)
    c_node.add_neighbours(d_node)
    d_node.add_neighbours(b_node)
    d_node.add_neighbours(f_node)
    e_node.add_neighbours(d_node)

    cyclic_graph = Graph([a_node, b_node, c_node, d_node, e_node, f_node])
    print(f"Does the graph have cycles?:{dfs_detect_cycle(cyclic_graph)}")






