import sys

a = list(map(int,sys.stdin.read().split()))
s = set()
for c in a :
    c = c%42
    s.add(c)
print(len(s))