import heapq, copy


with open("20/20_input.txt", "r") as f:
  data = [list(line.strip()) for line in f.readlines()]

HEIGHT=len(data)
WIDTH=len(data[0])


DIRS=((0,-1), (-1,0), (0,1), (1,0))

def get_adj_coords(pos):
    ret_val=[]
    x,y=pos
    search_list=['.', 'E', '1', '2']

    for d in DIRS:
        new_x=x+d[0]
        new_y=y+d[1]
        if new_x>=0 and new_x<WIDTH and new_y>=0 and new_y<HEIGHT and data[new_y][new_x] in search_list:
            ret_val.append((new_x,new_y))
    return ret_val

class Node:
    def __init__(self, pos, cost):
        self.pos = pos
        self.cost = cost
        self.h = self.cost

    def __lt__(self, other):
        return self.h < other.h

def dijkstra(visited, start_node):
    map = {}
    q = []

    map[start_node.pos] = start_node
    heapq.heappush(q, start_node)

    while q:
        n = heapq.heappop(q)
        x,y = n.pos
        cost = n.cost
        visited[y][x] = True

        adjList = get_adj_coords(n.pos)
        for adjLink in adjList:
            additional_cost = 1

            if adjLink not in map:
                map[adjLink] = Node(adjLink, cost + additional_cost)
            else:
                sn = map[adjLink]
                if cost + additional_cost < sn.cost:
                    sn.pos = adjLink
                    sn.cost = cost + additional_cost

            if not visited[adjLink[1]][adjLink[0]]:
                heapq.heappush(q, Node(adjLink, cost + additional_cost))

    return map



def find(c):
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == c:
                return (x,y)

S=find('S')
E=find('E')

visited = [[False for x in range(WIDTH)] for y in range(HEIGHT)]
costs = dijkstra(visited, Node(S, 0))

count=0
for y in range(HEIGHT):
    for x in range(WIDTH):
        if data[y][x] == '#': continue
        for r in range(20+1):
            for dx in range(r+1):                
                dy = r - dx
                for cheat_x, cheat_y in set([(x+dx,y+dy), (x+dx,y-dy), (x-dx,y+dy), (x-dx,y-dy)]):
                    if cheat_x>=0 and cheat_x<WIDTH and cheat_y>=0 and cheat_y<HEIGHT and data[cheat_y][cheat_x] != '#':
                        saves = costs[(x,y)].cost - costs[(cheat_x,cheat_y)].cost
                        if saves >= 100 + r:
                            count+=1


print(count)

pass