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
    
    x=int(m.group("x"))
    y=int(m.group("y"))
    
    answ=10**32
    
    for a,b in itertools.product(range(100), range(100)):
        if a*ax+b*bx == x and a*ay+b*by==y:
            answ = min(answ, 3*a+b)
            
    if answ == 10**32:
        return 0
    else:
        return answ
    
result=0
for m in machines:   
    s=check_machine(m)
    result += s
    
    
print(result)