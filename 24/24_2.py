import re
from itertools import product

re_wire = re.compile(r"(?P<wire>.{3}): (?P<val>\d)")
re_gate = re.compile(r"(?P<in1>.{3}) (?P<op>AND|OR|XOR) (?P<in2>.{3}) -> (?P<out>.{3})")

GATES = {}
with open("24/24_input.txt", "r") as f:
    for l in f.readlines():
        if l=="": continue
        
        # m = re_wire.match(l)
        # if m:
        #     w = m.group("wire")
        #     v = int(m.group("val"))
            
        #     def l_gen(v):
        #         return lambda: v
            
        #     VALUES[w] = l_gen(v)
            
        m = re_gate.match(l)
        if m:
            in1 = m.group("in1")
            in2 = m.group("in2")
            op = m.group("op")
            out = m.group("out")
            
            GATES[out] = (in1, in2, op)

def is_wire(g):
    return g.startswith('x') or g.startswith('y')

def is_out(g):
    return g.startswith('z')

def get_pos(g):
    assert(is_out(g) or is_wire(g))
    return int(g[1:])

def check_xor(g, pos):
    if is_wire(g):
        return False
    in1, in2, op = GATES[g]
    return op=='XOR' and is_wire(in1) and pos == get_pos(in1) and is_wire(in2) and pos == get_pos(in2)

def check_and_carry(g, pos):
    if is_wire(g):
        return False
    in1, in2, op = GATES[g]
    return op == 'AND' and is_wire(in1) and pos == get_pos(in1) and is_wire(in2) and pos == get_pos(in2)

def check_carry_chain(g, pos):
    if is_wire(g):
        return False
    in1, in2, op = GATES[g]
    return op == 'AND' and check_xor(in1, pos) and check_carry(in2, pos) or check_xor(in2, pos) and check_carry(in1, pos)

def check_carry(g, pos):
    if is_wire(g):
        return False
    in1, in2, op = GATES[g]
    if pos == 1:
        return op=='AND' and is_wire(in1) and get_pos(in1) == 0 and is_wire(in2) and get_pos(in2) == 0
    return op == 'OR' and (
        check_and_carry(in1, pos-1) and check_carry_chain(in2, pos-1) or
        check_and_carry(in2, pos-1) and check_carry_chain(in1, pos-1)
    )

def check_bit(g, pos):
    in1, in2, op = GATES[g]
    if op != 'XOR':
        return False
    if pos == 0:
        return is_wire(in1) and is_wire(in2) 
    return check_xor(in1, pos) and check_carry(in2, pos) or check_xor(in2, pos) and check_carry(in1, pos)

zs = [k for k in GATES if is_out(k)]

def check_gates():
    wrong_bit=0
    for z in sorted(zs):
        if not check_bit(z, get_pos(z)):
            return wrong_bit
        wrong_bit+=1
    return wrong_bit

wrong_gates=[]

for _ in range(4):
    w = check_gates()
    for a,b in product(GATES, GATES):
        GATES[a], GATES[b] = GATES[b], GATES[a]
        now_w = check_gates()
        if now_w > w:
            wrong_gates.append(a)
            wrong_gates.append(b)
            print(a,b, check_gates())
            break
        GATES[a], GATES[b] = GATES[b], GATES[a]

print(check_gates())

print(",".join(sorted(wrong_gates)))
    
