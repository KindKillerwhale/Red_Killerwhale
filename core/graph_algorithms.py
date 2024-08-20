import networkx as nx

def build_connected_components(graph):
    return [graph.subgraph(c).copy() for c in nx.connected_components(graph.to_undirected())]
