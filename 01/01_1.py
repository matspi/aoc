


left=[]
right=[]

with open("input_01_1.txt", "r") as input:
  for line in input.readlines():
    l, r = line.split("   ")
    left.append(int(l.strip()))
    right.append(int(r.strip()))

left.sort()
right.sort()

distance=0
for i in range(len(left)):
  d=abs(left[i] - right[i])
  distance += d


print(distance)