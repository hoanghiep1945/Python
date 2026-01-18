n = int(input())
sum4=0
sum7=0
while n>0:
    if(n%10 == 4) : sum4+=1
    if(n%10 == 7) : sum7+=1
    n//=10
if(sum4+sum7 == 4 or sum4+sum7 == 7) : print("YES")
else : print("NO")