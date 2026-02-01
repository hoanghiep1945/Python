import math

def nto(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

N = int(input())
A = list(map(int, input().split()))

seen = set()
a = []
for x in A:
    if x not in seen:
        seen.add(x)
        a.append(x)
        
wa = [0] * len(a)
wb = [0] * len(a)

wa[0] = a[0]
for i in range(1, len(a)):
    wa[i] = wa[i-1] + a[i]

wb[len(a)-1] = a[len(a)-1]
for i in range(len(a)-2, -1, -1):
    wb[i] = wb[i+1] + a[i]

ok = 1
for i in range(len(a) - 1):   
    if nto(wa[i]) and nto(wb[i+1]):  
        ok = 0
        print(i)
        break

if ok == 1:
    print("NOT FOUND")
