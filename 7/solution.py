with open("input.txt", "r") as f:
    data = f.readlines()

res1 = 0
res2 = 0
matrix = []

for line in data:
    line = [(n) for n in line.strip()]
    if not line:
        continue
    matrix.append(line)
n = len(matrix)
m = len(matrix[0])

seen = set()
seen.add(matrix[0].index("S"))


def part1():
    global res1
    for line in matrix[1:]:
        for i in range(len(line)):
            if line[i]=="^" and i in seen:
                res1+=1
                seen.remove(i)
                if i-1>=0:
                    seen.add(i-1)
                if i+1<m:
                    seen.add(i+1)

def part2():
    memo = {}
    def dfs(i, j):
        if j<0 or j>=m:
            return 0
        while(i<n and matrix[i][j]=="."):
            i+=1
        if i>=n:
            return 1
        if (i,j) in memo:
            return memo[(i,j)]
        if matrix[i][j]=="^":
            curr = dfs(i+1, j-1) + dfs(i+1, j+1)
            memo[(i,j)]=curr
            return curr
        return 0
    start = matrix[0].index("S")
    return dfs(1, start)


part1()
res2 = part2()


print(f"Part 1: {res1}")
print(f"Part 2: {res2}")
