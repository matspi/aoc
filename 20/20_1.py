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

orig_data = copy.deepcopy(data)

def apply_cheat(pos1):
    global data
    data=copy.deepcopy(orig_data)

    data[pos1[1]][pos1[0]]='1'
    


def check_cheat():
    visited = [[False for x in range(WIDTH)] for y in range(HEIGHT)] 
    costs = dijkstra(visited, Node(S, 0))
    return costs[E].cost


def possible_cheats():
    cheats=set()
    for y in range(1,HEIGHT-1):
        for x in range(1, WIDTH-1):
            if data[y][x] == '#':
                # for d in DIRS:
                #     old_x=x-d[0]
                #     old_y=y-d[1]
                #     new_x=x+d[0]
                #     new_y=y+d[1]

                #     if data[old_y][old_x] == '.' and data[new_y][new_x] == '.':
                cheats.add((x,y))

    return cheats


cheats=possible_cheats()
baseline = check_cheat()

print("Possible cheats: ", len(cheats))
print("Baseline: ", baseline)


results = []
for p1 in cheats:
    apply_cheat(p1)
    with_cheat = check_cheat()
    results.append(baseline - with_cheat)

print(len([i for i in results if i>=100]))

pass