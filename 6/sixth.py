import math
with open("input.txt", "r") as f:
    data = f.readlines()

res1 = 0
res2 = 0

matrix1 = []
matrix2 = []
matrix3 = []
lens = []

for line in data:
    line = line.strip().split()
    if not line:
        continue
    matrix1.append(line)
n = len(matrix1)
m = len(matrix1[0])

for line in data:
    line = line.strip("\n")
    if not line:
        continue
    matrix2.append(line)

i = 1
idx = 1
while(idx<len(matrix2[n-1])):
    if matrix2[n-1][idx]!=" " and i!=1:
        lens.append(i)
        i=1
        idx+=1
    else:
        i+=1
        idx+=1
    if idx == len(matrix2[n-1]):
        lens.append(i)
        break
for i in range(n-1):
    start = 0
    currline = []
    for dist in lens:
        currline.append(matrix2[i][start:start+dist])
        start+=dist
    matrix2[i]=currline
matrix2[n-1]=matrix2[n-1].split()



def part1():
    global res1
    for i in range(m):
        if (matrix1[n-1][i] == "+"):
            curr = 0
            for j in range(n-1):
                curr += int(matrix1[j][i])
            res1 += curr
        if (matrix1[n-1][i] == "*"):
            curr = 1
            for j in range(n-1):
                curr *= int(matrix1[j][i])
            res1 += curr

def part2():
    global res2
    for j,k in zip(range(m), lens):
        currline = []
        for l in range(k):
            num = 0
            for i in range(n-1):
                if matrix2[i][j][l]!=" ":
                    num = num*10 + int(matrix2[i][j][l])
            if num != 0:
                currline.append(num)
        if matrix2[n-1][j] == "+":
            res2+=sum(currline)
        if matrix2[n-1][j] == "*":
            res2+=math.prod(currline)

part1()
part2()

print(f"Part 1: {res1}")
print(f"Part 2: {res2}")

