curr = 50 
count1 = 0
count2 = 0

with open("input.txt", "r") as f:
    data = f.readlines()

for line in data:
    line = line.strip()
    if not line:
        continue
    
    dir = line[0].upper()
    dist = int(line[1:])

    hits = 0
    
    if dir == 'R':
        hits = (curr + dist) // 100
        
    elif dir == 'L':
        if curr == 0:
            hits = dist // 100
        else:
            if dist >= curr:
                hits = 1
                rem = dist - curr
                hits += rem // 100
            else:
                hits = 0

    count2 += hits
        
    if dir == 'R':
        curr = (curr + dist) % 100
    elif dir == 'L':
        curr = (curr - dist) % 100

    if curr == 0:
        count1 += 1

print(f"Part 1: {count1}")
print(f"Part 2: {count2}")
