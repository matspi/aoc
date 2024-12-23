import networkx as nx
from itertools import combinations

data = []
with open("23/23_input.txt", "r") as f:
  for l in f.readlines():
    a,b=l.strip().split("-")
    data.append((a,b))

connected={}

G = nx.Graph()

for a,b in data:
  G.add_edge(a,b)
  G.add_edge(b,a)


max_clique=max(nx.enumerate_all_cliques(G), key=len)
max_clique.sort()

print(",".join(max_clique))
