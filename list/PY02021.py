t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    i = j = l = 0
    res = []

    while i < n and j < m and l < k:
        a, b, c = A[i], B[j], C[l]
        if a == b == c:
            res.append(a)
            i += 1; j += 1; l += 1
        else:
            mn = min(a, b, c)
            if a == mn: i += 1
            if b == mn: j += 1
            if c == mn: l += 1

    print(*res) if res else print("NO")
