a = []
for _ in range(int(input())):
    name = input().strip()
    C, T = map(int, input().split())
    a.append((name, C, T))

a.sort(key=lambda x: (-x[1], x[2], x[0]))

for name, C, T in a:
    print(f"{name} {C} {T}")
