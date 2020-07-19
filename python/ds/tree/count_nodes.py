from ds.tree.tree_base import TreeBase
from ds.tree.tree import Node


class CountNodes(TreeBase):

    def count_nodes(self, node_type: str = "all"):
        self.tree.empty_tree_check()
        if node_type == 'leaf':
            return self.__count_leaf_nodes(self.tree.root)
        elif node_type == 'non_leaf':
            return self.__count_non_leaf_nodes(self.tree.root)
        elif node_type == 'full':
            return self.__count_full_nodes(self.tree.root)
        else:
            return self.__count_nodes(self.tree.root)

    def __count_leaf_nodes(self, node: Node, count: int = 0):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self.__count_leaf_nodes(node.left, count) + self.__count_leaf_nodes(node.right, count)

    def __count_full_nodes(self, node: Node, count: int = 0):
        if not node:
            return 0
        if not node.left and not node.right:
            return 0
        return self.__count_full_nodes(node.left, count) + self.__count_full_nodes(node.right, count) + (1 if (node.left and node.right) else 0)

    def __count_non_leaf_nodes(self, node: Node, count: int = 0):
        if not node:
            return 0
        if not node.left and not node.right:
            return 0
        return 1 + self.__count_non_leaf_nodes(node.left, count) + self.__count_non_leaf_nodes(node.right, count)

    def __count_nodes(self, node: Node, count: int = 0):
        if not node:
            return 0
        return 1 + self.__count_nodes(node.left, count) + self.__count_nodes(node.right, count)
