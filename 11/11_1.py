import networkx as nx

G = nx.DiGraph()


with open("input_11.txt") as f:
    for line in f.readlines():
        node = line.split(":")[0]
        succs = line.split(":")[1].strip().split(" ")

        G.add_node(node)
        for succ in succs:
            G.add_edge(node, succ)
sum = 0
paths = nx.all_simple_paths(G, "you", "out")
for p in paths:
    print(p)
    sum += 1

print(sum)
