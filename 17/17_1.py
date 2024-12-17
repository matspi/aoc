import re

reg_regex=re.compile("Register (?P<reg>[A-C]): (?P<val>\d+)")
prog_regex=re.compile("Program: (?P<ops>[\d,]*)")
with open("17/17_input.txt", "r") as f:
    data = f.read()
    
REGISTERS={}    
PROG=[]
PC=0

OUT=[]

for r in reg_regex.finditer(data):
    reg = r.group("reg")
    v = int(r.group("val"))
    REGISTERS[reg] = v
    
ops = prog_regex.findall(data)[0]
PROG=[int(o) for o in ops.split(",")]

def get_literal():
    return PROG[PC+1]

def get_combo():
    l=get_literal()
    if l>=0 and l<=3:
        return l
    elif l==4:
        return REGISTERS['A']
    elif l==5:
        return REGISTERS['B']
    elif l==6:
        return REGISTERS['C']

def adv():
    REGISTERS['A'] = REGISTERS['A'] // (2**get_combo())
    
def bxl():
    REGISTERS['B'] = REGISTERS['B'] ^ get_literal()
    
def bst():
    REGISTERS['B'] = get_combo() % 8
    
def jnz():
    global PC
    if REGISTERS['A'] == 0:
        return
    PC = get_literal() - 2
    
def bxc():
    REGISTERS['B'] = REGISTERS['B'] ^ REGISTERS['C']
    
def out():
    OUT.append(get_combo() % 8)
    
def bdv():
    REGISTERS['B'] = REGISTERS['A'] // (2**get_combo())
    
def cdv():
    REGISTERS['C'] = REGISTERS['A'] // (2**get_combo())
    
OPS={0: adv, 1:bxl, 2:bst, 3:jnz, 4:bxc, 5:out, 6:bdv, 7:cdv}

def op():
    global PC
    opcode = PROG[PC]
    op = OPS[opcode]
    op()
    PC+=2
    
    return PC<len(PROG)

rv=op()
while rv:
    rv=op()
    
print(",".join([str(s) for s in OUT]))