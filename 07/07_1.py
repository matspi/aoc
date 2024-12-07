import itertools 
import math
from joblib import Parallel, delayed
from joblib_progress import joblib_progress
data=[]
skipped=0
with open("07/07_input.txt", "r") as f:
  for l in f.readlines():
    l, r = l.split(":")

    result = int(l.strip())

    values = [int(v.strip()) for v in r.strip().split(" ")]

    if result < sum(values):
      skipped += 1
      continue
    if result > math.prod(values):
      skipped += 1
      continue

    data.append((result, values))

print(f"Entries: {len(data)}, skipped: {skipped}")

operations = [int.__add__, int.__mul__]

def check_entry(r, v):
  num_operations = len(v)-1

  for ops in itertools.product(operations, repeat=num_operations):
    result = v[0]
    for i in range(len(ops)):
      result = ops[i](result, v[i+1])
      if result > r:
        break
    if r == result:
        return r
  return 0


with joblib_progress("Calculating, ...", total=len(data)):
  results = Parallel(n_jobs=16)(delayed(check_entry)(r,v) for r,v in data)
print(sum(results))