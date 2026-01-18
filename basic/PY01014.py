a, k, n = map(int, input().split())

ok = False
# a+b=mk => b=mk-a>0 => m>a/k
m = (a // k) + 1   
# a+b = mk <= n
while m * k <= n:
    b = m * k - a
    if b > 0:
        print(b, end=" ")
        ok = True
    m += 1

if not ok:
    print(-1)
