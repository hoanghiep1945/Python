for _ in range(int(input())):
    s = input().strip()
    tmp = s[0]
    cnt = 0

    for c in s:
        if c == tmp:
            cnt += 1
        else:
            print(cnt, tmp, sep="", end="")
            tmp = c
            cnt = 1
#sep="" là in ra 2 phần tử liền nhau
    print(cnt, tmp, sep="")