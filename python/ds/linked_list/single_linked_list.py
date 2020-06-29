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
        print("")

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

    def insert_at_position(self, data: int, position: int):
        """
        :param data:
        :param position:
        :return:
        """
        node = self.head
        node_count = 0
        while (node.link.link is not None) & (node_count != position):
            node = node.link
            node_count += 1
        new_node = Node(data)
        new_node.link = node.link
        node.link = new_node

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
