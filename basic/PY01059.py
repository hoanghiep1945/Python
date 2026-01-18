for _ in range(int(input())) :
    n = input()
    cnt = 0
    tmp = 1
    for i in range(0,len(n)):
        if(i%2 == 0) : cnt += int(n[i])
        if(i%2 == 1 and n[i]=='0') : continue
        if(i%2 == 1) : tmp *= int(n[i])
    if all(n[i] == '0' for i in range(1,len(n),2)) : tmp=0
    print(f"{cnt} {tmp}")