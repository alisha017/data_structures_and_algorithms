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

    def delete_tail_node_without_previous_node_info(self):
        if self.tail is None:
            raise Exception("Empty linked list. No node to delete")
        else:
            previous_node: Node = self.head
            while previous_node is not None and previous_node.get_next_node() != self.tail:
                previous_node = previous_node.get_next_node()

            self.delete(self.tail, previous_node)


class Queue_With_Max:
    def __init__(self):
        self.__main_queue = LinkedList()
        self.__max_queue = LinkedList()

    def enqueue(self, data: int):
        self.__main_queue.append(data)

        while self.__max_queue.get_head() is not None and data > self.__max_queue.get_tail().get_data():
            self.__max_queue.delete_tail_node_without_previous_node_info()
        self.__max_queue.append(data)

    def dequeue(self):
        if self.__main_queue.get_head() is None:
            raise Exception("Empty queue, cannot perform delete operation")
        to_delete = self.__main_queue.get_head().get_data()
        self.__main_queue.delete(self.__main_queue.get_head(), None)

        if self.__max_queue.get_head() is not None and self.__max_queue.get_head().get_data() == to_delete:
            self.__max_queue.delete(self.__max_queue.get_head(), None)

    def get_max(self):
        if self.__max_queue.get_head() is not None:
            return self.__max_queue.get_head().get_data()
        else:
            raise Exception("Empty queue")

    def print_current_status(self):
        print("Main queue:")
        self.__main_queue.print_nodes()
        print("Max queue")
        self.__max_queue.print_nodes()


if __name__ == '__main__':
    qwm = Queue_With_Max()

    qwm.enqueue(2)
    print(qwm.get_max())
    qwm.enqueue(4)
    print(qwm.get_max())
    qwm.enqueue(3)
    print(qwm.get_max())
    qwm.enqueue(1)
    print(qwm.get_max())
    qwm.enqueue(5)
    qwm.print_current_status()
    print(qwm.get_max())
    qwm.enqueue(0)
    qwm.print_current_status()

    print(qwm.get_max())
    qwm.enqueue(2)
    qwm.print_current_status()

    print(qwm.get_max())
    qwm.dequeue()
    qwm.print_current_status()

    print(qwm.get_max())
    qwm.dequeue()
    qwm.print_current_status()

    print(qwm.get_max())
    qwm.dequeue()
    qwm.print_current_status()

    print(qwm.get_max())
    qwm.dequeue()
    qwm.print_current_status()

    print(qwm.get_max())
    qwm.dequeue()
    qwm.print_current_status()
    print(qwm.get_max())

