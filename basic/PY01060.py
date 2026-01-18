for _ in range(int(input())) :
    n = input()
    cnt = 0
    tmp = 1
    for i in range(0,len(n)):
        if(i%2 == 0 and n[i]=='0') : continue
        if(i%2 == 0) : tmp*= int(n[i])
        if(i%2 == 1) : cnt += int(n[i])
    print(f"{tmp} {cnt}")