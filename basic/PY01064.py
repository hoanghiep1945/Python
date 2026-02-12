t = int(input())
# sâu được tạo bởi 3 chuỗi là S(n) = S(n-1) + mid + S(n-1)
for _ in range(t):
    n, k = map(int, input().split())
    while True:
        mid = 2 ** (n - 1) # vị trí giữa
        if k == mid:
            print(chr(ord('A') + n - 1))
            break
        if k > mid:
            k -= mid
        n -= 1 # n-=1 để thu nhỏ bài toán từ S(n) thành S(n-1) 