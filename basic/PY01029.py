import math

t = int(input())
while t>0 :
    t-=1
    n=int(input())
    if(math.gcd(n,int(str(n)[::-1])) == 1) : print("YES")
    else : print("NO")