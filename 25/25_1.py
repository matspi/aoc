from itertools import product


keys=[]
locks=[]

def read_key(f):
    key=[5]*5
    for _ in range(6):
        l = f.readline()
        for i in range(5):
            if l[i] == '.':
                key[i]-=1
    keys.append(key)

def read_lock(f):
    lock=[0]*5
    for _ in range(6):
        l = f.readline()
        for i in range(5):
            if l[i] == '#':
                lock[i] += 1
    locks.append(lock)
    

with open("25/25_input.txt", "r") as f:
    while not f.closed:
        first = f.readline()
        if first=="":break
        if first.startswith("#"):
            read_lock(f)
        else:
            read_key(f)
        f.readline()
           
           
def fits(lock, key):
    for i in range(len(lock)):
        if lock[i] + key[i] >= 6:
            return False
        
    return True 

count=0           
for l, k in product(locks, keys):
    if fits(l, k):
        count+=1
        
print(count)
        