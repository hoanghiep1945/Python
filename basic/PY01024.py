def check(n):
    s = str(n)
    for i in range(0,len(s)-1):
        if(abs(int(s[i])-int(s[i+1])) != 2) : return False
    return True

t = int(input())
while t>0 :
    t-=1
    n = int(input())
    total = sum(int(ch) for ch in str(n))
    if(check(n) == False) :
        print("NO")
        continue
    if(total % 10 != 0) :
        print("NO")
        continue
    print("YES")
