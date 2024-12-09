from itertools  import zip_longest, chain

with open("09/09_input.txt", "r") as f:
  data = f.readline().strip()

blocks = [int(e) for e in data[0::2]]
freespace = [int(e) for e in data[1::2]]


freeblocks = [([0]*f) for i,f in enumerate(freespace)]
expanded_blocks = [[i]*b for i,b in enumerate(blocks)]


for b in range(len(expanded_blocks)-1,0,-1):
  l = len(expanded_blocks[b])
  block = expanded_blocks[b]
  for i in range(len(freeblocks)):
    if b < i: break
    f = freeblocks[i]
    if f.count(0) >= l:
      freeblocks[i] = f[:f.index(0)] + block + [0]*(f.count(0)-l)
      expanded_blocks[b] = [0] * len(block)
      break

merged = [i for sub in zip(expanded_blocks, freeblocks) for i in sub if i]
flat = chain.from_iterable(merged)

checksum=0
for i,n in enumerate(flat):
  checksum += i*n

print(checksum)
