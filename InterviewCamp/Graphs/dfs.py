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


def dfs_visit(node:Node, target:int):
    # mark as visiting
    node.set_state(State.VISITING)

    # process node
    if node.get_value() == target:
        return True

    # run dfs_visit for neighbours
    for neighbour in node.get_neighbours():
        if neighbour.get_state() == State.UNVISITED and dfs_visit(neighbour, target) is True:
            return True

    # mark the node as visited
    node.set_state(State.VISITED)

    return False


def dfs(graph:Graph, target:int):
    for node in graph.get_all_nodes():
        if node.get_state() == State.UNVISITED and dfs_visit(node, target) is True:
            return True

    return False


def dfs_copy(node:Node, old_new_graph_map:Dict[Node, Node]):
    node.set_state(State.VISITING)
    for neighbour in node.get_neighbours():
        if neighbour not in old_new_graph_map:
            old_new_graph_map[neighbour] = Node(neighbour.get_value())

            # adding the neighbour as the neighbour of the copied root
        neighbour_copy = old_new_graph_map[neighbour]

        root_copy = old_new_graph_map[node]
        root_copy.add_neighbours(neighbour_copy)

        old_new_graph_map[neighbour].get_neighbours()
        if neighbour.get_state() == State.UNVISITED:
            dfs_copy(neighbour, old_new_graph_map)

    node.set_state(State.VISITED)


def clone_graph(root:Node):
    if root is None:
        return None

    old_new_graph_map = {root:Node(root.get_value())}
    dfs_copy(root, old_new_graph_map)
    return old_new_graph_map


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

    # print([(node.get_value(), node) for node in my_graph.get_all_nodes()])
    # print(my_graph.get_all_nodes()[2].get_neighbours())

    # 2 and 4 will show not present because while traversing for 9, the node's state changed to visited
    # print(dfs(my_graph, 9))
    # print(dfs(my_graph, 2))
    # print(dfs(my_graph, 4))

    result: Dict[Node, Node] = clone_graph(node1)

    for key, value in result.items():
        print(f"original val:{key.get_value()}, clone_val:{value.get_value()}")
        print(f"\tNeighbours: original:{[neighbour.get_value() for neighbour in key.get_neighbours()]}")
        print(f"\tNeighbours: clone:{[neighbour.get_value() for neighbour in value.get_neighbours()]}")





