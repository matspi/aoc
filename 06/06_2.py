from itertools import pairwise
import math

def all_op_indices(op_line):
    return [i for i, ch in enumerate(op_line) if ch in "+*"]

lines=[]
with open("input_06_1.txt") as f:
    lines = f.readlines()
    op_line = lines[-1]

indices = all_op_indices(op_line)
indices.append(len(op_line))

num_len = len(lines)-1
ans=0
for col_start, col_end in pairwise(indices):
    col = [line[col_start:col_end] for line in lines[:-1]]
    op = op_line[col_start:col_end].strip()

    nums=   []
    for c in range(col_end-col_start):
        digits = [col[r][c] for r in range(num_len) if col[r][c].isdigit()]
        if len(digits) == 0:
            continue
        num = int(''.join([col[r][c] for r in range(num_len) if col[r][c].isdigit()]))
        nums.append(num)

    if op == "+":
        ans+= sum(nums)
    elif op == "*":
        ans += math.prod(nums)

print(ans)        