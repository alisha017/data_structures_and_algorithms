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


OPERATORS = {"+", "-", "*", "/"}
PRECEDENCE = {
    "*": 2,
    "/": 2,
    "-": 1,
    "+": 1
}


def process_expression(operand1: int, operand2: int, operator: str):
    if operator == "+":
        return operand1 + operand2
    if operator == "-":
        return operand1 - operand2
    if operator == "*":
        return operand1 * operand2
    if operator == "/":
        if operand2 == 0:
            raise ZeroDivisionError
        else:
            return operand1 // operand2


def evaluate_infix_expression(infix_expression: str):
    """
    maintain 2 stacks, operator stack and operand stack
    if operand put in a stack, operator in another stack
    if same or higher precendence operator, keep pushing,
    if lower precendence operator, pop and evaluate with the last 2 operands
    with the older operand being the first operand.
    :param infix_expression: a postfix expression
    :return: solution (int)
    """
    infix_expression_list = infix_expression.split(" ")
    print(f"Expression list: {infix_expression_list}")
    if len(infix_expression_list) > 2:
        operand_stack = Stack(len(infix_expression_list))
        operator_stack = Stack(len(infix_expression_list))

        for char in infix_expression_list:
            print(f"Current char:{char}")
            if char.isdigit():
                operand_stack.push(int(char))
                print("Current operator stack status:", operator_stack.print_stack())
                print("Current operand stack status:", operand_stack.print_stack())
            elif char in OPERATORS:
                if operator_stack.is_empty() or PRECEDENCE[char] >= PRECEDENCE[operator_stack.peek()]:
                    operator_stack.push(char)
                else:

                    while PRECEDENCE[operator_stack.peek()] > PRECEDENCE[char]:
                        print(f'print(PRECEDENCE[operator_stack.peek()]:{PRECEDENCE[operator_stack.peek()]}  '
                              f'> PRECEDENCE[char]:{PRECEDENCE[char]}')
                        operand2 = operand_stack.pop()
                        operand1 = operand_stack.pop()
                        operator = operator_stack.pop()
                        solution = process_expression(operand1, operand2, operator)
                        print(f"Expression: {operand1} {operator} {operand2}, Computed: {solution}")
                        operand_stack.push(solution)
                    operator_stack.push(char)

        while not operator_stack.is_empty():
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            operator = operator_stack.pop()
            solution = process_expression(operand1, operand2, operator)
            print(f"Expression: {operand1} {operator} {operand2}, Computed: {solution}")
            operand_stack.push(solution)

        return operand_stack.pop()

    elif len(infix_expression_list) == 0 or infix_expression == "":
        return 0
    else:
        raise Exception("Illegal input expression")


def evaluate_postfix_expression(postfix_expression: str):
    """
    if operands, push to a stack, if operator, pop last 2 elements, operate and push the result to stack
    :param postfix_expression:
    :return:
    """

    postfix_expression_list = postfix_expression.split(" ")
    print(f"Postfix expression list: {postfix_expression_list}")
    if len(postfix_expression_list) > 2:
        operand_stack = Stack(len(postfix_expression_list))
        for char in postfix_expression_list:
            print(f"Current char:{char}")
            if char in OPERATORS:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                solution = process_expression(operand1, operand2, char)
                print(f"Expression: {operand1} {char} {operand2}, Computed: {solution}")
                operand_stack.push(solution)
            elif char.isdigit():
                operand_stack.push(int(char))
                print("Current stack status:", operand_stack.print_stack())
            else:
                raise Exception("Invalid input expression")
        return operand_stack.pop()
    elif len(postfix_expression_list) == 0 or postfix_expression == "":
        return 0
    else:
        raise Exception("Invalid input expression")


if __name__ == '__main__':
    postfix_expr = ["2 10 + 9 6 - /", "", "1 -", "c d"]
    # for expr in postfix_expr:
    #     try:
    #         print(f"Solution:{evaluate_postfix_expression(expr)}")
    #     except Exception as e:
    #         print(f"Oops! Error occurred: {e}")

    infix_expr = ["1 + 2", "1 + 2 * 8 / 4", "1 +", "c f"]
    for expr in infix_expr:
        try:
            print(f"Solution:{evaluate_infix_expression(expr)}")
        except Exception as e:
            print(f"Oops! Error occurred: {e}")
