from ds.tree.binary.tree import Tree, Node
from ds.tree.tree_exceptions import EmptyTreeException, DuplicateNodeInBST


class BST(Tree):

    def insert_node(self, data: int):
        """
        Insert node, keeping the BST order intact
        :param data:
        :return:
        """
        try:
            self.__empty_tree()
        except EmptyTreeException as e:
            self.root = Node(data)
            return
        self.__insert_node(self.root, data)

    def search(self, data: int):
        self.__empty_tree()
        if self.__search(self.root, data):
            print("Data found")
        else:
            print("Data not found")

    def delete(self, data):
        self.__empty_tree()
        # self.root = self.__delete_2(self.root, data)
        if self.__delete(self.root, data):
            print("Node Deleted")
        else:
            print("Data Not Found")

    def __delete(self, current: Node, data: int, parent: Node = None, is_left: bool = False):
        """
                        10
                    11          6
                  8   7     9    10
                3   9
                   8   10
        :param current:  5
        :param parent:  10
        :param is_left: True
        :param data: 5
        :return:
        """
        if current is None:
            return False
        if current.data == data:
            if current.left is None and current.right is None:
                if parent is None:
                    self.root = None
                elif is_left:
                    parent.left = None
                else:
                    parent.right = None
                return True
            if current.left is None or current.right is None:
                if parent is None:
                    self.root = current.right if current.right else current.left
                elif is_left:
                    parent.left = current.right if current.right else current.left
                else:
                    parent.right = current.right if current.right else current.left
                return True
            largest_node = self.__pop_largest_node(current.left, current)  # TODO logic to get largest node
            if parent is None:
                self.root = largest_node
            elif is_left:
                parent.left = largest_node
            else:
                parent.right = largest_node
            largest_node.right = current.right
            largest_node.left = current.left
            return True
        if current.data < data:
            return self.__delete(current.right, data, current, False)
        return self.__delete(current.left, data, current, True)


    def __delete_2(self, node: Node, data: int):
        if node is None:
            return node
        if node.data < data:
            node.right = self.__delete_2(node.right, data)
        elif node.data > data:
            node.left = self.__delete_2(node.left, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                largest_node = self.__largest_node(node.left)
                node.data = largest_node.data
                node.left = self.__delete_2(node.left, largest_node.data)
        return node

    def __largest_node(self, node) -> Node:
        if node.right is None:
            return node
        return self.__largest_node(node.right)

    def __pop_largest_node(self, node, parent):
        if node.right is None:
            parent.right = None
            parent.left = node.left
            return node
        return self.__pop_largest_node(node.right, node)
#0 5 7 55 67 69 70 79 89

    def __search(self, node: Node, data: int):
        if node is None:
            return False
        if node.data == data:
            return True
        if node.data < data:
            return self.__search(node.right, data)
        else:
            return self.__search(node.left, data)

    def __insert_node(self, current_node: Node, data):
        if current_node.data == data:
            raise DuplicateNodeInBST
        if current_node.data < data:
            if current_node.right is None:
                current_node.right = Node(data)
                return True
            return self.__insert_node(current_node.right, data)
        if current_node.data > data:
            if current_node.left is None:
                current_node.left = Node(data)
                return True
            return self.__insert_node(current_node.left, data)

    def __empty_tree(self):
        if self.root is None:
            raise EmptyTreeException()
