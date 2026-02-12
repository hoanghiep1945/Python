m, n = map(int, input().split())
a = []
for _ in range(m):
    a.append(list(map(int, input().split())))

dirs = [(-1,-1), (-1,0), (-1,1),
        (0,-1), (0,1),
        (1,-1), (1,0), (1,1)]

total = 0
for i in range(m):
    for j in range(n):
        if a[i][j] == -1:
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n and a[ni][nj] >= 0:
                    total += a[ni][nj]

print(total)