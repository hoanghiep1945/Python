s = input()
res = ''
cnt = 0

for i in range(len(s) - 1, -1, -1):
    res = s[i] + res
    cnt += 1
    if cnt % 3 == 0 and i != 0:
        res = ',' + res

print(res)
