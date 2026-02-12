def to_base3(x):
    s = ""
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s

t = int(input())
for _ in range(t):
    N = int(input())
    
    count = 0
    num = 1
    res = []
    
    while count < N:
        s = to_base3(num)
        if s.count('2') > len(s) / 2:
            res.append(s)
            count += 1
        num += 1
    
    print(*res)