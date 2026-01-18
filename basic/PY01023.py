import math

for _ in range(int(input())) :
    n = int(input())
    print("1 ",end="")
    for i in range(2,int(math.sqrt(n))+1) :
        cnt = 0
        ok = 0
        if n%i==0:
            ok = 1
            while(n%i == 0):
                cnt+=1
                n//=i
            print(f"* {i}^{cnt}",end =" ")
            if(n//i)%i == 0 : 
                print(f"* {n//i}")
                n//=i
        
    if(n > 1) : print(f"* {n}^1")