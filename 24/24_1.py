import re

re_wire = re.compile(r"(?P<wire>.{3}): (?P<val>\d)")
re_gate = re.compile(r"(?P<in1>.{3}) (?P<op>AND|OR|XOR) (?P<in2>.{3}) -> (?P<out>.{3})")

VALUES = {}

with open("24/24_input.txt", "r") as f:
    for l in f.readlines():
        if l=="": continue
        
        m = re_wire.match(l)
        if m:
            w = m.group("wire")
            v = int(m.group("val"))
            
            def l_gen(v):
                return lambda: v
            
            VALUES[w] = l_gen(v)
            
           

            
        m = re_gate.match(l)
        if m:
            in1 = m.group("in1")
            in2 = m.group("in2")
            op = m.group("op")
            out = m.group("out")
            
            def l_gen(in1, in2, op):      
                if op == "AND":
                    return lambda: VALUES[in1]() & VALUES[in2]()
                elif op == 'OR':
                    return lambda: VALUES[in1]() | VALUES[in2]()
                elif op == 'XOR':
                    return lambda: VALUES[in1]() ^ VALUES[in2]()
                
            VALUES[out] = l_gen(in1, in2, op)
            
            
zs = [k for k in VALUES.keys() if k.startswith("z")]
zs.sort()

result=0
for z in zs:
    pos = int(z[1:])
    result |= (VALUES[z]() << pos)
    
print(result)