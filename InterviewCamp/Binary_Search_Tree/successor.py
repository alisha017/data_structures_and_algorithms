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
            self.set_parent_child_node(to_delete, parent, None)

        # if to_delete has 1 child
        elif to_delete.get_left_node() is None:
            print("left is null")
            self.set_parent_child_node(to_delete, parent, to_delete.get_right_node())
            print("to_delete location:", parent.get_left_node())
        elif to_delete.get_right_node() is None:
            print("right node is null")
            self.set_parent_child_node(to_delete, parent, to_delete.get_left_node())
            print("to_delete location:", parent.get_left_node())

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
            print("updated to delete value (with 2 kids):", to_delete.get_node_value())
            print("parent not changed: parent:", parent.get_node_value(),
                  "  left child:", parent.get_left_node().get_node_value(),
                  "  right child:", parent.get_right_node().get_node_value())
            print("successor parent : parent:", successor_parent.get_node_value())
            print("  left child:", (successor_parent.get_left_node().get_node_value()
                                    if successor_parent.get_left_node() is not None else None)),
            print("  right child:", (successor_parent.get_right_node().get_node_value()
                                     if successor_parent.get_right_node() is not None else None))

        print("Inorder traversal of the tree:", inorder_tree_traversal(self.__root))

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


def find_first_occurrence(bst: BinarySearchTree, value: float):
    node = bst.get_root()
    result = None

    while node is not None:
        print(f"current node value:", node.get_node_value())
        if node.get_node_value() > value:
            node = node.get_left_node()
        elif node.get_node_value() < value:
            node = node.get_right_node()
        else:
            print("Matched!:", node)
            result = node
            node = node.get_left_node()

    return result


def find_successor(node: TreeNode, root: TreeNode):
    result = None
    print("****" * 20)
    print("Current:", node.get_node_value())
    if node.get_right_node() is not None:
        print("node has right subtree")
        current = node.get_right_node()
        successor = None
        while current is not None:
            successor = current
            current = current.get_left_node()
        result = successor
    else:
        current = root
        successor = None
        value = node.get_node_value()
        # print(f"target: {value}")
        while current is not None:
            # print(f"Current val: {current.get_node_value() if current.get_node_value() is not None else None}, "
            #       f"Successor:{successor.get_node_value() if successor is not None else None}")
            if current.get_node_value() > value:
                successor = current
                current = current.get_left_node()
            elif current.get_node_value() < value:
                current = current.get_right_node()
            else:
                result = successor
                print("Matched!:", current.get_node_value(),
                      successor.get_node_value() if successor is not None else None)
                break

    return result


def find_successor_absent_support(node: float, root: TreeNode):
    successor = None
    to_find = root
    print("****" * 20)

    # find the node or find the first successor:
    while to_find is not None:
        print(f"to find: {to_find.get_node_value()}, node: {node}")
        if to_find.get_node_value() < node:
            to_find = to_find.get_right_node()
        elif to_find.get_node_value() > node:
            successor = to_find
            to_find = to_find.get_left_node()
        else:
            # print("finding successor...")
            # print(f"to_find:{to_find.get_node_value()}, root:{root.get_node_value()}")
            successor = find_successor(to_find, root)
            break

    # print("Final value:", successor.get_node_value(), node_found)
    return successor


def find_element_or_successor_absent_support(node: float, root: TreeNode):
    successor = None
    to_find = root
    print("****" * 20)

    # find the node or find the first successor:
    while to_find is not None:
        print(f"to find: {to_find.get_node_value()}, node: {node}")
        if to_find.get_node_value() < node:
            to_find = to_find.get_right_node()
        elif to_find.get_node_value() > node:
            successor = to_find
            to_find = to_find.get_left_node()
        else:
            # print("finding successor...")
            # print(f"to_find:{to_find.get_node_value()}, root:{root.get_node_value()}")
            return to_find

    # print("Final value:", successor.get_node_value(), node_found)
    return successor


def find_elements_in_range(bst: BinarySearchTree, lower_limit: float, upper_limit: float):
    root = bst.get_root()

    result_list = []

    successor = find_element_or_successor_absent_support(lower_limit, root)

    while lower_limit <= successor.get_node_value():
        result_list.append(successor.get_node_value())
        print(result_list)
        successor = find_successor_absent_support(successor.get_node_value(), root)
        if successor.get_node_value() > upper_limit:
            break

    return result_list


if __name__ == "__main__":

    my_bst = BinarySearchTree()

    for i in [4, 2, 6, 1, 1.5, 3, 5, 7]:
        my_bst.add_node(i)

    print(inorder_tree_traversal(my_bst.get_root()))

    to_search = [my_bst.search_for_val(1), my_bst.search_for_val(3),
    my_bst.search_for_val(7), my_bst.search_for_val(1.5)]
    for node in to_search:
        val = find_successor(node, my_bst.get_root())
        print(val.get_node_value() if val is not None else val)
        print("-----"*20)

    another_bst = BinarySearchTree()
    for i in [8, 3, 10, 1, 6, 4, 7, 14, 13]:
        another_bst.add_node(i)

    print(inorder_tree_traversal(another_bst.get_root()))

    successor_another_bst = find_successor_absent_support(14, another_bst.get_root())
    print(successor_another_bst.get_node_value() if successor_another_bst is not None else None)
    successor_another_bst = find_element_or_successor_absent_support(7.8, another_bst.get_root())
    print(successor_another_bst.get_node_value() if successor_another_bst is not None else None)
    
    print(find_elements_in_range(another_bst, 3.5, 11))
