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


# slow pointer --> 0,1,2,3,4
# fast pointer --> 0,2,4,6
# when slow_ptr = fast_ptr --> means there's a cycle in the linked list
# time complexity = O(2n)
# makes 2 cycles utmost to meet
def is_linked_list_cyclic(lili: LinkedList):
    slow_ptr = fast_ptr = lili.get_head()
    while fast_ptr is not None:
        try:
            fast_ptr = fast_ptr.get_next_node()
            if slow_ptr != lili.get_head() and slow_ptr == fast_ptr:
                print("cycle found")
                return True
            fast_ptr = fast_ptr.get_next_node()
            if slow_ptr != lili.get_head() and slow_ptr == fast_ptr:
                print("cycle found")
                return True
            else:
                slow_ptr = slow_ptr.get_next_node()
                # fast_ptr = fast_ptr.get_next_node().get_next_node()
                # print(f"Current status:\n  slow pointer:{slow_ptr.get_data()}\n  fast pointer:{fast_ptr.get_data()}")
                if fast_ptr.get_next_node() is None:
                    print("Hit tail. End of linked list reached, no cycle found")
                    return False
        except Exception as e:
            print("Nodes exhausted. End of linked list reached, no cycle found")
            return False


def find_length_of_cycle_in_linked_list(lili: LinkedList):
    if is_linked_list_cyclic(lili) is True:
        slow_ptr = lili.get_head()
        fast_ptr = slow_ptr.get_next_node().get_next_node()

        while slow_ptr != fast_ptr:
            fast_ptr = fast_ptr.get_next_node().get_next_node()
            slow_ptr = slow_ptr.get_next_node()
            # print(f"Element Current status:\n  slow pointer:{slow_ptr.get_data()}\n  fast pointer:{fast_ptr.get_data()}")

        slow_ptr = slow_ptr.get_next_node()
        length_of_cycle = 1
        # print(f"Current status:\n  slow pointer:{slow_ptr.get_data()}\n  fast pointer:{fast_ptr.get_data()}")

        while fast_ptr != slow_ptr and length_of_cycle!=10:
            length_of_cycle += 1
            slow_ptr = slow_ptr.get_next_node()
            print(f"Length Current status:\n  slow pointer:{slow_ptr.get_data()}\n  fast pointer:{fast_ptr.get_data()}")

        return length_of_cycle
    else:
        return -1


def find_start_of_cycle(lili: LinkedList):
    if is_linked_list_cyclic(lili):
        length_of_cycle = find_length_of_cycle_in_linked_list(lili)

        slow_ptr = lili.get_head()
        fast_ptr = slow_ptr

        for i in range(length_of_cycle):
            fast_ptr = fast_ptr.get_next_node()

        while slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.get_next_node()
            fast_ptr = fast_ptr.get_next_node()

        return slow_ptr
    else:
        return None


if __name__ == '__main__':
    tail = Node(5, None)
    head = Node(3, tail)
    cycle_node = Node(1, None)
    ll = LinkedList(head, tail)
    ll.append(cycle_node)
    ll.append(2)
    ll.append(4)
    ll.append(7)
    ll.append(9)
    ll.get_tail().set_next_node(cycle_node)
    print(is_linked_list_cyclic(ll))

    print(find_length_of_cycle_in_linked_list(ll))
    # print(find_start_of_cycle(ll))

    tail = Node(5, None)
    head = Node(3, tail)
    ll2 = LinkedList(head, tail)
    ll2.append(2)
    ll2.append(4)
    ll2.append(7)
    # ll2.append(9)

    ll2.print_nodes()
    # print(is_linked_list_cyclic(ll2))
    # print(find_length_of_cycle_in_linked_list(ll2))
    # print(find_start_of_cycle(ll2))


