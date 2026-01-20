def sang(n):
    is_prime = [True] * (n + 1)
    if n >= 0: is_prime[0] = False
    if n >= 1: is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime
#main

n, x = map(int, input().split())

p = sang(20000)  
primes = []
for i in range(2, 20001):
    if p[i]:
        primes.append(i)
        if len(primes) == n:
            break

cur = x
print(cur, end=" ")
for pr in primes:
    cur += pr
    print(cur, end=" ")