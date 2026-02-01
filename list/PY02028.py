import math

def nto(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

s = input()
a = list(map(int,input().split()))
res = []
for c in a :
    if nto(c) : res.append(c)
res.sort()
kq = []
i = 0
for c in a :
    if(nto(c)) : 
        kq.append(res[i])
        i+=1
    else : kq.append(c)
for c in kq :
    print(c,end=" ")