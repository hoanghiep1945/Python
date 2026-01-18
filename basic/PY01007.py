t = int(input())
while t>0 :
    t-=1
    n,x,m = map(float,input().split())
    y=0
    while n < m :
        y+=1
        n=n*(1+x/100)

    print(y)