with open("VANBAN.in", "r", encoding="utf-8") as f:
    w = f.read().split()

p = [x for x in w if len(x) > 1 and x == x[::-1]]
L = max(map(len, p))

seen = set()
for x in p:
    if len(x) == L and x not in seen:
        seen.add(x)
        print(x, w.count(x))
