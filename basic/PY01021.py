for _ in range(int(input())) :
    s = input()
    cnt = 0
    v=[]
    for i in range(len(s)):
        if s[i].isdigit() : cnt += int(s[i])
        else : v.append(s[i])
    v.sort()
    print("".join(v),end="")
    print(cnt)