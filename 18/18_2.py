import heapq

WIDTH=71
HEIGHT=71

def check(data):




    DIRS=((0,-1), (-1,0), (0,1), (1,0))

    def get_adj_coords(pos):
        ret_val=[]
        x,y=pos
        search_list=['.']
        
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
            self.h = WIDTH-pos[0] + HEIGHT-pos[1] + self.cost

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

            
            # print(x,y, sum([i.count(True) for i in visited]))

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

    start_node=Node((0,0), 0)
    visited = [[False for x in range(WIDTH)] for y in range(HEIGHT)] 

    costs = dijkstra(visited, start_node)

    return ((WIDTH-1, HEIGHT-1)) in costs.keys()


data=[['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
with open("18/18_input.txt", "r") as f:
    for i, l in enumerate(f.readlines()):
        # if i>= bytes: break
        x,y=l.strip().split(",")
        data[int(y)][int(x)] = '#'
        
        if i>=1024:
            print(i)
            if not check(data):
                print(l)
                break
            
