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

sets=set()
for n, nbrs in G.adj.items():
  for a,b in combinations(nbrs, 2):
    if G.has_edge(a,b) or G.has_edge(b,a):
      cluster=[n,a,b]
      cluster.sort()
      sets.add(tuple(cluster))


count=0
for a,b,c in sets:
  if a.startswith("t") or b.startswith("t") or c.startswith("t"):
    count+=1

print(count)
pass