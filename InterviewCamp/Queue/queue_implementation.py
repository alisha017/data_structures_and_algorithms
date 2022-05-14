from typing import Any


class Queue:
    def __init__(self, arr_len: int):
        self.__front = 0
        self.__back = 0
        self.__current_length = 0
        self.__array = [None] * arr_len

    def enqueue(self, data: Any):
        if self.__current_length == len(self.__array):
            raise Exception("Queue full!")

        self.__array[self.__back] = data
        self.__back = (self.__back+1) % len(self.__array)
        self.__current_length += 1

    def dequeue(self):
        if self.__current_length == 0:
            raise Exception("Empty Queue!")

        deleted_element = self.__array[self.__front]
        self.__array[self.__front] = None
        self.__front = (self.__front+1) % len(self.__array)
        self.__current_length -= 1
        return deleted_element

    def print_queue(self):
        print(self.__array)
        print(f"Front element at: {self.__front}, {self.__array[self.__front]}")
        print(f"Back element at: {self.__back}, {self.__array[self.__back]}")
        print(f"Current length = {self.__current_length}")

    def get_front(self):
        return self.__array[self.__front]

    def get_back(self):
        return self.__array[self.__back]


if __name__ == '__main__':
    my_queue: Queue = Queue(5)

    print("Adding elements..........")
    for i in range(6):
        try:
            my_queue.enqueue(i)
            my_queue.print_queue()
            print()
        except Exception as e:
            print(e)

    print("\n\nDeleting elements..........")
    for i in range(6):
        try:
            my_queue.dequeue()
            my_queue.print_queue()
        except Exception as e:
            print(e)
