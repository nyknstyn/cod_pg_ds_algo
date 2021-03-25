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

    def print_tree_v2(self, current_node, nameattr='value', left_child='left', right_child='right', indent='', last='updown'):

        if hasattr(current_node, nameattr):
            name = lambda node: getattr(node, nameattr)
        else:
            name = lambda node: str(node)

        up = getattr(current_node, left_child)
        down = getattr(current_node, right_child)

        if up is not None:
            next_last = 'up'
            next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '|', ' ' * len(str(name(current_node.data))))
            self.print_tree_v2(up, nameattr, left_child, right_child, next_indent, next_last)

        if last == 'up':
            start_shape = '┌'
        elif last == 'down':
            start_shape = '└'
        elif last == 'updown':
            start_shape = ' '
        else:
            start_shape = '├'

        if up is not None and down is not None:
            end_shape = '┤'
        elif up:
            end_shape = '┘'
        elif down:
            end_shape = '┐'
        else:
            end_shape = ''

        print('{0}{1}{2}{3}'.format(indent, start_shape, name(current_node.data), end_shape))

        if down is not None:
            next_last = 'down'
            next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '|', ' ' * len(str(name(current_node))))
            self.print_tree_v2(down, nameattr, left_child, right_child, next_indent, next_last)

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
        raise Exception("Please pass valid traversal")

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
