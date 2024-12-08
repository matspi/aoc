
data = []
with open("08/08_input.txt", "r") as f:
  for l in f.readlines():
    data.append(list(l.strip()))

def valid_coords(ant):
  x=ant[0]
  y=ant[1]
  return x>=0 and x<len(data[0]) and y>=0 and y<len(data)    

def find_other_antennas(x_in,y_in, freq):
  antennas=[]
  for y in range(len(data)):
    for x in range(len(data[y])):
      if x!=x_in and y!=y_in and data[y][x] == freq:
        antennas.append((x,y))

  return antennas

def distance(ant1, ant2):
  return (ant1[0] - ant2[0], ant1[1] - ant2[1])

def calculate_antinodes(ant1, ant2):
  dist = distance(ant1, ant2)
  return (ant1[0] + dist[0], ant1[1] + dist[1]), (ant2[0] - dist[0], ant2[1] - dist[1])

all_antinodes={}

for y in range(len(data)):
  for x in range(len(data[y])):
    if data[y][x] != '.':
      freq = data[y][x]
      other_antennas = find_other_antennas(x,y, freq)
      if freq not in all_antinodes.keys():
        all_antinodes[freq] = []

      for ant in other_antennas:
        antinodes = calculate_antinodes((x,y), ant)
        for n in antinodes:
          if valid_coords(n):
            all_antinodes[freq].append(n)

unique=set()
for freq in all_antinodes.keys():
  for i in all_antinodes[freq]:
    unique.add(i)

# print(all_antinodes)
# print(unique)
print(len(unique))
