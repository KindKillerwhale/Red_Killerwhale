import unittest
import networkx as nx
from core.graph_algorithms import build_connected_components

class TestGraphAlgorithms(unittest.TestCase):
    def test_build_connected_components(self):
        graph = nx.Graph()
        graph.add_edges_from([(1, 2), (2, 3), (4, 5)])
        components = build_connected_components(graph)
        self.assertEqual(len(components), 2)
        self.assertTrue(nx.is_connected(components[0]))
        self.assertTrue(nx.is_connected(components[1]))

if __name__ == '__main__':
    unittest.main()
