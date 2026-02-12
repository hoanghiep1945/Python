def to_base(n,base) :
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kq = ''
    if n == 0:
        return "0"
    while n != 0 :
        kq = digits[n%base] + kq
        n //= base
    return kq

def convert(s,a,b):
    kq = int(s,a)
    return to_base(kq,b)

s = input()
while len(s) % 3 != 0 : s = "0"+s
kq = ""
i = 0
while i < len(s) :
    kq += convert(s[i:i+3],2,8)
    i += 3
print(kq)