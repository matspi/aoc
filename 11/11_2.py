import networkx as nx
from functools import cache

G = nx.DiGraph()


with open("input_11.txt") as f:
    for line in f.readlines():
        node = line.split(":")[0]
        succs = line.split(":")[1].strip().split(" ")

        G.add_node(node)
        for succ in succs:
            G.add_edge(node, succ)

assert nx.is_directed_acyclic_graph(G)


def count(s, d):
    if s not in G or d not in G:
        return 0

    c = {}
    for n in reversed(list(nx.topological_sort(G))):
        if n == d:
            c[n] = 1
        else:
            c[n] = sum(c.get(s, 0) for s in G.successors(n))
    return c.get(s, 0)


df = count("svr", "dac") * count("dac", "fft") * count("fft", "out")
fd = count("svr", "fft") * count("fft", "dac") * count("dac", "out")

print(df + fd)
