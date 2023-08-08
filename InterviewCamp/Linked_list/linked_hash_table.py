from typing import Optional, Any, Dict, List


# space: O(1), time: O(n)
# implementing a doubly linked list 
class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.__data: Any = data
        self.__next: Optional[Node] = next_node
        self.__prev: Optional[Node] = prev_node

    def get_data(self):
        return self.__data

    def get_next_node(self):
        return self.__next

    def get_prev_node(self):
        return self.__prev

    def set_data(self, new_data):
        self.__data = new_data

    def set_next_node(self, new_next_node):
        self.__next = new_next_node

    def set_prev_node(self, new_prev_node):
        self.__prev = new_prev_node


class LRUCache:
    def __init__(self, length_of_cache: int, node: Node = None):
        self.__head: Node = node
        self.__tail: Node = self.__head
        self.__current_length: int = 1 if node is not None else 0
        self.__length_of_cache: int = length_of_cache
        self.__linked_hash_map: Dict[int, Node] = {node.get_data(): node}

    def print_cache_nodes(self):
        string = ""
        node = self.__head
        while node is not None:
            string += str(node.get_data())
            if node.get_next_node() is not None:
                string += "-->"
            node = node.get_next_node()
        print(string)

    def print_linked_hashmap_status(self):
        print("self.__linked_hash_map:")
        for key, value in self.__linked_hash_map.items():
            print(f"{key} : prev: {value.get_prev_node()}, next: {value.get_next_node()}")

    def write_to_cache(self, node: Node):
        if node is None:
            return
        else:
            # if max_length of cache reached, delete the head element and move head to next element
            # remove the key from the dictionary
            if self.__current_length == self.__length_of_cache:
                self.remove_element(self.__head)

            # append the new node and update the dictionary
            self.add_element(node)

    def read_from_cache(self, node: Node):
        if node.get_data() in self.__linked_hash_map:
            self.remove_element(node)
            self.add_element(node)
        else:
            print("Node not found")

        self.print_cache_nodes()
        return node.get_data()

    def remove_element(self, to_delete):
        if to_delete.get_data() not in self.__linked_hash_map:
            return
        else:
            self.__remove_from_linked_list(to_delete)
            del self.__linked_hash_map[to_delete.get_data()]
            self.__current_length -= 1

    def add_element(self, to_add):
        self.__add_to_linked_list(to_add)
        self.__linked_hash_map[to_add.get_data()] = self.__tail
        # update the current length
        self.__current_length += 1

    def __remove_from_linked_list(self, to_delete):
        if to_delete.get_prev_node() is not None:
            to_delete.get_prev_node().set_next_node(to_delete.get_next_node())

        if to_delete.get_next_node() is not None:
            to_delete.get_next_node().set_prev_node(to_delete.get_prev_node())

        if to_delete == self.__head:
            self.__head = self.__head.get_next_node()
            self.__head.set_prev_node(None)

        if to_delete == self.__tail:
            self.__tail = self.__tail.get_prev_node()
            self.__tail.set_next_node(None)

    def __add_to_linked_list(self, to_add: Node):
        to_add.set_prev_node(None)
        to_add.set_next_node(None)

        if self.__head is None:
            self.__head = to_add
        else:
            self.__tail.set_next_node(to_add)
            to_add.set_prev_node(self.__tail)

        self.__tail = to_add


if __name__ == '__main__':
    nodes_list: List[Node] = [Node(2)]
    my_lru_cache: LRUCache = LRUCache(5, nodes_list[0])

    for i in range(3, 8):
        nodes_list.append(Node(i))
        my_lru_cache.write_to_cache(nodes_list[-1])
        my_lru_cache.print_cache_nodes()

    # print([node.get_data() for node in nodes_list])
    # my_lru_cache.print_linked_hashmap_status()
    print(f"Recently accessed element: {my_lru_cache.read_from_cache(nodes_list[-3])}")
    my_lru_cache.print_linked_hashmap_status()
