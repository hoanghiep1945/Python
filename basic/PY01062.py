import math

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())) :
    s = input()
    bth = 0
    ngto = 0
    for i in range(len(s)) :
        if nt(int(s[i])) : ngto+=1
        else : bth += 1
    if(nt(len(s)) and ngto > bth) : print("YES")
    else : print("NO")