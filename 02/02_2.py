import copy

data=[]
with open("02_1_input copy.txt", "r") as f:
  for line in f.readlines():
    record = [int(e.strip()) for e in line.split(" ")]
    data.append(record)


def is_safe(r):
  if r[0] < r[1] and abs(r[0] - r[1]) <=3:
# increasing
    for i in range(1, len(r)-1):
      if r[i] >= r[i+1] or abs(r[i] - r[i+1]) > 3:
        break
    else:
      return True
  if r[0] > r[1] and abs(r[0] - r[1]) <=3:
# increasing
    for i in range(1, len(r)-1):
      if r[i] <= r[i+1] or abs(r[i] - r[i+1]) > 3:
        break
    else:
      return True
  return False

safe=0
for r in data:
  if is_safe(r):
    safe += 1
    continue
  else:
    for i in range(len(r)):
      new_r = copy.copy(r)
      del(new_r[i])
      if is_safe(new_r):
        safe += 1
        break


print(safe)