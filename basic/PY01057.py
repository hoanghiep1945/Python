import math

def nt(n):
    if(n < 2) : return False
    for i in range(2, int(math.sqrt(n))+1) :
        if(n%i == 0) : return False
    return True

def check(n) :
    for i in range(len(n)):
        if nt(i) == True and nt(int(n[i])) == False : return False
        if nt(i) == False and nt(int(n[i])) == True : return False
    return True

for _ in range(int(input())) :
    if check(input()) : print("YES")
    else : print("NO")