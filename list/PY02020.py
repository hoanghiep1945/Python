s = input()
a = list(map(float,input().split()))
amax = max(a)
amin = min(a)
while amax in a : a.remove(amax)
while amin in a : a.remove(amin)
tmp = 0
for c in a :
    tmp += c
print(f"{tmp/len(a):.2f}")