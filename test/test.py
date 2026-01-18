def la_ngto(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def in_n_ngto(n):
    dem, x = 0, 2
    while dem < n:
        if la_ngto(x):
            print(x, end=" ")
            dem += 1
        x += 1

n = int(input("Nhập n: "))
in_n_ngto(n)
