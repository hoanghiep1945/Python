import math

def nto(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

m,n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(m)]
tmp = 0
ok = 0
for i in range(m):
    for j in range(n):
        if nto(a[i][j]) : 
            if a[i][j]>tmp : 
                tmp = a[i][j]
                ok = 1
if ok == 1 :
    print(tmp)
    for i in range(m):
        for j in range(n):
            if a[i][j] == tmp :
                print(f"Vi tri [{i}][{j}]")
if ok == 0 : print("NOT FOUND")