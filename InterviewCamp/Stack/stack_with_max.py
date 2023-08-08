class Stack:
    def __init__(self, max_length: int):
        self.__max_length = max_length
        self.__current_length = 0
        self.__array = []

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow Exception")
        else:
            to_delete = self.__array.pop(-1)
            self.__current_length -= 1
            return to_delete

    def is_empty(self):
        return True if self.__current_length == 0 else False

    def is_full(self):
        return True if self.__current_length == self.__max_length else False

    def push(self, to_add: int):
        if self.is_full():
            raise Exception("Stack Overflow Exception")
        else:
            self.__array.append(to_add)
            self.__current_length += 1

    def peek(self):
        if self.is_empty():
            raise Exception("Stack Underflow Exception")
        else:
            return self.__array[-1]

    def current_length_of_stack(self):
        return self.__current_length

    def print_stack(self):
        temp_stack = Stack(self.current_length_of_stack())
        if self.is_empty():
            print("Empty stack")
        while not self.is_empty():
            print(f"|{self.peek()}|")
            temp_stack.push(self.pop())
        print("---")
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

    def flush_stack(self, to_stack):
        if self.is_empty():
            raise Exception("Stack underflow")

        if to_stack.is_full():
            raise Exception("Stack overflow")

        while not self.is_empty() and not to_stack.is_full():
            to_stack.push(self.pop())


class StackWithMax:
    def __init__(self, max_len):
        self.stack = Stack(max_len)
        self.__max_stack = Stack(max_len)

    def push(self, to_add):
        if self.stack.is_full():
            print("Stack overflow, no more space left")
            return

        self.stack.push(to_add)
        if not self.__max_stack.is_empty():
            if to_add > self.__max_stack.peek():
                self.__max_stack.push(to_add)
        else:
            self.__max_stack.push(to_add)

    def pop(self):
        if self.stack.is_empty():
            print("Stack underflow, no elements available")
            return

        deleted_ele = self.stack.pop()
        if not self.__max_stack.is_empty():
            if deleted_ele == self.__max_stack.peek():
                self.__max_stack.pop()

        return deleted_ele

    def max(self):
        if self.__max_stack.is_empty():
            raise "Stack underflow, no elements in the stack"
        else:
            return self.__max_stack.peek()


if __name__ == '__main__':
    my_stack = StackWithMax(5)

    for i in (4, 6, 5, 8, 3):
        my_stack.push(i)
        print(f"Max ele: {my_stack.max()}")

    for i in range(4):
        print(f"Popped: {my_stack.pop()}")
        print(f"Max ele: {my_stack.max()}")
