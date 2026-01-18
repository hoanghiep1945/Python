def check(n):
    if(len(n) <= 1) : return False
    return n == n[::-1]

for _ in range(int(input())) :
    s = input()
    n = sum(int(ch) for ch in s)
    if(check(str(n))) : print("YES")
    else : print("NO")