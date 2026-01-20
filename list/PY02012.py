import sys

n = int(input())
a = list(map(int, sys.stdin.read().split()))

chan = []
le = []

for x in a:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)
chan.sort()              
le.sort(reverse=True)    
i = j = 0
res = []
for x in a:
    if x % 2 == 0:
        res.append(chan[i])
        i += 1
    else:
        res.append(le[j])
        j += 1
print(*res)
