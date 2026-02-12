from itertools import combinations

n , k = map(int,input().split())
d = list(map(str,input().split()))
d = sorted(set(d))
for comb in combinations(d,k):
    print(" ".join(comb))