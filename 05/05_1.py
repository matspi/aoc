rules=[]
updates=[]

in_rules=True
with open("05/05_input.txt", "r") as f:
  for l in f.readlines():
    if l.strip() == "":
      in_rules = False
      continue

    if in_rules:
      before, after = l.split("|")
      rules.append((int(before.strip()), int(after.strip())))
    else:
      updates.append([int(p.strip()) for p in l.split(",")])


def check_update(u):
  for p in u:
    matching_rules = [r for r in rules if r[0] == p]
    later_pages = u[u.index(p)+1:]
    for l in later_pages:
      if len([r for r in matching_rules if r[1] == l]) == 0:
        return False
  return True
      
sum = 0
for u  in updates:
  if check_update(u):
    sum += u[len(u) // 2]

print(sum)