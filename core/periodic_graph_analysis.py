import networkx as nx
from core.graph_algorithms import build_connected_components
import logging

class PeriodicGraphAnalyzer:
    def __init__(self):
        pass

    def build_graph(self, market_data):
        graph = nx.DiGraph()
        for data in market_data:
            graph.add_edge(data['from'], data['to'], weight=data['price'])
        logging.info("Graph built from market data")
        return graph

    def find_profitable_opportunities(self, graph):
        connected_components = build_connected_components(graph)
        opportunities = []
        for component in connected_components:
            cycles = list(nx.simple_cycles(component))
            for cycle in cycles:
                profit = self.analyze_cycle(cycle, component)
                if profit > 0:
                    opportunities.append((cycle, profit))
        logging.info(f"Profitable opportunities found: {opportunities}")
        return opportunities

    def analyze_cycle(self, cycle, graph):
        profit = 0
        for i in range(len(cycle)):
            start = cycle[i]
            end = cycle[(i + 1) % len(cycle)]
            profit += graph[start][end]['weight']
        return profit
