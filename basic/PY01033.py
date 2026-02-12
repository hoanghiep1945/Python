import math

L, R = map(int, input().split())

for a in range(L, R - 1):
    for b in range(a + 1, R):
        if math.gcd(a, b) != 1:
            continue
        for c in range(b + 1, R + 1):
            if math.gcd(a, c) == 1 and math.gcd(b, c) == 1:
                print(f"({a}, {b}, {c})")
