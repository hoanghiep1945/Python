while True :
    n=int(input())
    if n == 0 : break
    a=[]
    for _ in range(n):
        x = int(input())
        a.append(x)
    if(max(a) == min(a)) : print("BANG NHAU")
    else : print(min(a), max(a))