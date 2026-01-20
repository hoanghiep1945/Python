import math

for _ in range(int(input())) :
    s = input()
    a = list(map(int,input().split()))
    a.sort(key = lambda x : (math.prod(int(ch) for ch in str(x)),x))
    for x in a:
        print(x,end =" ")
    print("")