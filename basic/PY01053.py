for _ in range(int(input())) :
    print("YES" if sum(int(ch) for ch in input())%3==0 else "NO")