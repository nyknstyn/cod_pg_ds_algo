from ds.linked_list.single_linked_list import SingleLinkedList, Node


class StackWithLinkedList:

    def __init__(self):
        self.stack = SingleLinkedList()

    def push(self, data):
        self.stack.insert_node(data)

    def pop(self):
        data = self.stack.element_at_position(1)
        self.stack.delete_at_position(1)
        return data

    def peek(self):
        return self.stack.element_at_position(1)

    def stack_size(self):
        return self.stack.length()

    def print(self):
        print("Top : ", end="")
        self.stack.print_list()
        print(" : Bottom", end="")
