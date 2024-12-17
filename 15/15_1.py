
WH=[]
MOVES=""

read_wh=True
with open("15/15_input.txt", "r") as f:
    for line in f.readlines():
        if line.strip() == "":
            read_wh=False
        
        if read_wh:
            WH.append(list(line.strip()))
        else:
            MOVES += line.strip()
            
DIRS={'<':(-1,0), '>': (1,0), '^':(0,-1), 'v':(0,1)}
            
def can_move_box(data, move, pos):
    x,y = pos
    d=DIRS[move]
    count = 0
    while True:
        x = x+d[0]
        y = y+d[1]

        if data[y][x] == '#':
            return False
        if data[y][x] == 'O':
            count+=1
            continue
        if data[y][x] == '.':
            return count
            
def tick(data, move, pos):
    x,y=pos
    
    d = DIRS[move]
    new_x = x+d[0]
    new_y = y+d[1]

    if new_x<0 or new_x>=len(data[0]) or new_y<0 or new_y>=len(data):
        return (x,y)

    if WH[new_y][new_x] == '.':
        WH[new_y][new_x] = '@'
        WH[y][x] = '.'
        
    elif WH[new_y][new_x] == '#':
        new_y=y
        new_x=x

    elif WH[new_y][new_x] == 'O':
        cmb = can_move_box(data, move, pos)
        if cmb == False:
            new_y=y
            new_x=x      
        else:
            WH[y][x] = '.'
            WH[new_y][new_x] = '@'
            next_x=new_x
            next_y=new_y
            for i in range(cmb):
                next_x = next_x+d[0]
                next_y = next_y+d[1]
                
                WH[next_y][next_x] = 'O'
                
    return (new_x, new_y)
                
def count(data):
    result=0
    for y in range(len(WH)):
        for x in range(len(WH[y])):
            if WH[y][x] == 'O':
                result += 100*y + x
    return result

def find_start():
    for y in range(len(WH)):
        for x in range(len(WH[y])):
            if WH[y][x] == '@':
                return (x,y)

pos=find_start()
for m in MOVES:
    pos = tick(WH, m, pos)
    pass
    
print(count(WH))