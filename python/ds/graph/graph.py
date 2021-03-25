import sys

from ds.linked_list.single_linked_list import SingleLinkedList


class DataNode:
    """
    Data Object
    """
    def __init__(self, data):
        self.data = data


class Edge:
    def __init__(self, start_v: str, end_v: str, weight: int = None):
        self.start_v = start_v
        self.end_v = end_v
        self.weight = weight


class AdjacencyData:
    def __init__(self, key: str, weight: int = None):
        self.key = key
        self.weight = weight


class ReferenceNode:
    """
        adjacency_list: data = key

    """
    def __init__(self, data_reference: DataNode, adjacency_list: SingleLinkedList = None):
        self.data_reference = data_reference
        self.adjacency_list = adjacency_list if adjacency_list is not None else SingleLinkedList()


class Graph:
    """
        graph table: Dict of addresses pointing to head of node list adjacent to that node
                    key --> ReferenceNode
    """
    def __init__(self, is_undirected: bool = True):
        self.is_undirected = is_undirected
        self.vertices = 0
        self.graph_table = {}

    def add_node(self, data, key: str):
        if self.graph_table.get(key) is not None:
            raise Exception("Key already Present")
        self.vertices += 1
        self.graph_table[key] = ReferenceNode(DataNode(data))

    def add_edge(self, key1: str, key2: str, weight: int = None):
        if self.graph_table.get(key1) is None or self.graph_table.get(key2) is None:
            raise Exception("Key not Present")
        if key1 == key2:
            raise Exception("Cannot create edge between same nodes")
        self.graph_table.get(key1).adjacency_list.append(AdjacencyData(key2, weight))
        self.graph_table.get(key2).adjacency_list.append(AdjacencyData(key1, weight))

    def get_minimum_weighted_edge(self):
        self.__is_graph_empty()
        edge = Edge(None, None, sys.maxsize)
        for key in self.graph_table.keys():
            if not self.graph_table.get(key).adjacency_list.is_empty():
                node = self.graph_table.get(key).adjacency_list.head
                while node:
                    if node.data.weight < edge.weight:
                        edge = Edge(key, node.data.key, node.data.weight)
                    node = node.link
        return edge

    def __is_graph_empty(self):
        if self.is_graph_empty():
            raise Exception("Graph is empty")

    def is_graph_empty(self):
        return self.vertices == 0

    def get_weight(self, start_v: str, end_v: str):
        self.__is_graph_empty()
        if self.graph_table.get(start_v) is None or self.graph_table.get(end_v) is None:
            raise Exception("Key not Present")

        if self.graph_table.get(start_v).adjacency_list.head is None:
            raise Exception("{} is isolated".format(start_v))

        node = self.graph_table.get(start_v).adjacency_list.head
        while node:
            if node.data.key == end_v:
                return node.data.weight
            node = node.link
        raise Exception("{} is not connected to {}".format(start_v, end_v))

    def is_connected(self, key1: str, key2: str):
        if self.graph_table.get(key1) is None or self.graph_table.get(key2) is None:
            raise Exception("Key not Present")

        if self.graph_table.get(key1).adjacency_list.head is not None:
            node = self.graph_table.get(key1).adjacency_list.head
            while node:
                if node.data.key == key2:
                    print("Connected")
                    return
                node = node.link
            print("Not Connected")
        else:
            print("Not Connected")


"""
Problems: Creating edge to same node. Two elements are added in the same node
"""