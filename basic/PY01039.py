def kc(n) :
    s = str(n)
    for i in range(0,len(s)-2):
        if(s[i] != s[i+2]) : return False
    return True

for _ in range(int(input())) :
    n = int(input())
    if kc(n) : print("YES")
    else : print("NO")