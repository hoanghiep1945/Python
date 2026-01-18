import math

def nt(n):
    if n < 2 : return False
    for i in range(2,int(math.sqrt(n))+1) :
        if(n%i == 0) : return False
    return True

def check(n) :
    if(nt(int(len(n))) == False) : return False
    nto = 0
    bth = 0
    for c in n:
        if(nt(int(c))) : nto+=1
        else : bth+=1
    return nto > bth

for _ in range(int(input())) :
    s = input()
    if(check(s)) : print("YES")
    else : print("NO")
    