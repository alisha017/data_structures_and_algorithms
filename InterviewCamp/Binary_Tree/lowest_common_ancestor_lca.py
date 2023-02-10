from typing import Optional, List


class TreeNode:
    def __init__(self, value: int, right: Optional['TreeNode'] = None,
                 left: Optional['TreeNode'] = None, parent: Optional['TreeNode'] = None):
        self._value: int = value
        self.__right_node: Optional['TreeNode'] = right
        self.__left_node: Optional['TreeNode'] = left
        self.__parent = parent
        self.__visited: bool = False

    def get_node_value(self):
        return self._value

    def get_right_node(self):
        return self.__right_node

    def get_left_node(self):
        return self.__left_node

    def is_visited(self):
        return self.__visited

    def get_parent(self):
        return self.__parent

    def set_node_value(self, val: int):
        self._value = val

    def set_right_node(self, new_right: 'TreeNode'):
        self.__right_node = new_right
        new_right.set_parent(self)

    def set_left_node(self, new_left: 'TreeNode'):
        self.__left_node = new_left
        new_left.set_parent(self)

    def set_visited(self, new_visited):
        self.__visited = new_visited

    def set_parent(self, new_parent: 'TreeNode'):
        self.__parent = new_parent


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


def get_depth_using_parent(node: TreeNode):
    depth = -1
    while node is not None:
        depth += 1
        node = node.get_parent()

    return depth


def lowest_common_ancestor_with_parent_info(a: TreeNode, b: TreeNode):
    if a is None or b is None:
        return None

    a_ptr = a
    b_ptr = b
    # find depth of both nodes
    a_depth = get_depth_using_parent(a_ptr)
    b_depth = get_depth_using_parent(b_ptr)

    # get depth difference and find which node is deeper and which one is shallow
    depth_diff = a_depth - b_depth

    deeper, shallow = (a_ptr, b_ptr) if depth_diff > 0 else (b_ptr, a_ptr)

    # move the pointer to the deeper node to the shallow node level
    for i in range(abs(depth_diff)):
        deeper = deeper.get_parent()

    # iterate up until the shallow node and deep node become equal

    if shallow == deeper:
        return deeper
    else:
        while deeper.get_parent() != shallow.get_parent():
            deeper = deeper.get_parent()
            shallow = shallow.get_parent()

        return deeper.get_parent()


def lowest_common_ancestor_without_parent_info(current_node: TreeNode, a: TreeNode, b: TreeNode):
    if current_node is None:
        return None
    if current_node == a or current_node == b:
        return current_node

    left_lca = lowest_common_ancestor_without_parent_info(current_node.get_left_node(), a, b)
    print(f"current node:{current_node.get_node_value()}, left lca = {left_lca.get_node_value() if left_lca is not None else None}")
    right_lca = lowest_common_ancestor_without_parent_info(current_node.get_right_node(), a, b)
    print(f"current node:{current_node.get_node_value()}, right lca = {right_lca.get_node_value() if right_lca is not None else None}")

    # when left lca and right lca both are not none, then that node is the common ancestor (current_node)
    # meaning on either sides of the lca
    if left_lca is not None and right_lca is not None:
        return current_node
    # if either left lca or right lca are not nulls,
    # means that the deeper node is a part of the subtree of shallow node
    elif left_lca is not None and right_lca is None:
        return left_lca
    elif left_lca is None and right_lca is not None:
        return right_lca


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

    # print("without withoutoparent", lowest_common_ancestor_without_parent_info(root, node7, node3).get_node_value())
    print("without oparent",lowest_common_ancestor_without_parent_info(root, node7, node4).get_node_value())
    print("with oparent",lowest_common_ancestor_with_parent_info(node7, node3).get_node_value())
    print("with oparent",lowest_common_ancestor_with_parent_info(node1, node7).get_node_value())
