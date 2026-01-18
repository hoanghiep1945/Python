t = int(input())
while t > 0:
    t -= 1
    # biến số thành mảng các char 
    s = list(input().strip())   
    n = len(s)

    # làm tròn từ phải sang trái
    for i in range(n - 1, 0, -1):
        if int(s[i]) >= 5:
            s[i - 1] = str(int(s[i - 1]) + 1)
        s[i] = '0'

    print(''.join(s))
