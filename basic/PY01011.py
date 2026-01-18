def check(n) :
    s = str(n)
    return s == s[::-1]

def SoDep(n):
    if(check(n) == False) : return False
    Sum = 0
    while n>0:
        if(n%10 != 0 and n%10 != 2 and n%10 != 4 and n%10 != 6 and n%10 != 8):
            return False
        Sum += 1
        n//=10
    return Sum%2 == 0

t = int(input())
while t>0 :
    t-=1
    n=int(input())
    for i in range(11,n) :
        if(SoDep(i)) : print(i,end=" ")
    print("")
       