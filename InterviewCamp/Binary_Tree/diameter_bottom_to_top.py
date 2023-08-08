from typing import Optional


class TreeNode:
    def __init__(self, value: int, right: Optional['TreeNode'] = None, left: Optional['TreeNode'] = None):
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


def get_diameter_of_tree(node: TreeNode):
    if node is None:
        return 0, 0

    left_height, left_max_diameter = get_diameter_of_tree(node.get_left_node())
    right_height, right_max_diameter = get_diameter_of_tree(node.get_right_node())

    diameter = left_height + right_height + 1
    max_diameter = max(max(left_max_diameter, right_max_diameter), diameter)

    return 1+max(left_height, right_height), max_diameter


if __name__ == "__main__":
    root = TreeNode(4)
    node1 = TreeNode(2)
    node2 = TreeNode(6)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    node5 = TreeNode(5)
    node6 = TreeNode(7)
    node7 = TreeNode(8)
    root.set_right_node(node2)
    root.set_left_node(node1)
    node1.set_left_node(node3)
    node1.set_right_node(node4)
    node2.set_left_node(node5)
    node2.set_right_node(node6)
    node4.set_left_node(node7)
    print(inorder_tree_traversal(root))
    print(get_diameter_of_tree(root))

    root = TreeNode(4)
    # node1 = TreeNode(2)
    # node2 = TreeNode(6)
    # node3 = TreeNode(1)
    # node4 = TreeNode(3)
    # node5 = TreeNode(5)
    # node6 = TreeNode(7)
    # node7 = TreeNode(8)

    # root.set_left_node(node1)
    # root.set_right_node(node2)
    # # node1.set_left_node(node3)
    # # node1.set_right_node(node4)
    # node2.set_left_node(node5)
    # node2.set_right_node(node6)
    # node5.set_left_node(node7)
    print(inorder_tree_traversal(root))
    print(get_diameter_of_tree(root))
    print(get_diameter_of_tree(None))


