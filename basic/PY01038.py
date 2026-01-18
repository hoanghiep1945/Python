for _ in range(int(input())) :
    n = int(input())
    cnt = 0
    while (n%7 != 0) and (cnt < 1000) :
        n = n + int(str(n)[::-1])
    if(cnt == 1000) : print(-1)
    else : print(n)