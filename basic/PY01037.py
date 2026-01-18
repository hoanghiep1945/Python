def d(n):
    c=0;i=1
    while i*i<=n:c+=1+(i*i!=n)*(n%i<1);i+=1
    return c
def check(n) :
    cnt = 0 
    for i in range(1,n):
        cnt += d(i)
    return d(n) > cnt
for _ in range(int(input())) :
    n = int(input())
    for i in range(n,pow(10,6)) :
        if(check(i)) :
            print(i)
            break