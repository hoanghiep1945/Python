for t in range(int(input())):
    s1 = input()
    s2 = input()
    if len(s1) != len(s2):
        print(f"Test {t+1}: NO")
    else:
        if sorted(s1) == sorted(s2):
            print(f"Test {t+1}: YES")
        else:
            print(f"Test {t+1}: NO")