with open("input.txt", "r") as f:
    data = f.readlines()

res1 = 0
res2 = 0

def checker1(id):
    global res1
    digits = [int(n) for n in str(id)]
    n = len(digits)
    if n % 2 == 0 and str(id)[: n // 2] * 2 == str(id):
        res1 += id

def checker2(id):
    global res2
    digits = [int(n) for n in str(id)]
    n = len(digits)
    for j in range(1, n//2+1):
        pattern = str(id)[:j]
        if n%len(pattern)!=0:
            continue
        pattern *= n//len(pattern)
        if str(id)==str(pattern):
            res2+=id
            break

for line in data:
    line = line.strip()
    if not line:
        continue
    ranges = line.split(",")
    for id in ranges:
        first, second = [int(n) for n in id.split("-")]
        for i in range(first, second + 1):
            checker1(i)
            checker2(i)

print(f"Part 1: {res1}")
print(f"Part 2: {res2}")

