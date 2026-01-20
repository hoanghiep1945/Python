for _ in range(int(input())) :
    s = input()
    a=list(map(int,input().split()))
    d=[0]*1000000
    tmp = 0
    cr = 0
    for c in a :
        d[c]+=1
        if d[c] > tmp  or (d[c]==tmp and c<cr):
            tmp = d[c]
            cr=c
    if max(d) > len(a)//2: print(cr)
    else : print("NO")