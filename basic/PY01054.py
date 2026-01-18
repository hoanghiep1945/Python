for _ in range(int(input())) :
    cnt = 1
    s = input()
    for i in range(0,len(s)) :
        if(s[i] == '0') : continue
        else : cnt *= int(s[i])  
    print(cnt)