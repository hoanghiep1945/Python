def fibo_list(n):
    a = [0, 1]
    for _ in range(2, n + 1):
        a.append(a[-1] + a[-2])
    return a



for _ in range(int(input())):
    a, b = map(int, input().split())
    fb = fibo_list(b)
    for i in range(a, b + 1):
        print(fb[i], end=" ")
    print()
