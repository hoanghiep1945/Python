s1 = input().lower()
s2 = input().lower()

set1 = set(s1.split())
set2 = set(s2.split())

hop = sorted(set1 | set2)
giao = sorted(set1 & set2)

print(" ".join(hop))
print(" ".join(giao))