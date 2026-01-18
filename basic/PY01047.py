import math

for _ in range(int(input())) :
    s = input()
    n = int(s[-4:])
    ok = 0
    if n < 2 :
        print("NO")
        continue
    for i in range(2,int(math.sqrt(n))+1) :
        if(n%i == 0):
            print("NO")
            ok = 1
            break
    if(ok == 0) : print("YES")