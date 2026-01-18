t = int(input())
for _ in range(t) :
    n = int(input())
    if(n%2 == 0) :
        sum = 0.0
        for i in range(2,n+2,2) :
            sum += 1/i
        print(f"{sum:.{6}f}")
    else :
        sum = 0.0
        for i in range(1,n+2,2) :
            sum += 1/i
        print(f"{sum:.{6}f}")