from typing import Optional


class TreeNode:
    def __init__(self, value: float, right: Optional['TreeNode'] = None,
                 left: Optional['TreeNode'] = None):
        self._value: float = value
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

    def set_node_value(self, val: float):
        self._value = val

    def set_right_node(self, new_right: Optional['TreeNode']):
        self.__right_node = new_right

    def set_left_node(self, new_left: Optional['TreeNode']):
        self.__left_node = new_left

    def set_visited(self, new_visited):
        self.__visited = new_visited


class BinarySearchTree:
    def __init__(self):
        self.__root: Optional[TreeNode] = None

    def add_node(self, new: float):
        parent: Optional[TreeNode] = self.__root
        current: Optional[TreeNode] = self.__root

        while current is not None:
            parent = current
            if parent.get_node_value() < new:
                current = parent.get_right_node()
            else:
                current = parent.get_left_node()

        new_node: TreeNode = TreeNode(new)
        if parent is None:
            self.__root = new_node
        elif parent.get_node_value() < new:
            parent.set_right_node(new_node)
        else:
            parent.set_left_node(new_node)

    def search_for_val(self, to_search: float):
        current: Optional[TreeNode] = self.__root

        while current is not None:
            if current.get_node_value() == to_search:
                return current
            if current.get_node_value() < to_search:
                current = current.get_right_node()
            else:
                current = current.get_left_node()

        return None

    def delete_node(self, to_delete: TreeNode, parent: TreeNode):
        print(to_delete.get_node_value(), to_delete.get_left_node(), to_delete.get_right_node())
        # if leaf node
        if to_delete.get_left_node() is None and to_delete.get_right_node() is None:
            print("left and right nodes are null")
            print(parent.get_node_value())
            self.set_parent_child_node(to_delete, parent, None)

        # if to_delete has 1 child
        elif to_delete.get_left_node() is None:
            print("left is null")
            self.set_parent_child_node(to_delete, parent, to_delete.get_right_node())
        elif to_delete.get_right_node() is None:
            print("right node is null")
            self.set_parent_child_node(to_delete, parent, to_delete.get_left_node())
        # if to_delete has 2 children
        else:
            print("left and right nodes are not null")
            # setting the left most child of the right child of to_delete at the to_delete position
            successor_parent = to_delete
            successor_current_node = to_delete.get_right_node()
            while successor_current_node.get_left_node() is not None:
                successor_parent = successor_current_node
                successor_current_node = successor_current_node.get_left_node()
            to_delete.set_node_value(successor_current_node.get_node_value())
            self.delete_node(successor_current_node, successor_parent)

    def get_root(self):
        return self.__root

    def set_parent_child_node(self, old_child, parent: Optional[TreeNode], new_child: Optional[TreeNode]):
        if parent is None:
            self.__root = new_child
        else:
            print("Parent:", parent.get_node_value())
            if parent.get_left_node() == old_child:
                parent.set_left_node(new_child)
                print(f"parent right node: {parent.get_right_node().get_node_value()}")
            elif parent.get_right_node() == old_child:
                parent.set_right_node(new_child)
                print(f"parent left node: {parent.get_left_node().get_node_value()}")
            else:
                raise Exception("Old child not found in the given parent")


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


if __name__ == "__main__":

    my_bst = BinarySearchTree()

    for i in [4, 2, 6, 1, 3, 5, 7]:
        my_bst.add_node(i)
    # root = TreeNode(4)
    # node1 = TreeNode(2)
    # node2 = TreeNode(6)
    # node3 = TreeNode(1)
    # node4 = TreeNode(3)
    # node5 = TreeNode(5)
    # node6 = TreeNode(7)

    node_5 = my_bst.search_for_val(5)
    node_6 = my_bst.search_for_val(6)
    print(inorder_tree_traversal(my_bst.get_root()))

    my_bst.delete_node(node_5, node_6)
    print(inorder_tree_traversal(my_bst.get_root()))

