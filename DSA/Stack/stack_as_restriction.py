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
        temp_stack.flush_stack(self)

    def flush_stack(self, to_stack):
        if self.is_empty():
            raise Exception("Stack underflow")

        if to_stack.is_full():
            raise Exception("Stack overflow")

        while not self.is_empty() and not to_stack.is_full():
            to_stack.push(self.pop())


# implementation with 2 stacks (used as restriction)
class Queue:
    def __init__(self, max_length: int):
        self.__stack1 = Stack(max_length)
        self.__stack2 = Stack(max_length)
        self.__max_length = max_length

    # time complexity : O(1)
    def enqueue(self, to_add: int):
        try:
            if self.__stack1.is_full():
                print("Queue is full, can't insert new element")
            else:
                self.__stack1.push(to_add)
        except Exception as e:
            print(e)
            return

    # time complexity : O(n)
    def dequeue(self):
        try:
            if self.__stack2.is_empty():
                self.__stack1.flush_stack(self.__stack2)

            if self.__stack2.is_empty():
                return None

            return self.__stack2.pop()
        except Exception as e:
            print(e)
            return None

    def print_queue(self):
        try:
            if self.__stack2.is_empty():
                self.__stack1.flush_stack(self.__stack2)

            if self.__stack2.is_empty():
                print("Empty Queue")
                return
            else:
                self.__stack2.print_stack()

            self.__stack2.flush_stack(self.__stack1)
        except Exception as e:
            print(e)
            return


class ArrayStack:
    def __init__(self, max_arr_len):
        self.__max_array_length = max_arr_len
        self.__array = [None] * max_arr_len
        self.__stack_pointer_dictionary = {
            1: {
                "curr_pos": -1,
                "min_pos": -1
            },
            2: {
                "curr_pos": self.__max_array_length,
                "min_pos": self.__max_array_length
            }}

    def push(self, stack_num, to_add):
        if self.__stack_pointer_dictionary[2]["curr_pos"] - self.__stack_pointer_dictionary[1]["curr_pos"] == 1:
            raise Exception("Stack overflow")

        if stack_num not in self.__stack_pointer_dictionary.keys():
            raise Exception("Illegal Stack number. It can be either 1 or 2")

        if stack_num == 1:
            self.__stack_pointer_dictionary[stack_num]["curr_pos"] += 1
        else:
            self.__stack_pointer_dictionary[stack_num]["curr_pos"] -= 1
        self.__array[self.__stack_pointer_dictionary[stack_num]["curr_pos"]] = to_add

    def pop(self, stack_num):
        if stack_num != 1 and stack_num != 2:
            raise Exception("Illegal Stack number. It can be either 1 or 2")

        if self.__stack_pointer_dictionary[stack_num]["curr_pos"] \
                == self.__stack_pointer_dictionary[stack_num]["min_pos"]:
            raise Exception("Stack underflow")
        else:
            popped_ele = self.__array[self.__stack_pointer_dictionary[stack_num]["curr_pos"]]
            self.__array[self.__stack_pointer_dictionary[stack_num]["curr_pos"]] = None
            if stack_num == 1:
                self.__stack_pointer_dictionary[stack_num]["curr_pos"] -= 1
            else:
                self.__stack_pointer_dictionary[stack_num]["curr_pos"] += 1
            return popped_ele

    def peek(self, stack_num):
        if stack_num != 1 and stack_num != 2:
            raise Exception("Illegal Stack number. It can be either 1 or 2")

        if self.__stack_pointer_dictionary[stack_num]["curr_pos"] \
                == self.__stack_pointer_dictionary[stack_num]["min_pos"]:
            raise Exception("Stack underflow")

        return self.__array[self.__stack_pointer_dictionary[stack_num]["curr_pos"]]

    def current_length_of_stack(self, stack_num):
        if stack_num != 1 and stack_num != 2:
            raise Exception("Illegal Stack number. It can be either 1 or 2")

        return abs(self.__stack_pointer_dictionary[stack_num]["min_pos"]
                   - self.__stack_pointer_dictionary[stack_num]["curr_pos"])

    def print_stack(self, stack_num):
        if stack_num != 1 and stack_num != 2:
            print("Illegal Stack number. It can be either 1 or 2")

        if self.__stack_pointer_dictionary[stack_num]["curr_pos"] \
                == self.__stack_pointer_dictionary[stack_num]["min_pos"]:
            print("Stack underflow")

        curr_pointer = self.__stack_pointer_dictionary[stack_num]["curr_pos"]
        while curr_pointer != self.__stack_pointer_dictionary[stack_num]["min_pos"]:
            print(f"| {self.__array[curr_pointer]} |")
            if stack_num == 1:
                curr_pointer -= 1
            else:
                curr_pointer += 1

        print("-"*7)


if __name__ == '__main__':
    # q1 = Queue(5)
    # for i in range(3, 10):
    #     q1.enqueue(i)
    #
    # print(q1.print_queue())
    #
    # for i in range(1, 9):
    #     print(q1.dequeue())
    #
    # print(q1.print_queue())

    arr_stack = ArrayStack(10)

    try:
        for i in range(4):
            arr_stack.push(1, i*10)
            arr_stack.push(2, i-2)
        print("Stack 1:")
        arr_stack.print_stack(1)
        print("Stack 2:")
        arr_stack.print_stack(2)
        print(f"Peek a boo: {arr_stack.peek(2)}")
        arr_stack.push(2, 900)
        arr_stack.push(2, 800)
        arr_stack.print_stack(2)
        # arr_stack.push(2, 1000)

        # for i in range(5):
        #     print(f"Popped: {arr_stack.pop(1)}")

        print(f"Popped: {arr_stack.pop(4)}")

    except Exception as e:
        print(e)
