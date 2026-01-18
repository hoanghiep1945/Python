def check(n) :
    if str(n) != str(n)[::-1] : return False
    if len(str(n)) % 2 != 0 : return False
    for c in str(n):
        if(int(c) % 2 != 0 ) : return False
    return True

for _ in range(int(input())) :
    for i in range(22,int(input()),2):
        if(check(i)) : print(i,end=" ")
    print("")