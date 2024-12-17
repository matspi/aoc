with open("16/16_input.txt", "r") as f:
  data = [line.strip() for line in f.readlines()]
  
H=len(data)
W=len(data[0])
  
import heapq

class Node:
    def __init__(self, pos, cost, direction):
        self.pos = pos
        self.cost = cost
        self.direction = direction

    def __lt__(self, other):
        return self.cost < other.cost
    
DIRS=((0,-1), (-1,0), (0,1), (1,0))
    
def get_adj_coords(pos):
    ret_val=[]
    x,y=pos
    search_list=['.', 'E']
    
    for d in DIRS:
        if data[y+d[1]][x+d[0]] in search_list:
            ret_val.append((x+d[0],y+d[1]))
    return ret_val
    
    
def dijkstra(visited, start_node):
    map = {}
    q = []

    map[start_node.pos] = start_node
    heapq.heappush(q, start_node)

    while q:
        n = heapq.heappop(q)
        x,y = n.pos
        cost = n.cost
        dir_x,dir_y = n.direction
        visited[y][x] = True

        adjList = get_adj_coords(n.pos)
        for adjLink in adjList:
            if (x+dir_x,y+dir_y) == adjLink:
                additional_cost = 1
            elif (x-dir_x,y-dir_y) == adjLink:
                additional_cost = 2001
            else:
                additional_cost = 1001        
            if not visited[adjLink[1]][adjLink[0]]:
                if adjLink not in map:
                    map[adjLink] = Node(adjLink, cost + additional_cost, (adjLink[0]-x, adjLink[1]-y))
                else:
                    sn = map[adjLink]
                    if cost + additional_cost < sn.cost:
                        sn.pos = adjLink
                        sn.direction = (adjLink[0]-x, adjLink[1]-y)
                        sn.cost = cost + additional_cost
                heapq.heappush(q, Node(adjLink, cost + additional_cost, (adjLink[0]-x, adjLink[1]-y)))

    return map

def find(c):
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == c:
                return (x,y)

visited = [[False for x in range(W)] for y in range(H)] 

S=find('S')
E=find('E')
start_node=Node(S, 0, (1,0))
costs = dijkstra(visited, start_node)

print(costs[E].cost)
