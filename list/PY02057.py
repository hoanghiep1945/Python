m,n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(m)]
tmp = max(max(row) for row in a)-min(min(row) for row in a)
ok = 0
for i in range(m):
    for j in range(n):
        if a[i][j] == tmp : 
                ok = 1
if ok == 1 :
    print(tmp)
    for i in range(m):
        for j in range(n):
            if a[i][j] == tmp :
                print(f"Vi tri [{i}][{j}]")
if ok == 0 : print("NOT FOUND")