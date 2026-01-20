import math

def nto(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

n = int(input())
d = [0]*1000000
a = list(map(int,input().split()))
for c in a :
    if(nto(c)) : d[c]+=1
for c in a :
    if(nto(c) and d[c]>0) : 
        print(c, d[c])
        d[c] = 0