import sys
import math

def mod_big(b, a):
    r = 0
    for ch in b.strip():
        r = (r * 10 + (ord(ch) - 48)) % a
    return r

def main():
    input = sys.stdin.readline
    t = int(input())
    out = []

    for _ in range(t):
        a = int(input().strip())
        b = input().strip()

        out.append(str(math.gcd(a, mod_big(b, a))))

    sys.stdout.write("\n".join(out))

main()
