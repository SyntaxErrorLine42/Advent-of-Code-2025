from collections import deque

with open("input.txt", "r") as f:
    data = f.readlines()

res1 = 0
res2 = 0
matrix = []
q = deque()
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
change = False
toRemove = []


def bfs1(i, j):
    global res1
    cnt = 0
    for dir in dirs:
        dx, dy = dir
        nx, ny = i + dx, j + dy
        if nx >= 0 and nx < n and ny >= 0 and ny < m and matrix[nx][ny] == "@":
            cnt += 1
    if cnt < 4:
        res1 += 1


def bfs2(i, j):
    global res2
    cnt = 0
    for dir in dirs:
        dx, dy = dir
        nx, ny = i + dx, j + dy
        if nx >= 0 and nx < n and ny >= 0 and ny < m and matrix[nx][ny] == "@":
            cnt += 1
    if cnt < 4:
        res2 += 1
        toRemove.append([i, j])


for line in data:
    line = line.strip()
    if not line:
        continue
    matrix.append(list(line))

n = len(matrix)
m = len(matrix[0])

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "@":
            bfs1(i, j)


for i in range(n):
    for j in range(m):
        if matrix[i][j] == "@":
            bfs2(i, j)
while len(toRemove) != 0:
    change = True
    rx, ry = toRemove.pop()
    matrix[rx][ry] = "."
while (change):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "@":
                bfs2(i, j)
    change = False
    while len(toRemove) != 0:
        change = True
        rx, ry = toRemove.pop()
        matrix[rx][ry] = "."

print(f"Part 1: {res1}")
print(f"Part 2: {res2}")
