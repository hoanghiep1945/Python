n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
k = int(input())
tmp1 = 0
tmp2 = 0
for i in range(n):
    for j in range(n):
        if i + j <= n - 1 : tmp1 += a[i][j]
for i in range(n):
    for j in range(n):
         if i + j >= n - 1 : tmp2 += a[i][j]
kq = abs(tmp1-tmp2)
if(kq <= k) : print("YES")
else : print("NO")
print(kq)