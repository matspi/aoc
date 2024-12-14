import re
from math import ceil, floor
import time

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
        
def show(robots):
    coords = set([r[0] for r in robots])
    if len(coords) != len(robots):
        return
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x,y) in coords:
                print("*",end="")
            else:
                print(".",end="")
        print()
    print()
    print()
    input()
    
    
for i in range(1000000):
    robots = tick(robots)
    print(i)
    show(robots)
    