import math

def check(n):
    if n<2 : return False
    for i in range(2,int(math.sqrt(n))+1) :
        if n%i == 0 : return False
    return True

def gcd(a,b) :
    while b>0:
        r = a%b
        a=b
        b= r
    return a

t = int(input())
while t>0:
    t-=1
    n = int(input())
    sum=0
    for i in range(1,n):
        if(gcd(i,n) == 1) : sum+=1
    if(check(sum)) : print("YES")
    else : print("NO")
