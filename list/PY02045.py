s = input()
while(len(s) != 1) :
    res = len(s)//2
    s = str(int(s[:res])+int(s[res:]))
    print(s)