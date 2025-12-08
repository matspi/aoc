ingreds = []
ranges = []
with open("input_05_1.txt", "r") as input:
    read_ranges = True
    for line in input.readlines():
        if line.strip() == "":
            read_ranges = False
            break

        if read_ranges:
            r = [int(i) for i in line.strip().split("-")]
            ranges.append(r)
        else:
            ingreds.append(int(line.strip()))


ranges.sort()
maxi = 0

count = 0
for r in ranges:
    maxi = max(maxi, r[0])
    if maxi <= r[1]:
        count += r[1] - maxi + 1
        maxi = r[1] + 1

print(count)
