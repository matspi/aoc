


left=[]
right=[]

with open("input_01_2.txt", "r") as input:
  for line in input.readlines():
    l, r = line.split("   ")
    left.append(int(l.strip()))
    right.append(int(r.strip()))


similarity=0
for i in range(len(left)):
  s = left[i] * right.count(left[i])
  similarity += s


print(similarity)