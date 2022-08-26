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
        self.__color:int = -1

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

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


class Graph:
    def __init__(self, nodes: List[Node] = None):
        self.__nodes_list = nodes if nodes is not None and len(nodes) > 0 else []

    def get_all_nodes(self):
        return self.__nodes_list

    def add_new_node(self, new_node):
        self.__nodes_list.append(new_node)


def dfs_visit_and_color(node:Node, color:int):
    # mark as visiting
    node.set_state(State.VISITING)

    # process node
    node.set_color(color)

    # run dfs_visit for neighbours
    for neighbour in node.get_neighbours():
        if neighbour.get_state() == State.UNVISITED:
            dfs_visit_and_color(neighbour, color)

    # mark the node as visited
    node.set_state(State.VISITED)


def dfs_color_connected_components(graph:Graph):
    color = 0
    for node in graph.get_all_nodes():
        if node.get_state() == State.UNVISITED:
            dfs_visit_and_color(node, color)
            color += 1


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
    node2.add_neighbours(node1)
    node3.add_neighbours(node4)
    node3.add_neighbours(node5)
    node3.add_neighbours(node1)
    node4.add_neighbours(node6)
    node4.add_neighbours(node3)
    node4.add_neighbours(node2)
    node5.add_neighbours(node6)
    node5.add_neighbours(node3)

    node7.add_neighbours(node8)
    node8.add_neighbours(node7)

    my_graph = Graph([node1, node2, node3, node4, node5, node6, node7, node8])

    dfs_color_connected_components(my_graph)

    print([(node.get_value(), node.get_color()) for node in my_graph.get_all_nodes()])
    # print(my_graph.get_all_nodes()[2].get_neighbours())

    # 2 and 4 will show not present because while traversing for 9, the node's state changed to visited
    # print(dfs(my_graph, 9))
    # print(dfs(my_graph, 2))
    # print(dfs(my_graph, 4))






