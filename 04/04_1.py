

with open("04/04_input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

    
SEARCH = "XMAS"
    
def coord_valid(x, y):
    return x>=0  and x<len(data[0]) and y>=0 and y<len(data)
    
def findXmas(i, x, y, dir_x, dir_y):
    if i == len(SEARCH):
        return True
    
    if coord_valid(x, y) and SEARCH[i] == data[y][x]:
        return findXmas(i+1, x+dir_x, y+dir_y, dir_x, dir_y)
    
    return False

x_dirs = [-1, -1, -1, 0, 0, 1, 1, 1]
y_dirs = [-1, 0, 1, -1, 1, -1, 0, 1]

found=0
for y in range(len(data)):
    for x in range(len(data[0])):
        for dir in range(len(x_dirs)):
            if findXmas(0, x, y, x_dirs[dir], y_dirs[dir]):
                found += 1
                
print(found)