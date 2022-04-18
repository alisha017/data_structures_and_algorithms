from typing import Optional, Any


class Node:
    def __init__(self, data, next_node=None):
        self.data: Any = data
        self.next: Optional[Node] = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next

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


def append_2_linked_lists(to_append: LinkedList, original: LinkedList):
    if to_append is None or to_append.get_head() is None:
        return
    else:
        original.append(to_append.get_head())
        original.set_tail(to_append.get_tail())


# time complexity : O(n), space complexity : O(1)
def sort_nodes(linked_list: LinkedList):
    node = linked_list.head
    nodes_dictionary = {}
    while node is not None:
        if node.data not in nodes_dictionary:
            nodes_dictionary[node.data] = LinkedList(Node(node.data))
        else:
            nodes_dictionary[node.data].append(node.data)
        node = node.next
    all_nodes = list(nodes_dictionary.keys())
    all_nodes.sort()
    # for node_data in all_nodes:
    #     nodes_dictionary[node_data].print_nodes()

    result = nodes_dictionary[all_nodes[0]]
    for i in range(1, len(all_nodes)):
        # nodes_dictionary[all_nodes[i]]\
        #     .get_tail()\
        #     .set_next_node(nodes_dictionary[all_nodes[i+1]].get_head())
        append_2_linked_lists(nodes_dictionary[all_nodes[i]], result)

    return [result.get_head().get_data(), result.get_tail().get_data()]

# # time complexity : O(n), space complexity : O(1)
# def sort_nodes(linked_list: LinkedList):
#     node = linked_list.get_head()
#     nodes_dictionary = {}
#     while node is not None:
#         if node.data not in nodes_dictionary:
#             nodes_dictionary[node.get_data()] = 1  # o(1)
#         else:
#             nodes_dictionary[node.get_data()] += 1
#         node = node.next
#     print(nodes_dictionary)
#     sorted_linked_list = LinkedList()
#     for key, value in nodes_dictionary.items():
#         counter = 0
#         while counter < value:
#             sorted_linked_list.append(key)
#             counter += 1
#
#     sorted_linked_list.print_nodes()


if __name__ == '__main__':
    tail = Node(6, None)
    head = Node(7, tail)

    ll = LinkedList(head, tail)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(3)
    ll.append(7)
    ll.append(5)

    print(sort_nodes(ll))

