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


if __name__ == '__main__':
    tail = Node(6, None)
    head = Node('A', tail)

    ll = LinkedList(head, tail)
    ll.append(5)
    ll.append(6)
    ll.append('A')
    ll.append(2)
    ll.append('A')
    ll.append(5)

    ll2 = LinkedList()
    ll2.append(7)
    ll2.append(8)
    ll2.append(9)

    ll3 = LinkedList(Node(10))
    ll.print_nodes()
    print(ll.search_for_k(6).get_next_node().get_data())
    # ll.delete(ll.search_for_k(5), ll.search_for_k(6))
    ll.delete(ll.search_for_k('A'), )
    ll.print_nodes()

    # try:
    #     ll.print_nodes()
    #     print(ll.search_for_k('A'))
    #     print(ll.get_nth_element(2).data)
    #     print(f"Tail element:{ll.get_tail().data}")
    #     print("%%%%%%%%% Second linked list : %%%%%%%%%%")
    #     ll2.print_nodes()
    #     print(f"Head element:{ll2.get_head().data}")
    #     print(f"Tail element:{ll2.get_tail().data}")
    #     print(ll2.search_for_k(7))
    #     print(ll2.get_nth_element(1).data)
    #     # print(ll2.search_for_k(6))
    #     print("%%%%%%%%% Third linked list : %%%%%%%%%%")
    #     ll3.print_nodes()
    #     ll3.append(17)
    #     ll3.print_nodes()
    #     print(f"Head element:{ll3.get_head().data}")
    #     print(f"Tail element:{ll3.get_tail().data}")
    # except Exception as e:
    #     print(e)

