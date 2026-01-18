import math

def nt(n):
    if(n < 2) : return False
    for i in range(2, int(math.sqrt(n))+1) :
        if(n%i == 0) : return False
    return True

def check(n) :
    for i in range(len(n)):
        if i % 2 == 0 and int(n[i]) % 2 == 1 : return False
        if i % 2 == 1 and int(n[i]) % 2 == 0 : return False
    total = sum(int(ch) for ch in n)
    return nt(total)

for _ in range(int(input())) :
    if check(input()) : print("YES")
    else : print("NO")