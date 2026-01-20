for _ in range(int(input())) :
    s = input()
    a = list(map(int,input().split()))
    d = [0]*1000000
    for c in a :
        d[c]+=1
    for c in a :
        if(d[c]%2 == 1):
            print(c)
            break