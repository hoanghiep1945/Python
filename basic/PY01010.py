t = int(input())
while t>0 :
    t-=1
    s = list(input())
    if(s[0]+s[1] != s[len(s)-2]+s[len(s)-1]) : print("NO")
    else :  print("YES")