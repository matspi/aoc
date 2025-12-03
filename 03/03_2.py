sum = 0


def find_biggest(line, start_index, max_index):
    idx = 0
    num = 0
    for i, c in enumerate(line[start_index:]):
        if len(line) - i - start_index < max_index:
            break
        if int(c) > num:
            num = int(c)
            idx = i + start_index

    return num, idx


sum = 0
with open("input_03_1.txt", "r") as input:

    for line in input.readlines():
        num = 0
        line = line.strip()
        idx = -1
        for i in range(12):
            n, idx = find_biggest(line, idx + 1, 12 - i)
            num += 10 ** (11 - i) * n

        sum += num

print(sum)
