import re

with open("03/03_input.txt", "r") as f:
    data = f.read()
    
r = re.compile("mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")

sum = 0
enabled = True
for l, r, do, dont in r.findall(data):
    if do != "":
        enabled = True
        continue
    if dont != "":
        enabled = False
        continue
    if enabled:
        sum += int(l) * int(r)
    

print(sum)