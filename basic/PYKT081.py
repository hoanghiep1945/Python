for _ in range(int(input())):
    s = input().strip()
    a = s.split('.')

    if len(a) != 4:
        print("NO")
        continue

    ok = 1
    for x in a:
        if not x.isdigit():
            ok = 0
            break
        v = int(x)
        if v < 0 or v > 255:
            ok = 0
            break

    print("YES" if ok else "NO")
