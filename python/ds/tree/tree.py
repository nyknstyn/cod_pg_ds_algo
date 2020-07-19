class Node:
    def __init__(self, data: int):
        self.left = None
        self.data = data
        self.right = None


class Tree:
    def __init__(self, root: Node = None):
        self.root = root

    def insert_node(self, data: int):
        if not self.root:
            self.root = Node(data)
            print("Node Inserted as Root")
            return
        self.__insert_node(self.root, data)

    def print_tree(self, traversal: str):
        self.empty_tree_check()
        if not str:
            raise Exception("Please pass valid traversal")
        if traversal == 'pre_order':
            return self.__pre_order_print(self.root)
        if traversal == 'post_order':
            return self.__post_order_print(self.root)
        if traversal == 'in_order':
            return self.__in_order_print(self.root)
        print("")

    def search(self, data):
        self.empty_tree_check()
        if self.__search(data):
            print("Data Found")
        else:
            print("Data not Found")

    def empty_tree_check(self):
        if not self.root:
            raise Exception("Tree is Empty")

    def __search(self, node: Node, data: int) -> bool:
        if not node:
            return False
        if node.data == data:
            return True
        if self.__search(node.left, data):
            return True
        return self.__search(node.right, data)

    def __pre_order_print(self, node: Node):
        if node:
            print(node.data, end=" ")
            self.__pre_order_print(node.left)
            self.__pre_order_print(node.right)

    def __in_order_print(self, node: Node):
        if node:
            self.__in_order_print(node.left)
            print(node.data, end=" ")
            self.__in_order_print(node.right)

    def __post_order_print(self, node: Node):
        if node:
            self.__post_order_print(node.left)
            self.__post_order_print(node.right)
            print(node.data, end=" ")

    def __insert_node(self, node: Node, data: int) -> bool:
        """
        :param node: Node
        :param data: int
        :return: bool
        """
        if not node.left:
            node.left = Node(data)
            print("Node Inserted")
            return True
        if not node.right:
            node.right = Node(data)
            print("Node Inserted")
            return True
        if self.__insert_node(node.left, data):
            return True
        return self.__insert_node(node.right, data)
