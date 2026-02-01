def check(n):
    s = str(n)
    return len(s)>=2 and s==s[::-1]

m,n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(m)]
tmp = 0
ok = 0
for i in range(m):
    for j in range(n):
        if check(a[i][j]) : 
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