import networkx as nx

def find_arbitrage_opportunities(graph):
    opportunities = []
    for cycle in nx.simple_cycles(graph):
        profit = calculate_cycle_profit(cycle, graph)
        if profit > 0:
            opportunities.append((cycle, profit))
    return opportunities

def calculate_cycle_profit(cycle, graph):
    profit = 0
    for i in range(len(cycle)):
        start = cycle[i]
        end = cycle[(i + 1) % len(cycle)]
        profit += graph[start][end]['weight']
    return profit
