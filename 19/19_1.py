from functools import cache

PATTERNS=[]

with open("19/19_input.txt", "r") as f:
  TOWELS = [t.strip() for t in f.readline().strip().split(", ")]
  f.readline()

  for l in f.readlines():
    PATTERNS.append(l.strip())

@cache
def check(p):
  if p=="":
    return True
  
  ret_val=False
  for t in TOWELS:
    if p.startswith(t):
      ret_val |= check(p[len(t):])
  return ret_val


print([check(p) for p in PATTERNS].count(True))