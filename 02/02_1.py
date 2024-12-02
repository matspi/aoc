
data=[]
with open("02_1_input.txt", "r") as f:
  for line in f.readlines():
    record = [int(e.strip()) for e in line.split(" ")]
    data.append(record)

safe=0

for r in data:
  if r[0] < r[1] and abs(r[0] - r[1]) <=3:
    # increasing
    for i in range(1, len(r)-1):
      if r[i] >= r[i+1] or abs(r[i] - r[i+1]) > 3:
        break
    else:
      safe += 1
  if r[0] > r[1] and abs(r[0] - r[1]) <=3:
    # increasing
    for i in range(1, len(r)-1):
      if r[i] <= r[i+1] or abs(r[i] - r[i+1]) > 3:
        break
    else:
      safe += 1


print(safe)