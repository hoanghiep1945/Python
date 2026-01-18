def check(n) :
    if n<2 : return False
    for i in range(2,n) :
        if n%i == 0 :
            return False
    return True
t = int(input())
while t>0:
    t-=1
    n=int(input())
    sum = 0
    while n>0:
        sum += n%10
        n//=10
    if check(sum) : print("YES")
    else : print("NO")

