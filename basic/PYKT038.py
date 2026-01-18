s = input().strip()

# bổ sung 0 cho đủ bội số của 3
while len(s) % 3 != 0:
    s = '0' + s

res = ""

for i in range(0, len(s), 3):
    val = 0
    for j in range(3):
        val = val * 2 + (ord(s[i + j]) - 48)
    res += str(val)

# bỏ số 0 dư đầu 
res = res.lstrip('0')
if res == "":
    res = "0"

print(res)
