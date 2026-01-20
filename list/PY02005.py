s = input()
a = list(map(int,input().split()))
cnt = 0
for i in range(0,len(a)):
    for j in range(1,len(a)) :
        if(i<j and a[i] > a[j]) : cnt+=1
        
print(cnt)