class Stack:
    MAX_SIZE = 10
    EMPTY_STACK_TOP = -1

    def __init__(self):
        self.elements = []
        self.top = -1

    def push(self, data):
        self.__check_for_full()
        self.elements.append(data)
        self.top += 1

    def __check_for_empty(self):
        if self.top == Stack.EMPTY_STACK_TOP:
            raise Exception("Stack is Empty")

    def __check_for_full(self):
        if self.top == Stack.MAX_SIZE:
            raise Exception("Stack is full")

    def pop(self):
        self.__check_for_empty()
        self.top -= 1
        return self.elements[self.top+1]

    def peek(self):
        self.__check_for_empty()
        return self.elements[self.top]

    def stack_size(self):
        return self.top + 1

    def print_stack(self):
        self.__check_for_empty()
        top_temp = self.top
        while top_temp != Stack.EMPTY_STACK_TOP:
            print(self.elements[top_temp])
            top_temp -= 1
