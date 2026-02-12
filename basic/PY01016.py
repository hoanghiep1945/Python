for _ in range(int(input())):
    s = input()
    tmp = ""
    for c in s :
        if c.isalpha() :
            tmp = c
        else:
            cr = int(c)
            for _ in range(0,cr):
                print(tmp,end="")
    print()