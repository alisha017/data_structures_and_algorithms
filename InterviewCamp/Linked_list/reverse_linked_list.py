from typing import Optional, Any


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

    def append(self, data):
        node = Node(data)
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


def reverse_linked_list(lili: LinkedList):
    if lili is None:
        return None

    prev: Optional[Node] = None
    curr: Optional[Node] = lili.get_head()
    if lili.get_head() == lili.get_tail():
        return lili.get_tail()

    while curr is not None:
        next: Optional[Node] = curr.get_next_node()
        curr.set_next_node(prev)
        prev = curr
        curr = next

    return prev


if __name__ == '__main__':

    ll2 = LinkedList()
    ll2.append(7)
    ll2.append(8)
    ll2.append(9)
    ll2.append(10)
    print(reverse_linked_list(ll2).get_data())
