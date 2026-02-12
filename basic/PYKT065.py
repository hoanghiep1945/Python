import sys

def primes_upto(n):
    a = [1]*(n+1); a[0]=a[1]=0
    for i in range(2,int(n**0.5)+1):
        if a[i]:
            for j in range(i*i,n+1,i): a[j]=0
    return [i for i in range(2,n+1) if a[i]]

def solve(l,r,n):
    p = primes_upto(n)
    bad = 0
    a = [(1,0)]
    for x in p:
        b = a[:]                 # không chọn x
        for prod,par in a:       # chọn x
            np = prod*x
            if np<=r:
                c = r//np - (l-1)//np
                bad += c if par==0 else -c
                b.append((np,1-par))
        a = b
    return (r-l+1) - bad

while 1:
    s = input()
    if s == '-1': break
    l,r = map(int,s.split())
    n = int(input())
    print(solve(l,r,n))
