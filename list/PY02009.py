for _ in range(int(input())) :
    n = int(input())
    s=set()
    d = [0]*1001
    for _ in range(n) :
        x = int(input())
        s.add(x)
        d[x]+=1
    tmp = max(s)
    
    for c in s:
        if(d[c] == d[tmp] and c < tmp): tmp = c
        if(d[c] > d[tmp] ): tmp = c
    print(tmp)