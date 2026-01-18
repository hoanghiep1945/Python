for _ in range(int(input())):
    _, _, s, w = input().split()
    s = float(s)
    w = float(w)

    avg = (s + w) / 2

    x = avg * 2
    if x - int(x) == 0.5:
        x = int(x) + 1
    else:
        x = int(x)

    print(f"{x / 2:.1f}")
