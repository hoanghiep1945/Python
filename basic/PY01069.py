from itertools import product

N = int(input())
digits = ['2','3','5','7']

for length in range(4, N+1):
    # sinh ra tổ hợp có length phần tử từ tập digits
    for p in product(digits, repeat=length):
        if set(p) == set(digits) and p[-1] != '2':
            print("".join(p))