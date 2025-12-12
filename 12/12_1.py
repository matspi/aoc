gifts = []
trees = []
with open("input_12.txt") as f:
    lines = f.readlines()

    cntr = 0

    for i in range(6):
        line = lines[cntr]
        gift_no = int(line.split(":")[0])
        gift_layout = [l.strip() for l in lines[cntr + 1 : cntr + 4]]
        gift_area = sum([l.count("#") for l in gift_layout])

        gifts.append((gift_layout, gift_area))

        cntr += 5

    while cntr < len(lines):
        tree_size = [int(e) for e in lines[cntr].split(":")[0].split("x")]
        tree_gifts = [int(e) for e in lines[cntr].split(":")[1].strip().split(" ")]

        trees.append((tree_size, tree_gifts))
        cntr += 1


impossible = 0
for ts, tg in trees:
    x, y = ts
    tree_area = x * y

    gift_area = 0
    for i, g in enumerate(tg):
        gift_area += g * gifts[i][1]

    if gift_area > tree_area:
        impossible += 1


print(len(trees) - impossible)
