DIG = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for _ in range(int(input())):
    n, b = map(int, input().split())

    if n == 0:
        print(0)
        continue

    s = ""
    while n > 0:
        s = DIG[n % b] + s
        n //= b

    print(s)
