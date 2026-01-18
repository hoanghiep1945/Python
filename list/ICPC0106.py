import re

t = int(input())

for _ in range(t):
    b = int(input())
    s = input().strip()

    # Bước 1: xác định k = số bit cho 1 chữ số ở hệ b
    if b == 2:
        k = 1
    elif b == 4:
        k = 2
    elif b == 8:
        k = 3
    else:  # b == 16
        k = 4

    # Bước 2: thêm '0' vào đầu để độ dài chia hết cho k
    # r là số kí tự còn thiếu
    r = len(s) % k
    if r != 0:
        s = '0' * (k - r) + s

    # Bước 3: chuyển từng nhóm k bit thành 1 ký tự kết quả
    digits = "0123456789ABCDEF"
    ans = ""

    i = 0
    while i < len(s):
        group = s[i:i+k]          # lấy k bit
        value = int(group, 2)     # đổi nhóm bit sang số (0..15)
        ans += digits[value]      # đổi số sang ký tự
        i += k

    # Bước 4: bỏ số 0 ở đầu (nếu có)
    ans = ans.lstrip('0')
    if ans == "":
        ans = "0"

    print(ans)
