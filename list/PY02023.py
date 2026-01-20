for _ in range(int(input())) :
    s = input()
    a = list(map(int,input().split()))
    a.sort(key = lambda x : (sum(int(ch) for ch in str(x)),x))
    for c in a :
        print(c,end=" ")
    print("")