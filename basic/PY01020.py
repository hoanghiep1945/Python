t = int(input())
while t>0 :
    t-=1
    s = input()
    print("YES" if s[len(s)-2]+s[len(s)-1]=="86" else "NO")