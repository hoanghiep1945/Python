import math

s = input()
a = list(map(int,input().split()))
a.sort()
for i in range(0,len(a)) :
    for j in range(1,len(a)):
        if(a[i]<a[j] and math.gcd(a[i],a[j]) == 1) :
            print(a[i], a[j])