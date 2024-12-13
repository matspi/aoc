import re
import itertools


machines=[]

r =re.compile("Button A:\s+X\+(?P<ax>\d+),\s+Y\+(?P<ay>\d+)\s+Button B:\s+X\+(?P<bx>\d+),\s+Y\+(?P<by>\d+)\s+Prize:\s+X=(?P<x>\d+),\s+Y=(?P<y>\d+)")

with open("13/13_input.txt", "r") as f:
  data = f.read()
  
machines = r.finditer(data)

def check_machine(m):
    ax=int(m.group("ax"))
    ay=int(m.group("ay"))
    bx=int(m.group("bx"))
    by=int(m.group("by"))
    
    x=int(m.group("x")) + 10000000000000
    y=int(m.group("y")) + 10000000000000
    
    det = ax*by - ay*bx
    da = x*by - y*bx
    db= y*ax - x*ay
    
    
    if det == 0 or da%det != 0 or db%det != 0:
        return 0
    
    a=da//det
    b=db//det
    
    return 3*a+b
    
result=0
for m in machines:   
    s=check_machine(m)
    result += s
    
    
print(result)