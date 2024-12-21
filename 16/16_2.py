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
       
from collections import deque
       
def dijkstra(visited, start_node, e):
    map = {}
    q = []
    best=float("inf")
    lowest={(start_node.pos[0], start_node.pos[1], start_node.direction[0], start_node.direction[1]): 0}
    backtrack={}
    end_states=set()

    map[start_node.pos] = start_node
    heapq.heappush(q, start_node)

    while q:
        n = heapq.heappop(q)
        x,y = n.pos
        cost = n.cost
        dir_x,dir_y = n.direction
        visited[y][x] = True
        
        # if cost > lowest[x,y,dir_x,dir_y]: continue
        # lowest[x,y,dir_x,dir_y] = cost
        
        if e == n.pos:
            if cost > best: break
            best = cost
            end_states.add((x,y,dir_x, dir_y))

        adjList = get_adj_coords(n.pos)
        for adjLink in adjList:
            if (x+dir_x,y+dir_y) == adjLink:
                additional_cost = 1
            elif (x-dir_x,y-dir_y) == adjLink:
                additional_cost = 2001
            else:
                additional_cost = 1001     
                
            new_cost = cost + additional_cost
                
            low = lowest.get((adjLink[0], adjLink[1], adjLink[0]-x, adjLink[1]-y), float('inf'))   

            if new_cost > low: continue
            if new_cost < low:
                backtrack[(adjLink[0], adjLink[1], adjLink[0]-x, adjLink[1]-y)] = set()
                lowest[(adjLink[0], adjLink[1], adjLink[0]-x, adjLink[1]-y)] = new_cost

            backtrack[(adjLink[0], adjLink[1], adjLink[0]-x, adjLink[1]-y)].add((x,y,dir_x,dir_y))
            heapq.heappush(q, Node(adjLink, cost + additional_cost, (adjLink[0]-x, adjLink[1]-y)))

    return end_states, backtrack



def find(c):
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == c:
                return (x,y)

visited = [[False for x in range(W)] for y in range(H)] 

S=find('S')
E=find('E')
start_node=Node(S, 0, (1,0))
end_states, bt = dijkstra(visited, start_node, E)

states = deque(end_states)
seen = set(end_states)

while states:
    k = states.popleft()
    for l in bt.get(k, []):
        if l in seen: continue 
        seen.add(l)
        states.append(l)
        
seats = {(x,y) for x,y,_,_ in seen}
        
print(seats)
print(len(seats))