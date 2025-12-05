with open("input.txt", "r") as f:
    data = f.readlines()

res1 = 0
res2 = 0
ranges = []
ids = []
seen = set()

def part1():
    global res1
    for id in ids:
        for rng in ranges:
            l, r = rng
            if l<=id<=r:
                res1+=1
                break

def part2():
    global res2
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    current_l, current_r = sorted_ranges[0]

    for l, r in sorted_ranges[1:]:
        if l <= current_r + 1:
            current_r = max(current_r, r)
        else:
            merged.append((current_l, current_r))
            current_l, current_r = l, r

    merged.append((current_l, current_r))

    res2 = sum(r - l + 1 for l, r in merged)

for line in data:
    line = line.strip()
    if not line:
        continue
    if '-' in line:
        rng = [int(n) for n in line.split("-")]
        ranges.append(rng)
    else:
        ids.append(int(line))

part1()
part2()


print(f"Part 1: {res1}")
print(f"Part 2: {res2}")


