class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class SingleLinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def print_list(self):
        """
        Print data of all the nodes
        """
        if not self.head:
            print("Empty List")
            return
        node = self.head
        print(node.data, end="")
        node = node.link
        while node:
            print(" ==> {}".format(node.data), end="")
            node = node.link

    def insert_node(self, data: int):
        """
        Insert data at the beginning of list
        :param data:
        :return:
        """
        node = Node(data)
        node.link = self.head
        self.head = node
        print("Node inserted")

    def reverse(self):
        if not self.head:
            print("Empty list")
            return
        node = self.head
        prev_node = None
        while node:
            next_node = node.link
            node.link = prev_node
            prev_node = node
            node = next_node
        self.head = prev_node

    def reverse_using_recursion(self, current_node: Node, prev_node: Node = None):
        """

        :param current_node: Head of List
        :param prev_node: For internal purpose
        :return:
        """
        if current_node:
            self.reverse_using_recursion(current_node.link, current_node)
            current_node.link = prev_node
        else:
            self.head = prev_node

    def length(self) -> int:
        """
        Length of Linked List
        :return: int
        """
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.link
        return length

    def delete_at_position(self, position: int):
        """
        Delete node at given position
        :param position:
        :return:
        """
        if not self.head:
            print("Empty List")
            return
        if position < 1:
            print("Invalid position")
            return
        node = self.head
        if position == 1:
            self.head = node.link
            return
        node_count = 1
        prev_node = node
        node = node.link
        while node:
            node_count += 1
            if node_count == position:
                prev_node.link = node.link
                break
            prev_node = node
            node = node.link
        return

    def element_at_position(self, position: int):
        """
        Fetch Element at a given position
        :param position:
        :return:
        """
        if not self.head:
            raise Exception("List is empty")
        if position < 1:
            raise Exception("Invalid position")
        node = self.head
        node_count = 1
        while node:
            if position == node_count:
                return node.data
            position += 1
            node = node.link
        raise Exception("Invalid position")


    def insert_at_position(self, data: int, position: int):
        """
        Inserts node at a position
        :param data:
        :param position:
        :return:
        """
        node = self.head
        node_count = 1
        if position < 1:
            print("Invalid position")
            return
        if position == 1:
            new_node = Node(data)
            new_node.link = self.head
            self.head = new_node
            return
        if not self.head:
            print("List is empty")
            return
        prev_node = node
        node = node.link
        while node:
            node_count += 1
            if node_count == position:
                new_node = Node(data)
                new_node.link = prev_node.link
                prev_node.link = new_node
                break
            prev_node = node
            node = node.link



    def append(self, data):
        """
        Inserts data at the end of the list
        :param data:
        :return:
        """
        node = self.head
        if not node:
            self.insert_node(data)
            return
        while node.link:
            node = node.link
        node.link = Node(data)


if __name__ == "__main__":
    my_list = SingleLinkedList()
    my_list.insert_node(2)
    my_list.insert_node(3)
    my_list.insert_node(4)
    my_list.insert_node(5)

    my_list.print_list()

    my_list.append(9)

    my_list.print_list()

    my_list2 = SingleLinkedList()
    my_list2.append(8)
    my_list2.print_list()

    my_list2.insert_at_position(9, -1)

    my_list2.print_list()
