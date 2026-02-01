while True:
    line = input().strip()
    if line == "0":
        break
    k, s = line.split()
    k = int(k)
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    kq = ""
    for ch in s:
        kq += P[(P.index(ch) + k) % 28]
    print(kq[::-1])