import re
from math import ceil, floor

WIDTH = 101
HEIGHT = 103

robots = []

regex = re.compile("p=(?P<x>\d+),(?P<y>\d+) v=(?P<vx>-?\d+),(?P<vy>-?\d+)")
with open("14/14_input.txt", "r") as f:
    data=f.read()
    for r in regex.finditer(data):
        x=int(r.group("x"))
        y=int(r.group("y"))
        vx=int(r.group("vx"))
        vy=int(r.group("vy"))
        
        robots.append(((x,y), (vx,vy)))
        
def tick(robots):
    new_robots=[]
    
    for pos,vel in robots:
        x,y = pos
        vx,vy = vel
        
        new_x = (x + vx) % WIDTH
        new_y = (y + vy) % HEIGHT
        
        new_robots.append(((new_x,new_y), (vx,vy)))
    return new_robots
        
def get_quadrant(r):
    x,y=r[0]
    if x<floor(WIDTH/2):
        if y<floor(HEIGHT/2):
            return 1
        elif y>=ceil(HEIGHT/2):
            return 3
    elif x>=ceil(WIDTH/2):
        if y<floor(HEIGHT/2):
            return 2
        elif y>=ceil(HEIGHT/2):
            return 4     
    return 0  

for i in range(100):
    robots = tick(robots)
    
q=[get_quadrant(r) for r in robots]

result = q.count(1) * q.count(2) * q.count(3) * q.count(4)

print(result)