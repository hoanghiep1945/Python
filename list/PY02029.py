_, M = map(int, input().split())
a = list(map(int, input().split()))

cnt = [0]*(M+1)
for x in a: cnt[x]+=1

s = sorted({x for x in cnt[1:] if x > 0}, reverse=True)

if len(s) < 2:
    print("NONE")
else:
    # lấy ứng viên đầu tiên thỏa mãn điều kiện
    print(next(i for i in range(1, M+1) if cnt[i] == s[1]))
