
with open("22/22_input.txt", "r") as f:
  input=[int(l.strip()) for l in f.readlines()]


def mix(s, n):
  return s^n

def prune(s):
  return s%16777216

def step1(s):
  return prune(mix(s, s*64))

def step2(s):
  return prune(mix(s, s//32))

def step3(s):
  return prune(mix(s, s*2048))

def evolve(s):
  return step3(step2(step1(s)))


result=0
for i in input:
  s=i
  for _ in range(2000):
    s=evolve(s)
  print(s)
  result+=s

print(result)