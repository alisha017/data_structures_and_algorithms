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

    def push(self, to_add):
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

def find_element(stack: Stack, to_find: int):
    if stack is None:
        return False
    if stack.current_length_of_stack() < 1:
        return False
    else:
        temp_stack = Stack(stack.current_length_of_stack())
        while stack.current_length_of_stack() != 0:
            top = stack.peek()
            if top == to_find:
                temp_stack.flush_stack(stack)
                return True
            else:
                temp_stack.push(stack.pop())

        temp_stack.flush_stack(stack)
        return False


if __name__ == '__main__':
    my_stack = Stack(5)
    # try:
    #     for i in range(1, 7):
    #         my_stack.push(i)
    #         my_stack.print_stack()
    # except Exception as e:
    #     print(e)
    #
    # try:
    #     for i in range(1, 7):
    #         my_stack.pop()
    #         my_stack.print_stack()
    # except Exception as e:
    #     print(e)

    another_stack = Stack(7)
    for i in range(11, 18):
        another_stack.push(i)

    print(find_element(another_stack, 11))
    another_stack.print_stack()
    print(find_element(another_stack, 10))
