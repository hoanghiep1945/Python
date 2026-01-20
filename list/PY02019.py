import math

s = input()
a = list(map(int,input().split()))
a.sort()
for i in range(len(a)):
    for j in range(1,len(a)):
        if(math.gcd(a[i],a[j])==1 and a[i]<a[j]):
            print(a[i], a[j])