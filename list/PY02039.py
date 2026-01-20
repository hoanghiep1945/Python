n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
k = int(input())
tmp1 = 0
tmp2 = 0
for i in range(n):
    for j in range(i+1,n):
        tmp1 += a[i][j]
for i in range(n):
    for j in range(i):
        tmp2 += a[i][j]
kq = abs(tmp1-tmp2)
if(kq < k) : print("YES")
else : print("NO")
print(kq)