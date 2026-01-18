t = int(input())
for _ in range(t):
    p, q = input().split()
    if(p > q) :
        tmp = p
        p = q
        q = tmp
    x1 = input().strip()
    x2 = input().strip()

    mn = int(x1.replace(q, p)) + int(x2.replace(q, p))
    mx = int(x1.replace(p, q)) + int(x2.replace(p, q))

    print(mn, mx)
