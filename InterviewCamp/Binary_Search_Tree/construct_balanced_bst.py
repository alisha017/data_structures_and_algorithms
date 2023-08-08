from typing import Optional, Any


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


class Node:
    def __init__(self, data, next_node=None):
        self.data: Any = data
        self.next: Optional[Node] = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return  self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next_node(self, new_next_node):
        self.next = new_next_node


class LinkedList:
    def __init__(self, head: Node = None, tail: Node = None):
        self.head: Node = head
        if tail is None:
            self.tail = self.head
        else:
            self.tail: Node = tail

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def set_head(self, head: Node):
        self.head = head

    def set_tail(self, tail: Node):
        self.tail = tail

    # get node at nth position
    def get_nth_element(self, index):
        node: Node = self.head

        # moving to the next of n-1th element which is the nth element, if the linked list is shorter,
        # will raise exception
        for i in range(1, index):
            if node.next is not None:
                node = node.next
            else:
                raise Exception("Index out of bounds")

        # checking if the node is none, if not, return the node else raise exception
        if node is None:
            raise Exception("Index out of bounds")
        else:
            return node

    # search for specific data
    def search_for_k(self, k):
        node: Node = self.head
        counter = 0
        while node is not None:
            counter += 1
            if node.data == k:
                print(f"Element found at {counter}")
                return node
            else:
                node = node.next

        raise Exception("Element not found")

    def append(self, data: Any):
        if isinstance(data, Node) is False:
            node = Node(data)
        else:
            node = data
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def print_nodes(self):
        string = ""
        node = self.head
        while node is not None:
            string += str(node.data)
            if node.next is not None:
                string += "-->"
            node = node.next
        print(string)

    def delete(self, to_delete: Node, previous_node: Optional[Node]):
        if to_delete is None:
            return
        if to_delete == self.head:
            self.head = to_delete.get_next_node()
        if to_delete == self.tail:
            self.tail = previous_node
        if previous_node is not None:
            previous_node.set_next_node(to_delete.get_next_node())

        to_delete.set_next_node(None)

    def delete_without_previous_node(self, to_delete: Node):
        if to_delete is None:
            return
        if to_delete.get_next_node() is None:
            print("Tail node, cannot be deleted without the knowledge of previous node")
            return

        to_delete.set_data(to_delete.get_next_node().get_data())
        self.delete(to_delete, to_delete.get_next_node())


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


def preorder_tree_traversal(root: TreeNode):
    stack = []
    node = root
    stack.append(node)
    preorder_list = []

    # why stack.append(current_node) at the end when preorder should have it as the first line?
    # because we're implementing this using stack, so the process gets reversed
    while len(stack) > 0:
        current_node = stack.pop(-1)
        if current_node.is_visited() is True:
            preorder_list.append(current_node.get_node_value())
        else:
            current_node.set_visited(True)
            if current_node.get_right_node() is not None:
                stack.append(current_node.get_right_node())
            if current_node.get_left_node() is not None:
                stack.append(current_node.get_left_node())
            stack.append(current_node)
    return preorder_list


def check_out_of_bounds_error(array: list, index):
    return True if index < 0 or index >= len(array) else False


def construct_balanced_bst_using_list(sorted_elements_array: list, start_index, end_index) -> Optional[TreeNode]:
    if start_index > end_index \
            or check_out_of_bounds_error(sorted_elements_array, start_index) \
            or check_out_of_bounds_error(sorted_elements_array, end_index):
        return None
    mid = (start_index + end_index) // 2
    print(f"Creating current node from array: {sorted_elements_array[mid]}")
    node = TreeNode(sorted_elements_array[mid])

    node.set_left_node(construct_balanced_bst_using_list(sorted_elements_array, start_index, mid-1))
    node.set_right_node(construct_balanced_bst_using_list(sorted_elements_array, mid + 1, end_index))

    return node


def find_median_of_linked_list(head:Node, tail:Node):
    """
    since it is a singly linked list, we also need to return the previous node
    else if it was a doubly linked list, returning the median node would suffice
    :type head: Node
    :type tail: Node
    :return median_node: Node, previous_node: Node
    """

    slow_ptr:Node = head
    fast_ptr: Node = head
    previous_node: Optional[Node] = None

    while fast_ptr != tail:
        fast_ptr = fast_ptr.get_next_node()
        if fast_ptr != tail:
            previous_node = slow_ptr
            slow_ptr = slow_ptr.get_next_node()
            fast_ptr = fast_ptr.get_next_node()

    return slow_ptr, previous_node


def construct_balanced_bst_using_linked_list(head:Node, tail:Node):
    if head is None or tail is None or tail.get_next_node() == head:
        return None

    median_node, previous_node = find_median_of_linked_list(head, tail)

    print(f"Creating current node from ll:{median_node.get_data()}")
    node = TreeNode(median_node.get_data())
    node.set_left_node(construct_balanced_bst_using_linked_list(head, previous_node))
    node.set_right_node(construct_balanced_bst_using_linked_list(median_node.get_next_node(), tail))

    return node


if __name__ == "__main__":
    print("Hello World!")
    sorted_array: list = [1, 2, 3, 4, 5, 6, 7, 8]
    my_bst = construct_balanced_bst_using_list(sorted_array, 0, len(sorted_array)-1)
    print("***"*30)
    print("Creating balanced bst using list...")
    # print(inorder_tree_traversal(my_bst))
    print(preorder_tree_traversal(my_bst))

    sorted_linked_list = LinkedList()
    for i in range(1, 7):
        sorted_linked_list.append(i)
    print("***" * 30)
    print("Checking median of the linked list...")
    median_node, previous_node = find_median_of_linked_list(sorted_linked_list.get_head(), sorted_linked_list.get_tail())
    print(f"Previous: {previous_node.get_data() if previous_node is not None else None}")
    print(f"Previous: {median_node.get_data() if median_node is not None else None}")

    print("***" * 30)
    print("Creating balances bst using linked list...")
    ll_bst = construct_balanced_bst_using_linked_list(sorted_linked_list.get_head(), sorted_linked_list.get_tail())
    print(preorder_tree_traversal(ll_bst))


