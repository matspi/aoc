from collections import deque
from itertools import product

with open("21/21_input.txt", "r") as f:
  codes = [l.strip() for l in f.readlines()]

DIRS=[(0,1,'v'), (-1,0,'<'), (0,-1,'^'), (1,0,'>')]

KP1= (
  (   7, 8,  9),
  (   4, 5,  6),
  (   1, 2,  3),
  (None, 0, 'A')
)

KP2= (
  (None, '^', 'A'),
  ( '<', 'v', '>')
)

def valid_coord(x,y,kp):
  return x>=0 and x < len(kp[0]) and y>=0 and y<len(kp) and kp[y][x] != None

def find_shortest(kp):
  keys={}
  for y in range(len(kp)):
    for x in range(len(kp[0])):
      keys[kp[y][x]] = (x,y)

  presses={}
  for start in keys:
    for end in keys:
      if start == None or end == None:
        continue
      if start == end:
        presses[(start, end)] = ['A']
        continue
      shortest = 10**9

      choices=[]
      q = deque()
      q.append((keys[start][0], keys[start][1], ''))
      while q:
        x,y,p = q.popleft()
        for dx,dy,d in DIRS:
          new_x = x+dx
          new_y = y+dy
          if not valid_coord(new_x, new_y, kp):
            continue
          if kp[new_y][new_x] == end:
            if shortest < len(p) + 1:
              break
            else:
              shortest = len(p) + 1
              choices.append(p + d + 'A')
          else:
            q.append((new_x, new_y, p + d))
        else:
          continue
        break

      presses[(start, end)] = choices
  return presses


shortest_kp1 = find_shortest(KP1)
shortest_kp2 = find_shortest(KP2)
shortest_kp3 = find_shortest(KP2)


def press_keys(seq, shortest):
  start='A'
  kp=[]
  for i, s in enumerate(seq):
    presses_kp = shortest[(start, s)]
    kp.append(presses_kp)
    start=s
  presses=["".join(p) for p in product(*kp)]
  return presses

def press_code(code):
  c = [int(i) for i in code if i!='A']
  c.append('A')
  kp1 = press_keys(c, shortest_kp1)
  
  kp2=[]
  for p1 in kp1:
    kp2.extend(press_keys(p1, shortest_kp2))

  kp3=[]
  for p2 in kp2:
    kp3.extend(press_keys(p2, shortest_kp3))

  lens=[len(p) for p in kp3]
  minlen = min(lens)

  int_part=int(code.rstrip('A'))

  return minlen*int_part


result=0
for c in codes:
  result += press_code(c)

print(result)