def to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

def convert(s, base_a, base_b):
    n = int(s, base_a)      # về hệ 10
    return to_base(n, base_b)

for _ in range(int(input())) :
    n , b = map(int,input().split())
    print(convert(str(n),10,b))