import sys

from ds.graph.graph import Graph, Edge


class TargetVertex:
    def __init__(self, vertex: str, weight: int):
        self.vertex = vertex
        self.weight = weight

def get_minimum_cost_spanning_tree(graph: Graph, Edges: []):
    # Tasks
    #   1. Validation: Empty Graph, Connected Graph
    #   2. Get Minimum Weighted Edge
    #   3. Create a dictionary nearest_vertex_dict with V keys. Keep adding the the nearest vertex on each traversal
    #   4. Create a list of dictionary. Keep adding the calculated minimum edges

    if graph.is_graph_empty():
        raise Exception("Graph is Empty")
    # todo add check for connected graph
    minimum_weighted_edge = graph.get_minimum_weighted_edge()
    spanning_tree = [minimum_weighted_edge]
    total_min_weight = minimum_weighted_edge.weight
    nearest_vertex_dict = {}
    for key in graph.graph_table.keys():
        if key == minimum_weighted_edge.start_v or key == minimum_weighted_edge.end_v:
            nearest_vertex_dict[key] = None
            continue
        start_v_to_key_weight = None
        end_v_to_key_weight = None
        try:
            start_v_to_key_weight = graph.get_weight(key, minimum_weighted_edge.start_v)
        except :
            pass
        try:
            end_v_to_key_weight = graph.get_weight(key, minimum_weighted_edge.end_v)
        except :
            pass
        if start_v_to_key_weight is None and end_v_to_key_weight is None:
            nearest_vertex_dict[key] = None
            continue
        if start_v_to_key_weight and end_v_to_key_weight:
            if start_v_to_key_weight < end_v_to_key_weight:
                nearest_vertex_dict[key] = TargetVertex(minimum_weighted_edge.start_v, start_v_to_key_weight)
            else:
                nearest_vertex_dict[key] = TargetVertex(minimum_weighted_edge.end_v, end_v_to_key_weight)
        elif start_v_to_key_weight:
            nearest_vertex_dict[key] = TargetVertex(minimum_weighted_edge.start_v, start_v_to_key_weight)
        else:
            nearest_vertex_dict[key] = TargetVertex(minimum_weighted_edge.end_v, end_v_to_key_weight)

    for key in range(2, graph.vertices):
        start_v = None
        min_weight = sys.maxsize
        for vertex in nearest_vertex_dict:
            if nearest_vertex_dict.get(vertex) is not None and nearest_vertex_dict.get(vertex).weight < min_weight:
                start_v = vertex
                min_weight = nearest_vertex_dict.get(vertex).weight

        spanning_tree.append(Edge(start_v, nearest_vertex_dict.get(start_v).vertex, min_weight))
        total_min_weight += min_weight
        nearest_vertex_dict[start_v] = None
        for key in graph.graph_table.keys():
            if nearest_vertex_dict[key] is not None:
                weight_from_last_vertex = None
                try:
                    weight_from_last_vertex = graph.get_weight(key, start_v)
                except:
                    pass
                if weight_from_last_vertex and nearest_vertex_dict[key].weight > weight_from_last_vertex:
                    nearest_vertex_dict[key] = TargetVertex(start_v, weight_from_last_vertex)

    return spanning_tree, total_min_weight

def get_test_graph():
    my_graph = Graph()
    my_graph.add_node("1", "1")
    my_graph.add_node("2", "2")
    my_graph.add_node("3", "3")
    my_graph.add_edge("1", "2", 4)
    my_graph.add_edge("1", "3", 89)
    my_graph.add_edge("2", "3", 80)
    return my_graph

