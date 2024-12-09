

with open("09/09_input.txt", "r") as f:
  data = f.readline().strip()

blocks = [int(e) for e in data[0::2]]
freespace = [int(e) for e in data[1::2]]

result = []

expanded_blocks=[]
for i, block in enumerate(blocks):
  expanded_blocks.extend([i] * block)

for i, (b,f) in enumerate(zip(blocks, freespace)):
  if len(expanded_blocks) == 0:
    break

  # block
  result.extend(expanded_blocks[:b])
  expanded_blocks = expanded_blocks[b:]
  # fill freespace
  for n in range(f):
    if len(expanded_blocks) == 0:
      break
    result.append(expanded_blocks.pop())

  # print(result)
  None


checksum=0
for i,n in enumerate(result):
  checksum += i*n

print(checksum)