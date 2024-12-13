

with open("04/04_input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

    
SEARCH = "MAS"
    
def coord_valid(x, y):
    return x>=0  and x<len(data[0]) and y>=0 and y<len(data)
    
def find_mas(i, x, y, dir_x, dir_y):
    if i == len(SEARCH):
        return True
    
    if coord_valid(x, y) and SEARCH[i] == data[y][x]:
        return find_mas(i+1, x+dir_x, y+dir_y, dir_x, dir_y)
    
    return False

def find_character(x, y, c):
    return coord_valid(x,y) and data[y][x] == c

x_dirs = [-1, -1, 1, 1]
y_dirs = [-1, 1, -1, 1]

found=0
for y in range(len(data)):
    for x in range(len(data[0])):
        
        if data[y][x] == 'A':
            finds = [find_mas(0, x-x_dirs[k], y-y_dirs[k], x_dirs[k], y_dirs[k])  for k in range(len(x_dirs))]
            if finds.count(True) == 2:
                found += 1
                
                
print(found)