_,_ = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
da = [0]*1001
db = [0]*1001
s = set()
for c in a : 
    da[c]+=1
    s.add(c)
for c in b : 
    db[c]+=1
    s.add(c)
for c in s :
    if(da[c] > 0 and db[c] > 0) : 
        print(c,end=" ")
print()
for c in s :
    if(da[c] > 0 and db[c] == 0) : 
        print(c,end=" ")
print()
for c in s :
    if(da[c] == 0 and db[c] > 0) : 
        print(c,end=" ")