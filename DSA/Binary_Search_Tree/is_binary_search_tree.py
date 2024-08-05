import sys
from typing import Optional


class TreeNode:
    def __init__(self, value: int, right: Optional['TreeNode'] = None,
                 left: Optional['TreeNode'] = None):
        self._value: int = value
        self.__right_node: Optional['TreeNode'] = right
        self.__left_node: Optional['TreeNode'] = left
        self.__visited: bool = False

    def get_node_value(self):
        return self._value

    def get_right_node(self):
        return self.__right_node

    def get_left_node(self):
        return self.__left_node

    def is_visited(self):
        return self.__visited

    def set_node_value(self, val: int):
        self._value = val

    def set_right_node(self, new_right: 'TreeNode'):
        self.__right_node = new_right

    def set_left_node(self, new_left: 'TreeNode'):
        self.__left_node = new_left

    def set_visited(self, new_visited):
        self.__visited = new_visited


class MinMaxPair:
    def __init__(self, min= sys.maxsize, max= -sys.maxsize):
        self.__min = min
        self.__max = max

    def get_min(self):
        return self.__min

    def get_max(self):
        return self.__max


def inorder_tree_traversal(root: TreeNode):
    stack = []
    node = root
    stack.append(node)
    inorder_list = []

    while len(stack) > 0:
        current_node = stack.pop(-1)
        if current_node.is_visited() is True:
            inorder_list.append(current_node.get_node_value())
        else:
            current_node.set_visited(True)
            if current_node.get_right_node() is not None:
                stack.append(current_node.get_right_node())
            stack.append(current_node)
            if current_node.get_left_node() is not None:
                stack.append(current_node.get_left_node())
    return inorder_list


def is_binary_search_tree(node: TreeNode):
    print("****"*30)
    if node is None:
        return MinMaxPair()
    print(f"Current node: {node.get_node_value()}")
    left = is_binary_search_tree(node.get_left_node())
    print(f"Left minmaxpair: {(left.get_min(), left.get_max()) if left is not None else left}")
    right = is_binary_search_tree(node.get_right_node())
    print(f"Right minmaxpair: {(right.get_min(), right.get_max()) if right is not None else right}")

    if left is None or right is None:
        return None

    if left.get_max() > node.get_node_value() or right.get_min() < node.get_node_value():
        return None

    min_val = node.get_node_value() if node.get_left_node() is None else left.get_min()
    max_val = node.get_node_value() if node.get_right_node() is None else right.get_max()
    print(f"min_val: {min_val}, max_val: {max_val}")
    print("----"*30)
    return MinMaxPair(min_val, max_val)


if __name__ == "__main__":
    root = TreeNode(4)
    node1 = TreeNode(2)
    node2 = TreeNode(6)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    node5 = TreeNode(5)
    node6 = TreeNode(7)
    root.set_right_node(node2)
    root.set_left_node(node1)
    node1.set_left_node(node3)
    node1.set_right_node(node4)
    node2.set_left_node(node5)
    node2.set_right_node(node6)

    print(inorder_tree_traversal(root))
    print(is_binary_search_tree(root))

    node4.set_left_node(TreeNode(8))
    print(inorder_tree_traversal(root))
    print(is_binary_search_tree(root))

