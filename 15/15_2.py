
WH=[]
MOVES=""

read_wh=True
with open("15/15_input.txt", "r") as f:
    for line in f.readlines():
        if line.strip() == "":
            read_wh=False
        
        if read_wh:
            l=[]
            for c in line.strip():
                if c == '#':
                    l.extend(['#','#'])
                elif c == 'O':
                    l.extend(['[',']'])
                elif c == '.':
                    l.extend(['.','.'])
                elif c == '@':
                    l.extend(['@','.'])
                
            WH.append(l)
        else:
            MOVES += line.strip()
            
DIRS={'<':(-1,0), '>': (1,0), '^':(0,-1), 'v':(0,1)}
            
def can_move_box(data, move, pos):
    x,y = pos
    x,y=pos
    if move == '<':
        # only need to look to the left
        if WH[y][x-1] == '#':
            return False
        if WH[y][x-1] == '.':
            # can move
            return True
        if WH[y][x-1] == ']':
            if can_move_box(data, move, (x-2, y)):
                return True
            else:
                return False               
        
    if move == '>':
        # only need to look to the right
        if WH[y][x+1] == '#':
            return False
        if WH[y][x+1] == '.':
            # can move
            return True
        if WH[y][x+1] == '[':
            if can_move_box(data, move, (x+2, y)):
                return True
            else:
                return False
        
    if move == '^':
        if WH[y-1][x] == '.':
            return True
        if WH[y-1][x] == '[':
            if (WH[y-2][x] == '.' and WH[y-2][x+1] == '.') or \
                (WH[y-2][x] == '.' and WH[y-2][x+1] in ('[', ']') and can_move_box(data, move, (x+1,y-1))) or \
                (WH[y-2][x] in ('[', ']') and WH[y-2][x+1] == '.' and can_move_box(data, move, (x,y-1))) or \
                (WH[y-2][x] in ('[', ']') and WH[y-2][x+1] in ('[', ']') and \
                    can_move_box(data, move, (x,y-1)) and can_move_box(data, move, (x+1,y-1))):
                    return True  
            return False
                   
        if WH[y-1][x] == ']':
            if (WH[y-2][x] == '.' and WH[y-2][x-1] == '.') or \
                (WH[y-2][x] == '.' and WH[y-2][x-1] in ('[', ']') and can_move_box(data, move, (x-1,y-1))) or \
                (WH[y-2][x] in ('[', ']') and WH[y-2][x-1] == '.' and can_move_box(data, move, (x,y-1))) or \
                (WH[y-2][x] in ('[', ']') and WH[y-2][x-1] in ('[', ']') and \
                    can_move_box(data, move, (x,y-1)) and can_move_box(data, move, (x-1,y-1))):
                    return True
            else:
                return False
            
    if move == 'v':
        if WH[y+1][x] == '.':
            return True
        if WH[y+1][x] == '[':
            if (WH[y+2][x] == '.' and WH[y+2][x+1] == '.') or \
                (WH[y+2][x] == '.' and WH[y+2][x+1] in ('[', ']') and can_move_box(data, move, (x+1,y+1))) or \
                (WH[y+2][x] in ('[', ']') and WH[y+2][x+1] == '.' and can_move_box(data, move, (x,y+1))) or \
                (WH[y+2][x] in ('[', ']') and WH[y+2][x+1] in ('[', ']') and \
                    can_move_box(data, move, (x,y+1)) and can_move_box(data, move, (x+1,y+1))):
                    return True  
            return False
                   
        if WH[y+1][x] == ']':
            if (WH[y+2][x] == '.' and WH[y+2][x-1] == '.') or \
                (WH[y+2][x] == '.' and WH[y+2][x-1] in ('[', ']') and can_move_box(data, move, (x-1,y+1))) or \
                (WH[y+2][x] in ('[', ']') and WH[y+2][x-1] == '.' and can_move_box(data, move, (x,y+1))) or \
                (WH[y+2][x] in ('[', ']') and WH[y+2][x-1] in ('[', ']') and \
                    can_move_box(data, move, (x,y+1)) and can_move_box(data, move, (x-1,y+1))):

                    return True
            else:
                return False
        
        
def move_box(data, move, pos):
    x,y=pos
    
    if can_move_box(data, move, pos) == False:
        return
    
    if move == '<':
        # only need to look to the left
        if WH[y][x-1] == '#':
            return False
        if WH[y][x-1] == '.':
            # can move
            WH[y][x-1]='['
            WH[y][x]=']'
            return True
        if WH[y][x-1] == ']':
            if move_box(data, move, (x-2, y)):
                WH[y][x-1]='['
                WH[y][x]=']'
                return True
            else:
                return False               
        
    if move == '>':
        # only need to look to the right
        if WH[y][x+1] == '#':
            return False
        if WH[y][x+1] == '.':
            # can move
            WH[y][x+1]=']'
            WH[y][x]='['
            return True
        if WH[y][x+1] == '[':
            if move_box(data, move, (x+2, y)):
                WH[y][x+1]=']'
                WH[y][x]='['
                return True
            else:
                return False
        
    if move == '^':
        if WH[y-1][x] == '.':
            return True
        if WH[y-1][x] == '[':
            if (WH[y-2][x] == '.' and WH[y-2][x+1] == '.') or \
                (WH[y-2][x] == '.' and WH[y-2][x+1] in ('[', ']') and move_box(data, move, (x+1,y-1))) or \
                (WH[y-2][x] in ('[', ']') and WH[y-2][x+1] == '.' and move_box(data, move, (x,y-1))) or \
                (WH[y-2][x] in ('[', ']') and WH[y-2][x+1] in ('[', ']') and \
                    move_box(data, move, (x,y-1)) and move_box(data, move, (x+1,y-1))):
                    
                    WH[y-2][x]='['
                    WH[y-2][x+1]=']'
                    WH[y-1][x]='.'
                    WH[y-1][x+1]='.'
                    return True  
            return False
                   
        if WH[y-1][x] == ']':
            if (WH[y-2][x] == '.' and WH[y-2][x-1] == '.') or \
                (WH[y-2][x] == '.' and WH[y-2][x-1] in ('[', ']') and move_box(data, move, (x-1,y-1))) or \
                (WH[y-2][x] in ('[', ']') and WH[y-2][x-1] == '.' and move_box(data, move, (x,y-1))) or \
                (WH[y-2][x] in ('[', ']') and WH[y-2][x-1] in ('[', ']') and \
                    move_box(data, move, (x,y-1)) and move_box(data, move, (x-1,y-1))):
                    
                    WH[y-2][x]=']'
                    WH[y-2][x-1]='['
                    WH[y-1][x]='.'
                    WH[y-1][x-1]='.'
                    return True
            else:
                return False
            
    if move == 'v':
        if WH[y+1][x] == '.':
            return True
        if WH[y+1][x] == '[':
            if (WH[y+2][x] == '.' and WH[y+2][x+1] == '.') or \
                (WH[y+2][x] == '.' and WH[y+2][x+1] in ('[', ']') and move_box(data, move, (x+1,y+1))) or \
                (WH[y+2][x] in ('[', ']') and WH[y+2][x+1] == '.' and move_box(data, move, (x,y+1))) or \
                (WH[y+2][x] in ('[', ']') and WH[y+2][x+1] in ('[', ']') and \
                    move_box(data, move, (x,y+1)) and move_box(data, move, (x+1,y+1))):
                    
                    WH[y+2][x]='['
                    WH[y+2][x+1]=']'
                    WH[y+1][x]='.'
                    WH[y+1][x+1]='.'
                    return True  
            return False
                   
        if WH[y+1][x] == ']':
            if (WH[y+2][x] == '.' and WH[y+2][x-1] == '.') or \
                (WH[y+2][x] == '.' and WH[y+2][x-1] in ('[', ']') and move_box(data, move, (x-1,y+1))) or \
                (WH[y+2][x] in ('[', ']') and WH[y+2][x-1] == '.' and move_box(data, move, (x,y+1))) or \
                (WH[y+2][x] in ('[', ']') and WH[y+2][x-1] in ('[', ']') and \
                    move_box(data, move, (x,y+1)) and move_box(data, move, (x-1,y+1))):
                    
                    WH[y+2][x]=']'
                    WH[y+2][x-1]='['
                    WH[y+1][x]='.'
                    WH[y+1][x-1]='.'
                    return True
            else:
                return False
            
def tick(data, move, pos):
    # show(WH)
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

    elif WH[new_y][new_x] in ('[',']'):
        if move_box(data, move, pos):

            WH[y][x] = '.'
            WH[new_y][new_x] = '@'  

        else:
            new_y=y
            new_x=x
                
    return (new_x, new_y)
                
def count(data):
    result=0
    for y in range(len(WH)):
        for x in range(len(WH[y])):
            if WH[y][x] == '[':
                result += 100*y + x
    return result

def find_start():
    for y in range(len(WH)):
        for x in range(len(WH[y])):
            if WH[y][x] == '@':
                return (x,y)

def show(data):
    for y in range(len(data)):
        l=""
        for x in range(len(data[y])):
            l += data[y][x]
        print(l)
        
import time
pos=find_start()
for i,m in enumerate(MOVES):

    pos = tick(WH, m, pos)

    # time.sleep(0.1)
    
    
print(count(WH))