n = int(input())
a = []
while len(a) < n:
    a.extend(map(int, input().split()))
d = [0]*max(a)
if(len(a) == len(d)) : print("Excellent!")
else :
    for i in range(len(d)) :
        if i+1 not in a :
            print(i+1)