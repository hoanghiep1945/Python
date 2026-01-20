for _ in range(int(input())) :
    s = input()
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    ok = 0
    for i in range(len(a)) :
        if(a[i] > b[i]) : 
            ok = 1
            print("NO")
            break
    if(ok == 0) : print("YES")