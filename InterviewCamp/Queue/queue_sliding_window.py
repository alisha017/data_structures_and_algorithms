from typing import Any, List, Optional


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


class Stock_Price:
    def __init__(self, price, day):
        self.__price = price
        self.__day = day

    def get_price(self):
        return self.__price

    def get_day(self):
        return self.__day


class Stock_Price_With_Time:
    def __init__(self, window_days: int):
        self.__stock_past_window_days = LinkedList()
        self.__window_days = window_days

    # assuming that day is always current and sorted
    def add_new_stock_info(self, stock_price: int, day: int):

        current_data = Stock_Price(stock_price, day)
        if self.__stock_past_window_days.get_tail() is not None \
                and day < self.__stock_past_window_days.get_tail().get_data().get_day():
            raise Exception("Previous days' input")

        if self.__stock_past_window_days.get_head() is not None:
            while self.__stock_past_window_days.get_head() is not None \
                    and day - self.__stock_past_window_days.get_head().get_data().get_day() > self.__window_days-1:
                print(f"Current head day:{self.__stock_past_window_days.get_head().get_data().get_day()}, current day: {day}")
                self.__stock_past_window_days.delete(self.__stock_past_window_days.get_head(), None)

        self.__stock_past_window_days.append(current_data)

    def get_max_stock_price(self):
        if self.__stock_past_window_days.get_head() is None:
            return 0

        max_price = 0
        curr = self.__stock_past_window_days.get_head()
        while curr is not None:
            if curr.get_data().get_price() > max_price:
                max_price = curr.get_data().get_price()
            curr = curr.get_next_node()

        return max_price


# not FIFO, insertion and deletion can happen from both ends
class Deque:
    def __init__(self, capacity: int):
        self.__q = LinkedList()
        self.__capacity = capacity
        self.__current_length = 0

    def enqueue(self, data: Any):
        if self.__current_length == self.__capacity:
            self.dequeue()

        self.__q.append(data)
        self.__current_length += 1

    def dequeue(self):
        if self.__q.get_head() is None and self.__q.get_tail() is None:
            raise Exception("Empty queue, can't perform delete operation")

        self.__q.delete(self.__q.get_head(), None)
        self.__current_length -= 1

    def print_queue(self):
        self.__q.print_nodes()

    def get_current_length(self):
        return self.__current_length

    def get_last_element(self):
        return self.__q.get_tail().get_data()

    def get_front_element(self):
        return self.__q.get_head().get_data()


def sliding_window_using_queue(num_list: List[int], k: int):
    if k == 0:
        return [0]
    elif k == 1:
        return num_list

    if num_list is None:
        return None
    elif len(num_list) < k:
        return sum(num_list)

    window_queue = Deque(k)
    sum_array = []
    sum_of_k_elements = 0

    for element in num_list:

        sum_of_k_elements += element
        window_queue.enqueue(element)

        if window_queue.get_current_length() == k:
            sum_array.append(sum_of_k_elements)
            sum_of_k_elements -= window_queue.get_front_element()

        print(f"Element: {element}\nSum of k elements:{sum_of_k_elements}")

    return sum_array


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 3

    print(sliding_window_using_queue(array, k))

    spwt = Stock_Price_With_Time(3)

    spwt.add_new_stock_info(1199,1)
    spwt.add_new_stock_info(102,1)
    spwt.add_new_stock_info(25,1)
    spwt.add_new_stock_info(17,2)
    spwt.add_new_stock_info(1229,2)
    spwt.add_new_stock_info(33,3)

    print(f"Max price: {spwt.get_max_stock_price()}")

    spwt.add_new_stock_info(26, 3)
    spwt.add_new_stock_info(87, 5)

    print(f"Max price: {spwt.get_max_stock_price()}")

    spwt.add_new_stock_info(33,10)
    spwt.add_new_stock_info(45,11)
    spwt.add_new_stock_info(34,12)

    print(f"Max price: {spwt.get_max_stock_price()}")

