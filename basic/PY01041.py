for _ in range(int(input())):
    s=input()
    i=1
    while i<len(s) and s[i]>s[i-1]: i+=1
    print("YES" if i>1 and i<len(s) and all(s[j]<s[j-1] for j in range(i+1,len(s))) else "NO")
