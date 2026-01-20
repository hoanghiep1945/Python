while True:
    n = int(input())
    if  n == 0 : break
    if(n == 1) : 
        print(1)
        continue
    s=set()
    s.add(n)
    while n != 1 :
        if(n%2 == 0): n=n//2
        else : n=n*3+1
        s.add(n)
    print(len(s))